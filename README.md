⁸# Info
Order given files at start index or reorder some files specific. File names are in format of integer.
Example: 2018.png 2019.png 2020.png ...

# Example
Lets say you have image files in directory named "test".
These image files are named by numbers in order.
```
test/
    2018.png
    2019.png
    2021.png
    2022.png
    2023.png
    2024.png
```

You want to have these files being in order. But 2021 must be renamed to 2020 and in according 2022 to 2021 and so far.
You simply type:
```
python3 indexing-cli.py -s test -sft .png -st 2018
```
Ta Da you achived the goal.
Now files:
```
test/
    2018.png
    2019.png
    2020.png
    2021.png
    2022.png
    2023.png
```

### Reordering Feature

# Usage
```
python3 indexing-cli.py [parameters]
```
```
OrderingCLI [-h] -s SRC_DIR -sft SOURCE_FILE_TYPE [-st START] [-r REVERSE_ORDERING]
                   [-ro ['FROM', 'TO'] [['FROM', 'TO'] ...]] [-f FORMAT] [-v]
options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose the renaming and total number of renamed files.

Directory:
  -s, --src-dir SRC_DIR
                        Source directory to read files from.

File Types:
  -sft, --source-file-type SOURCE_FILE_TYPE
                        Source file type to select from list of files in directory.

Ordering:
  -st, --start START    Order the target from starting given number.
  -r, --reverse-ordering REVERSE_ORDERING
                        Reverse ordering, takes 1 for True, 0 for False
  -ro, --reorder ['FROM', 'TO'] [['FROM', 'TO'] ...]
  -f, --format FORMAT   If file names are in date format, then specify format with this. It uses
                        datetime.strptime(format=format)
```
