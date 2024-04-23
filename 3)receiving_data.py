import sqlite3

database2 = sqlite3.connect("database2.db")
cursor = database2.cursor()

create_table= "CREATE TABLE IF NOT EXISTS personal(name TEXT, surname TEXT, department TEXT, fee INT)"

cursor.execute(create_table)

database2.commit()

cursor.execute("INSERT INTO personal VALUES('Levent','Ertunalılar','Bilişim',4000)")
cursor.execute("INSERT INTO personal VALUES('Ali','Demir','Satın Alma',5000)")
cursor.execute("INSERT INTO personal VALUES('Selin','Aksoy','İnsan Kaynakları',5500)")
cursor.execute("INSERT INTO personal VALUES('Emrah','Doğu','İnsan Kaynakları',5500)")
cursor.execute("INSERT INTO personal VALUES('Meltem','Doğan','Satın Alma',5000)")

database2.commit()

def receive_data():
    cursor.execute("SELECT * FROM personal")
    list = cursor.fetchall()
    for i in list:
        print(i)

def receive_person():
    cursor.execute("SELECT name,surname FROM personal")
    list = cursor.fetchall()
    for i in list:
        print(i)

def receive_department():
    cursor.execute("SELECT * FROM personal WHERE department = 'Satın Alma'")
    list = cursor.fetchall()
    for i in list:
        print(i)

receive_department()

database2.close()