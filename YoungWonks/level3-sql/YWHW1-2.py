import sqlite3

conn = sqlite3.connect('YWHW1-2.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (Username TEXT,Password TEXT,Firstname TEXT,Lastname TEXT,Age INTEGER,DateofBirth TEXT)')

c.execute("INSERT INTO users ('Hungry', 'Password', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('Food', 'Password', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('Thirsty', 'Password', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('Drink', 'Password', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('AmazingPassword', 'NoPassword', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('HorriblePassword', '1234', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('CantPronounceName', 'NotEnoughTongues', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('ChickenNuggets', 'Yummy', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('WaterBottle', 'WaterBottle?', 'First Name', 'Last Name', 1, 'January 1, 1111')")
c.execute("INSERT INTO users ('TheCowGoesMoo', 'Mooooo', 'First Name', 'Last Name', 1, 'January 1, 1111')")

conn.commit()
conn.close()