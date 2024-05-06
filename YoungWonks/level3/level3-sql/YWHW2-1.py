import sqlite3

# Setup
conn = sqlite3.connect('ItemsDatabase.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS items (num INTEGER, name TEXT, description TEXT)")

# Insert values
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")
c.execute("INSERT INTO items VALUES (XXXXX, XXXXX, XXXXX)")

# Display data
c.execute("SELECT * FROM items")
data = c.fetchall()




conn.commit()
conn.close()