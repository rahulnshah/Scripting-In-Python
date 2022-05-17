# Scripting-In-Python
(portfolio project)
## What is it?
This repository consists of some .py files I wrote to test out some modules of the [Python Standard Library](https://docs.python.org/3/library/).
 
## Files
- [recursionEx.py](recursionEx.py)
    - It is a python script that imports the turtle module of python to recursively print the word "recursion" in middle of the viewer's window with a Turtle object.
- [tellTime.py](tellTime.py)
    - It is a python script that imports the turtle, time, and datetime module of python and calculates amount of hours and minutes left until the day ends.
- [collegeEssayDBMS.py](essayDataBaseScripts/collegeEssayDBMS.py)
    - What is ```import sqlite3```?
        - 1) Used to to connect to an SQLite database in Python
        - 2) To execute queries, you use the cursor object, which is obtained from the connection 
    - What is ```import os``` and ```os.scandir(directory)```?
        - 1) 
    - What is ```import csv```?
        - 1) CSV stands for “Comma Separated Values.” First line of it is a header defining columns of the file and the rest are record of the file.  One can say # of records present in a csv file are always N + 1, where N is # of non-headers in a csv file. 
        - 2) csv modules's reader method is as the name suggests used to read an opened csv file. 
        - 3) csv files could be read or seen in any other mode using the with context manager just as a text file, but I've kept my code simple here. 
    - What is ```encoding=utf-8```?
        - 1) It is a keyword/named argument.  You can pass required and optional arguments into a function as keyword arguments. 
        - 2) Here the argument means all files in myCollegeEssays are encoded in UTF-8 (8-bit Unicode, as opposed to UTF-16 or UTF-32).  This is done so to avoid ```Traceback (most recent call last):  ...
        UnicodeDecodeError: 'charmap' codec can't decode byte 0x81 in position 36593: character 
        maps to <undefined> ```, which occurs in Windows upon opening a text file whose path is passed into the open function as its first argument.  
- [output.txt](essayDataBaseScripts/output.txt)
    - Shows result sets of running each SQL query, such as CREATE TABLE, SELECT, and INNER JOIN 

## Further Reading 
- [python-tutorial-working-with-csv-file-for-data-science](https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/)
- [Getting a Traceback error when opening a file in python](https://sites.pitt.edu/~naraehan/python3/mbb12.html)
- [how-to-iterate-over-files-in-directory-using-python](https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/)

