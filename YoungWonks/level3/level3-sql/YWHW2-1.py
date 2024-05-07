import sqlite3

# Setup
conn = sqlite3.connect('ItemsDatabase.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS items (num INTEGER, name TEXT, description TEXT)")

# Insert values
c.execute("INSERT INTO items VALUES (89263, 'Nutcracker', 'Cracks nuts for you')")
c.execute("INSERT INTO items VALUES (01924, 'Glass Jar', 'Stores items for you')")
c.execute("INSERT INTO items VALUES (00287, 'Paper Towel Roll', 'Cleans stuff')")
c.execute("INSERT INTO items VALUES (29753, 'Air Conditioner', 'Cools down the air')")
c.execute("INSERT INTO items VALUES (10283, 'Pencil', 'Writes stuff down')")
c.execute("INSERT INTO items VALUES (61237, 'Eraser', 'Erases pencil mark')")
c.execute("INSERT INTO items VALUES (01923, 'Lollipop', 'Suck on it')")
c.execute("INSERT INTO items VALUES (36472, 'Glue Bottle', 'Stick stuff')")
c.execute("INSERT INTO items VALUES (10938, 'Chair', 'Sit on it')")
c.execute("INSERT INTO items VALUES (18374, 'Desk', 'Put stuff on it')")

# Display data
c.execute("SELECT * FROM items")
data = c.fetchall()
for item in data:
    print(f'{item[0]} {item[1]}: {item[2]}')


conn.commit()
conn.close()