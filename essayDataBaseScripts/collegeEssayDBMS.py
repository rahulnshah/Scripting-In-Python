import sqlite3
import os
import csv

if __name__ == '__main__':

    conn = sqlite3.connect(':memory:')

    with conn:

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS essays (
                          title TEXT PRIMARY KEY,
                          content TEXT,
                          essay_url TEXT,
                          words INTEGER,
                          course_id INTEGER NOT NULL,
                          FOREIGN KEY (course_id) REFERENCES courses (id)
                        );""")
       
        cursor.execute("""CREATE TABLE IF NOT EXISTS departments (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT
                        );""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS courses (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          department_id INTEGER NOT NULL,
                          FOREIGN KEY (department_id) REFERENCES departments (id)
                        );""")

        # insert into the departments table - positional parameters example AUTOINCREMENT Fails to work this way 
        records = [(1,"Department of Humanities and Social Sciences"),
                   (2,"Federated Department of History"),
                   (3,"Department of Informatics"),
		   (4,"Department of Physics"),
                   (5,"Department of Management")]
        cursor.executemany("INSERT INTO departments VALUES (?,?);", records)
        # insert into the courses table - second way to do it, but where AUTOINCREMNT does work
        create_courses = """
                        INSERT INTO
                          courses (name, department_id)
                        VALUES
                          ('Writing, Speaking, Thinking I', 1),
                          ('Physics I Lab', 4),
                          ('Writing, Speaking, Thinking II', 1),
                          ('Physics II Lab', 4),
                          ('The Twentieth-Century World', 2),
                          ('Microeconomics', 5),
                          ('U.S. As A World Power', 2),
                          ('Computers, Society and Ethics', 3);
                        """
        cursor.execute(create_courses)

        print("departments:")
        cursor.execute("""SELECT * FROM departments""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        print(cursor.fetchall())     
        print()
        print("courses:")
        cursor.execute("""SELECT * FROM courses""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        print(cursor.fetchall())
        print()
        # inner join example
        select_courses = """SELECT departments.name, courses.name
                            FROM courses
                            INNER JOIN departments ON courses.department_id=departments.id;"""
        # courses and their corresponding departments
        cursor.execute(select_courses)
        inner_join_res = cursor.fetchall()
        print("inner join result set:")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in inner_join_res:
            print(rec)
        print()
        # drop column of the essays table
        cursor.execute("""ALTER TABLE essays DROP COLUMN essay_url;""");
        cursor.execute("""SELECT * FROM essays""")
        # essay_url column dropped 
        # column_names = [description[0] for description in cursor.description]
        # print(column_names)

        # get all data that is needed for the essays table in the data.csv file - loop each file in the myCollegeEssays directory 
        directory = 'myCollegeEssays'
        # overwrtie the csv file
        header = ["Title","Words","CourseId", "Content"]
        csvFile =  open('data.csv', mode='w',newline='')
        # create csv writer
        writer = csv.writer(csvFile)
        writer.writerow(header)
        # close the file
        csvFile.close()
                
        for filename in os.scandir(directory):
            if filename.is_file():
                aRow = list()
                aFileName = filename.path[filename.path.index("\\") + 1:filename.path.index(".txt")]
                # print(type(filename.path) , filename.path)
                total_words = 0
                file = open(filename.path, 'r', encoding="utf-8")
                read_data = file.read()
                read_data = read_data.replace("\n", " ")
                total_words = len(read_data.split())
                # print('Total Words:', total_words)
                file.close()
                aRow.append(aFileName)
                aRow.append(total_words)
                # append the courseid to aRow
                if read_data.lower().find("hum101") >= 0:
                    aRow.append(1)
                elif read_data.lower().find("hum102") >= 0:
                    aRow.append(3)
                elif read_data.lower().find("hist213") >= 0:
                    aRow.append(5)
                elif read_data.lower().find("hist363") >= 0:
                    aRow.append(7)
                elif read_data.lower().find("phys111") >= 0:
                    aRow.append(2)
                elif read_data.lower().find("phys121") >= 0:
                    aRow.append(4)
                elif read_data.lower().find("econ265") >= 0:
                    aRow.append(6)
                else: # is350
                    aRow.append(8)
                aRow.append(read_data)
                # write to the csv file 
                csvFile =  open('data.csv', mode='a', newline='', encoding="utf-8")
                # create csv writer
                writer = csv.writer(csvFile)
                writer.writerow(aRow)
                # close the file
                csvFile.close()
        # read data.csv and insert into the essays table 
        aCsvFile = open('data.csv', mode='r', encoding="utf-8")
        
        csvreader = csv.reader(aCsvFile)
        # skip the header 
        header = next(csvreader)
        for row in csvreader:
            #insert contents of each row in to the essays table in the order that data is declared in the CREATE TABLE query for essays table
            cursor.execute("INSERT INTO essays VALUES (:title, :content, :words, :course_id)", {"title" : row[0], "words" : int(row[1]), "course_id" : int(row[2]), "content" : row[3]})
        print("essays:")
        cursor.execute("""SELECT words FROM essays""")
        for rec in cursor.fetchall():
            print(rec)
        print()
        #inner join example 2
        select_courses = """SELECT courses.name, essays.title
                            FROM essays
                            INNER JOIN courses ON essays.course_id=courses.id;"""
        # essays and their corresponding courses
        print("inner join on essays and courses")
        cursor.execute(select_courses)
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        # GROUP BY query example to find how many toal essays I have written per course
        print("how many total essays have I written per course:")
        cursor.execute("""SELECT COUNT(title), course_id
                        FROM essays 
                        GROUP BY course_id;""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        print("inner join and where clauses together:")
        cursor.execute("""SELECT courses.name, essays.title
                        FROM essays 
                        INNER JOIN courses ON essays.course_id=courses.id WHERE essays.course_id = 2;""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        print("How many total word have I written? Enough to publish a book?")
        cursor.execute("""SELECT SUM(words) AS TotalWords FROM essays;""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        print("Writings which are less than 1000 words long:")
        cursor.execute("""SELECT title, words, course_id FROM essays WHERE words < 1000;""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        # one more comment 
        cursor.execute("""SELECT title FROM essays WHERE title LIKE '%the%' OR title LIKE '% lab % ';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        cursor.execute("""SELECT title FROM essays WHERE title LIKE '%the%' OR title LIKE '%lab% ';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        cursor.execute("""SELECT title FROM essays WHERE title LIKE '%personAL%' AND title LIKE '%narrative%';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        for rec in cursor.fetchall():
            print(rec)
        print()
        print("Writings in which I used the word \"the\":")
        # I know for sure that the word the had a space before and after it in any one of my writing if it is present in one
        cursor.execute("""SELECT title FROM essays WHERE content LIKE '% the %';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        res_set = cursor.fetchall()
        print("length of result set: " + str(len(res_set)))
        for rec in res_set:
            print(rec)
        print()
        print("Writings in which I used the word \"and\":")
        # I know for sure that the word the had a space before and after it in any one of my writing if it is present in one
        cursor.execute("""SELECT title FROM essays WHERE content LIKE '% and %';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        res_set = cursor.fetchall()
        print("length of result set: " + str(len(res_set)))
        for rec in res_set:
            print(rec)
        print()
        print("Writings in which I used a \",\":")
        cursor.execute("""SELECT title FROM essays WHERE content LIKE '%,%';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        res_set = cursor.fetchall()
        print("length of result set: " + str(len(res_set)))
        for rec in res_set:
            print(rec)
        print()
        print("Writings in which I never used the word \"the\" or \"and\":")
        cursor.execute("""SELECT title FROM essays WHERE content NOT LIKE '% the %' OR content NOT LIKE '% and %';""")
        column_names = [description[0] for description in cursor.description]
        print(column_names)
        res_set = cursor.fetchall()
        print("length of result set: " + str(len(res_set)))
        for rec in res_set:
            print(rec)
        print()
        cursor.execute("""SELECT COUNT(*) FROM essays;""")
        print("total records in essays table: " + str(cursor.fetchone()[0]))
# connection is closed - loop through the files again and rewrite data.csv; context managers DO NOT have scope of their own in Python
csvFile =  open('data.csv', mode='w',newline='')
# create csv writer
writer = csv.writer(csvFile)
writer.writerow(header)
# close the file
csvFile.close()

for filename in os.scandir(directory):
    if filename.is_file():
        aRow = list()
        aFileName = filename.path[filename.path.index("\\") + 1:filename.path.index(".txt")]
        # print(type(filename.path) , filename.path)
        total_words = 0
        file = open(filename.path, 'r', encoding="utf-8")
        read_data = file.read()
        read_data = read_data.replace("\n", " ")
        total_words = len(read_data.split())
        # print('Total Words:', total_words)
        file.close()
        aRow.append(aFileName)
        aRow.append(total_words)
        # append the courseid to aRow
        if read_data.lower().find("hum101") >= 0:
            aRow.append(1)
        elif read_data.lower().find("hum102") >= 0:
            aRow.append(3)
        elif read_data.lower().find("hist213") >= 0:
            aRow.append(5)
        elif read_data.lower().find("hist363") >= 0:
            aRow.append(7)
        elif read_data.lower().find("phys111") >= 0:
            aRow.append(2)
        elif read_data.lower().find("phys121") >= 0:
            aRow.append(4)
        elif read_data.lower().find("econ265") >= 0:
            aRow.append(6)
        else: # is350
            aRow.append(8)
        aRow.append("content erased!!!!!!!!!!!!!")
        # write to the csv file 
        csvFile =  open('data.csv', mode='a', newline='', encoding="utf-8")
        # create csv writer
        writer = csv.writer(csvFile)
        writer.writerow(aRow)
        # close the file
        csvFile.close()
        
        


