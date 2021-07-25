
# Combine MySQL Insert statements
### This simple script will help you combine single row insert statements into multi-row insert statements in a SQL script which will decrease its execution time.
## When to use it 
### Use this code if you have more than 100K records each in a single insert statement otherwise it won't make a big difference.
## Why I made this
### I had a SQL script that includes 10 million records each in a single insert statement, I ran the script on my server, but it was too slow, and it would take around 16-18 hours to finish, so I made this python script and combined each 1000 row in a single insert statement and ended up having 10K queries instead of 10M, and it took it around 25 minutes only to execute.
## Usage:
```sh
python main.py data_file.sql number_of_values output_file.sql
```
### Example:
Assume we have the following data:
```sh
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("1", "1", "1");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("2", "2", "2");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("3", "3", "3");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("4", "4", "4");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("5", "5", "5");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("6", "6", "6");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("7", "7", "7");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("8", "8", "8");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("9", "9", "9");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) VALUES ("10", "10", "10");
```

If you want 3 sets of values in each statement:
```sh
python main.py sample_data.sql 3 output.sql
```
And the output will be like this:
```sh
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) values ("1", "1", "1"), ("2", "2", "2"), ("3", "3", "3");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) values ("4", "4", "4"), ("5", "5", "5"), ("6", "6", "6");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) values ("7", "7", "7"), ("8", "8", "8"), ("9", "9", "9");
INSERT INTO `TABLE` (`column1`, `column2`, `column3`) values ("10", "10", "10");
```