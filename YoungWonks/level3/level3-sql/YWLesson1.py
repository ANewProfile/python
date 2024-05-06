import sqlite3

conn = sqlite3.connect('First_Database.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS places (Name TEXT,Population INTEGER)')

# c.execute("INSERT INTO places VALUES ('Amsterdam',1856000)")
# c.execute("INSERT INTO places VALUES ('New York',2000000)")
# c.execute("INSERT INTO places VALUES ('Hong Kong',1795000)")
# c.execute("INSERT INTO places VALUES ('USA',500000000)")

c.execute('SELECT * FROM places')
values = c.fetchall()
# print(f'{values[0][0]}: {values[0][1]}')
print(values)
# Paris: 2161000
conn.commit()
conn.close()