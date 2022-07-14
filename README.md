# Scripting-In-Python
(portfolio project)
## What is it?
This repository consists of some .py files I wrote to test out some modules of the [Python Standard Library](https://docs.python.org/3/library/).
 
## Files
- [recursionEx.py](recursion_in_python/recursionEx.py)
    - It is a python script that imports the turtle module of python to recursively print the word "recursion" in middle of the viewer's window with a Turtle object.
- [tellTime.py](using_time_module/tellTime.py)
    - It is a python script that imports the turtle, time, and datetime module of python and calculates amount of hours and minutes left until the day ends.
- [collegeEssayDBMS.py](essayDataBaseScripts/collegeEssayDBMS.py)
   -  I organized my college essays into an sqlite database. 
        - Plan-of-attack:
            - First, create 3 tables: ```essays, departments, and courses```.  ```departments``` keeps records of all NJIT departments at NJIT.  ```courses``` keeps track of all writing courses I have take at NJIT and has a ```FOREIGN KEY``` called ```department_id```. ```essays``` table has title and words of the essays I have written at NJIT as well as a ```FOREIGN KEY``` called ```course_id```. The ```essays``` table also has a column called ```content``` which stores all of my written content as ```TEXT``` in the table.  
            - Then, I insert records into the ```departments``` and ```courses``` table.
            - Next, I gathered all of my college essays into one folder in google drive and downloaded them one by one in O(n) (linear time) into ```myCollegeEssays```.  I changed every file's extension to .txt.  
            - Finally I looped every file in ```myCollegeEssays``` folder and for each file, I created a list named ```aRow```, to which I appended the file's title and total words in a text file per iteration.  At the end of an iteration, I opened ```data.csv``` in append mode and appended ```aRow``` to the file's ```writer``` object.  After filling up ```data.csv```, I reopened it and looped over its set of non-headers and inserted values in each row into the ```essays``` table. 
        - What is ```:memory:```?
            - The is a special path name can be provided to create a temporary database in RAM. If you do plan to use an actual path to a database file like a .db or .sqlite file, then substitiute ```\``` with ```\\``` in your path on your Windows script.  That is just how Python interprets a ```\```. 
        - What is ```import sqlite3```?
            - 1) Used to to connect to an SQLite database in Python
            - 2) To execute queries, you use the cursor object, which is obtained from the connection 
        - What is ```import os``` and ```os.scandir(directory)```?
            -  It returns iterator of ```os.DirEntry``` objects corresponding to the entries (files or folders) in the directory given by specified path.
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
        - Shows result sets of running each SQL query, such as CREATE TABLE, SELECT, LIKE, and INNER JOIN 

## Further Reading 
- [python-tutorial-working-with-csv-file-for-data-science](https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/)
- [Getting a Traceback error when opening a file in python](https://sites.pitt.edu/~naraehan/python3/mbb12.html)
- [how-to-iterate-over-files-in-directory-using-python](https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/)

