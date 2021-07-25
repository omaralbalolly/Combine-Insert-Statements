import re
import argparse


def get_values(lines):
    insert = None
    values = []
    for line in lines:
        insert, value = re.split("values", line, flags=re.IGNORECASE)
        values.append(value.strip(';').strip())
    return insert.strip(), values


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Required arguments for the script")
    parser.add_argument('data_file', type=str, help="Data file")
    parser.add_argument('number_of_values', type=int, help="Number of values sets in each insert statements")
    parser.add_argument('output_file', type=str, help="Output file")
    args = parser.parse_args()
    data_file = args.data_file
    number = int(args.number_of_values)
    output_file = args.output_file
    with open(data_file) as f:
        lines = [line.strip() for line in f.readlines()]
    insert, values = get_values(lines)
    new_queries = []
    values_chunks = [values[x:x + number] for x in range(0, len(values), number)]
    for chunk in values_chunks:
        ins = insert + ' values ' + ', '.join(chunk) + ';'
        new_queries.append(ins)
    with open(output_file, 'w') as f:
        for i, ins in enumerate(new_queries):
            f.write(ins)
            if i + 1 != len(new_queries):
                f.write('\n')
    print('Done !')
    print(f'Output file : "{output_file}"')
