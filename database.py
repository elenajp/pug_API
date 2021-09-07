import random
import sqlite3
from random import randint

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS
new_table(image_id INTEGER PRIMARY KEY,
        species TEXT NOT NULL, 
        shark_image TEXT NOT NULL)"""

cursor.execute(create_table)

# cursor.execute(
#     "INSERT INTO new_table (species, shark_image) VALUES ('greatwhite', './white2.jpg')")
connection.commit()


# query = cursor.execute('SELECT * FROM new_table')

# select a random row for a certain shark species
random_species = cursor.execute(
    'SELECT * FROM new_table WHERE species LIKE "greatwhite%" ORDER BY RANDOM() LIMIT 1;')


# colname = [d[0] for d in query.description]
# result_list = [dict(zip(colname, r)) for r in query.fetchall()]
# cursor.close()
# cursor.connection.close()
# print(result_list)

colname = [d[0] for d in random_species.description]
result_list = [dict(zip(colname, r)) for r in random_species.fetchall()]
cursor.close()
cursor.connection.close()
print(result_list[0]['shark_image'])
# print(random.choice(result_list))
