import sqlite3

conn = sqlite3.connect('YWHW1-1.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS nutritionfacts (Name TEXT,ServingsContainer INTEGER,ServingSize INTEGER,Calories INTEGER,Expiration TEXT)')

c.execute("INSERT INTO nutritionfacts VALUES ('Name', 1, 1, 1, '01/01/11')")
c.execute("INSERT INTO nutritionfacts VALUES ('Name', 1, 1, 1, '01/01/11')")
c.execute("INSERT INTO nutritionfacts VALUES ('Name', 1, 1, 1, '01/01/11')")
c.execute("INSERT INTO nutritionfacts VALUES ('Name', 1, 1, 1, '01/01/11')")
c.execute("INSERT INTO nutritionfacts VALUES ('Name', 1, 1, 1, '01/01/11')")
c.execute("INSERT INTO nutritionfacts VALUES ('Name', 1, 1, 1, '01/01/11')")

# c.execute('SELECT * FROM nutritionfacts')
# food_items = c.fetchall()
# for food_item in food_items:
#     print(f'{food_item[0]}:\n\tServings/Container: {food_item[1]}\n\tServing Size: {food_item[2]}\n\tCalories: {food_item[3]}\n\tExpiration Date: {food_item[4]}')

conn.commit()
conn.close()
