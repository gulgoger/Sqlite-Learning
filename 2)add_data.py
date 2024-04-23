import sqlite3

database2 = sqlite3.connect("database2.db")
cursor = database2.cursor()

create_table= "CREATE TABLE IF NOT EXISTS personal(name TEXT, surname TEXT, department TEXT, fee INT)"

cursor.execute(create_table)

database2.commit()

cursor.execute("INSERT INTO personal VALUES('Levent','Ertunalılar','Bilişim',4000)")
cursor.execute("INSERT INTO personal VALUES('Ali','Demir','Satın Alma',5000)")
cursor.execute("INSERT INTO personal VALUES('Selin','Aksoy','İnsan Kaynakları',5500)")

database2.commit()

name = input("Name:")
surname = input("Surname:")
department = input("Department:")
fee = int(input("Fee:"))

cursor.execute("INSERT INTO personal VALUES(?,?,?,?)", (name,surname,department,fee))

database2.commit()

database2.close()