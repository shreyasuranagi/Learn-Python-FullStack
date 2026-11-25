# # create the database

# import sqlite3
# conn=sqlite3.connect('data.db')
# print(conn)
# print(str(conn))
# p=conn.cursor()
# print(p)
# print(str(p))

# #create a table

# p.execute('create table Student(rollno number, name varchar, phno number, marks number)')
# print(p)
# p.commit()
# p.close()

# # insert the records

# import sqlite3
# conn = sqlite3.connect('data.db')
# p=conn.cursor()
# print(p)
# p.execute("insert into Student values(1,'aadya',2345678,86)")
# p.execute("insert into Student values(2,'brinda',6543,66)")
# p.execute("insert into Student values(3,'chala',234543,86)")
# print(p)
# conn.commit()
# conn.close()




# # read and fetch the data

import sqlite3
conn=sqlite3.connect('data.db')
p=conn.cursor() 
data = p.execute('select * from Student')
print(data) #<sqlite3.Cursor object at 0x000002223BAFBF40>
print(list(data)) # [(1, 'aadya', 2345678, 86), (2, 'brinda', 6543, 66), (3, 'chala', 234543, 86)]
print(data.fetchone()) # None
print(data.fetchmany(2))# []
#print(data.fetchmany(2)[1][0])
print(data.fetchall())
conn.close()

