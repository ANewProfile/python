import sqlite3

conn = sqlite3.connect('YWHW1-1.db')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS nutritionfacts (Name TEXT,ServingsContainer INTEGER,ServingSize TEXT,Calories INTEGER,Expiration TEXT)')

c.execute("INSERT INTO nutritionfacts VALUES ('Lactaid', 8, '1 cup', 130, '05/26/24')")
c.execute("INSERT INTO nutritionfacts VALUES ('Iodized Sea Salt', 567, '0.25 tsp', 0, '-')")
c.execute("INSERT INTO nutritionfacts VALUES ('Organic Peanut Butter', 16, '2 tbsp', 190, '12/17/24')")
c.execute("INSERT INTO nutritionfacts VALUES ('Cereal', 9, '1 cup', 160, '02/12/25')")
c.execute("INSERT INTO nutritionfacts VALUES ('Canola Oil', 63, '1 tbsp', 120, '06/29/25')")

# c.execute('SELECT * FROM nutritionfacts')
# food_items = c.fetchall()
# for food_item in food_items:
#     print(f'{food_item[0]}:\n\tServings/Container: {food_item[1]}\n\tServing Size: {food_item[2]}\n\tCalories: {food_item[3]}\n\tExpiration Date: {food_item[4]}')

conn.commit()
conn.close()
