import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()

create_table = """CREATE TABLE IF NOT EXISTS
new_table(image_id INTEGER PRIMARY KEY,
        species TEXT NOT NULL, 
        shark_image TEXT NOT NULL)"""

cursor.execute(create_table)

cursor.execute(
    "INSERT INTO new_table (species, shark_image) VALUES ('greatwhite', './white2.jpg')")
connection.commit()


# cursor.execute('SELECT * FROM new_table')
# for row in cursor.fetchall():
#     print(row)

query = cursor.execute('SELECT * FROM new_table')
colname = [d[0] for d in query.description]
result_list = [dict(zip(colname, r)) for r in query.fetchall()]
cursor.close()
cursor.connection.close()
print(result_list)
