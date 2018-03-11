import sqlite3
conn=sqlite3.connect("hello.db")
c=conn.cursor()
#c.execute('''CREATE TABLE members
#        (date text, name text, id text, age real)''')
c.execute("INSERT INTO members VALUES('2018-01-13', 'John', 'wx2561673', 24)")
conn.commit()

lis=[('2018-01-13', 'Judy', 'wx5461673', 24),
     ('2018-01-13', 'Jack', 'wx2532373', 23),
     ('2018-01-13', 'Hans', 'wx2531573', 25),]

c.executemany("INSERT INTO members VALUES (?,?,?,?)", lis)
conn.commit()

date=("2018-01-13",)
for item in c.execute("SELECT * FROM members WHERE date=?", date):
    print(item)

conn.rollback()
c.execute("SELECT * FROM members WHERE date=?", date)
print(c.fetchall())

def ret_age(x,y):
    return x+y
conn.create_function("RA", 2, ret_age)
c.execute("SELECT  RA(?,?)", (12, 23))
print(c.fetchall())

conn.close()
