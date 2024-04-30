import sqlite3

conn = sqlite3.connect('YWHW1-2.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (Username TEXT,Password TEXT,Firstname TEXT,Lastname TEXT,Age INTEGER,DateofBirth TEXT)')

c.execute("INSERT INTO users ('Hungry', 'BeefSandwich', 'Bob', 'Ross', 80, 'October 29, 1942')")
c.execute("INSERT INTO users ('Food', 'ChickenSandwich', 'Bruce', 'Lee', 82, 'November 27, 1940')")
c.execute("INSERT INTO users ('Thirsty', '12345679', 'Dwayne', 'Johnson', 51, 'May 2, 1972')")
c.execute("INSERT INTO users ('Drink', 'BluePersonGreenPersonShareSamePassword1234', 'Jeff', 'Bezos', 60, 'January 12, 1964')")
c.execute("INSERT INTO users ('AmazingPassword', 'NoPassword', 'Elon', 'Musk', 52, 'June 28, 1971')")
c.execute("INSERT INTO users ('HorriblePassword', '1234', 'Steve', 'Jobs', 68, 'Febuary 24, 1955')")
c.execute("INSERT INTO users ('CantPronounceName', 'NotEnoughTongues', 'Eurgphmthilthmsphlthm', 'Johnson', 1000, 'December 31, 1023')")
c.execute("INSERT INTO users ('ChickenNuggets', 'Yummy', 'Taylor', 'Swift', 34, 'December 13, 1989')")
c.execute("INSERT INTO users ('WaterBottle', 'WaterBottle?', 'Sundar', 'Pichai', 51, 'June 10, 1972')")
c.execute("INSERT INTO users ('TheCowGoesMoo', 'Mooooo', 'Bill', 'Gates', 68, 'October 28, 1955')")

conn.commit()
conn.close()