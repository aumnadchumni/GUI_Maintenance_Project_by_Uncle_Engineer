import sqlite3

#สร้าง connection เพื่อเชื่อมต่อกับ DB
conn = sqlite3.connect('maintenance.sqlite3')

#สร้าง Cursor เอาไว้สั่งคำสั่ง SQL
c = conn.cursor()

#create table mt_workorder name
c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    name TEXT,
                    department TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    tel TEXT ) """)

#สร้างฟังก์ชั่น INSERT
def insert_mtworkorder(tsid, name, department, machine, problem, number, tel):
    #create
    with conn:
        command = 'INSERT INTO mt_workorder VALUES(?,?,?,?,?,?,?,?)'
        c.execute(command,(None, tsid, name, department, machine, problem, number, tel)) #None แทนค่า ID เพื่อให้ระบบ Generate อัตโนมัติ
    conn.commit() #save ข้อมูลลง database

#แสดงข้อมูล
def view_mtworkorder():
    with conn:
        command = 'SELECT * FROM mt_workorder' #SELECT ข้อมูล
        c.execute(command)
        result = c.fetchall()
    return result

#Update ข้อมูล
def update_mtworkorder(tsid, field, newvalue):
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue, tsid))
    conn.commit()

#Delete ข้อมูล
def delete_mtworkorder(tsid):
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
        c.execute(command,([tsid]))
    conn.commit()

