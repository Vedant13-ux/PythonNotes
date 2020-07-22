import sqlite3
import json

conn = sqlite3.connect('course.sqlite')
cur = conn.cursor()

cur.executescript('''
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;
    DROP TABLE IF EXISTS User;

    CREATE TABLE Course(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );
    CREATE TABLE User(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );
    CREATE TABLE Member(
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY(user_id,course_id)       
    );
''')
f = open('roster_data.json').read()
data = json.loads(f)

for member in data:
    cur.execute('''
        INSERT OR IGNORE INTO User (name) 
        VALUES ( ? )''', (member[0],))
    cur.execute('SELECT id FROM User WHERE name= ? ', (member[0],))
    user_id = cur.fetchone()[0]

    cur.execute('''
        INSERT OR IGNORE INTO Course (title) 
        VALUES ( ? )''', (member[1],))
    cur.execute('SELECT id FROM Course WHERE title= ? ', (member[1],))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id,course_id,role)
        VALUES (?,?,?)''', (user_id, course_id, member[2]))


conn.commit()
