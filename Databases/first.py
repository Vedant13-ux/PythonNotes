import sqlite3
import re
# conn = sqlite3.connect('smaildb.sqlite')
# cur = conn.cursor()

# cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('CREATE TABLE Counts (org TEXT,count INTEGER)')

# fname = input('Enter File Name')
# if(len(fname) < 1):
#     fname = './mbox.txt'

# f = open(fname, 'rt')
# for line in f:
#     if not line.startswith('From: '):
#         continue
#     pieces = line.split()
#     org = pieces[1]
#     cur.execute('''SELECT count FROM Counts WHERE org=?''', (org,))
#     row = cur.fetchone()

#     if row is None:
#         cur.execute('''INSERT INTO Counts(org,count) VALUES (?,1)''', (org,))
#     else:
#         cur.execute('''UPDATE Counts SET count=count+1 WHERE org=?''', (org,))
#     conn.commit()

# sqlstr = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'
# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()

#***********************************************#


conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1):
    fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    # if not line.startswith('From: ') : continue
    # pieces = line.split()[1]
    # org = pieces.split('@')[1]
    org_list = re.findall('^From: \S+@(\S+)', line)
    if not org_list:
        continue
    org = org_list[0]

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    print(row[0])
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
				VALUES ( ?, 1 )''', (org, ))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?',
                    (org, ))

conn.commit()


# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

# for row in cur.execute(sqlstr):
#     print(str(row[0]), row[1])

# cur.close()
