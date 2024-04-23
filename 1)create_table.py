import sqlite3

database = sqlite3.connect("database.db")
cursor = database.cursor()

create_table = "CREATE TABLE IF NOT EXISTS personal (name,surname,department,fee)"

cursor.execute(create_table)

database.close()
