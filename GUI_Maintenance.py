from tkinter import * #import library ทั้งหมดของ tkinter
from tkinter import messagebox
from songline import Sendline
import csv
from datetime import datetime
from db_maintenance import * #import DB
from tkinter import ttk #Theme of tkinter

#ส่งไลน์
""""
token = 'Az61I2S6uvv0HOUtrSx4auHd4vGbUMKgVS6cOXcGeEc'
messenger = Sendline(token)
"""

#ฟังก์ชั่น Export CSV
"""
def writecsv(records_list):
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(records_list)
"""

#GUI
GUI = Tk()
GUI.title('โปรแกรมซ่อมบำรุง by Gop') #ใส่ชื่อโปรแกรม

#กำหนดขนาดหน้าจอของโปรแกรม แต่ถ้าอยากกำหนดว่าให้โปรแกรมแสดงตรงไหนของหน้าจอใช้ 200+20 เพื่อกำหนดระยะ x และ y
GUI.geometry('800x600')

#กำหนดฟอนต์
FONT1 = ('Angsana New', 20, 'bold')
FONT2 = ('Angsana New', 15)

#กำหนด Tab
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1, text='ใบแจ้งซ่อม') #กำหนด Tab1 ชื่อใบแจ้งซ่อม
Tab.add(T2, text='ดูใบแจ้งซ่อม') #กำหนด Tab2 ชื่อดูใบแจ้งซ่อม
Tab.add(T3, text='สรุป') #กำหนด Tab2 ชื่อสรุป
Tab.pack(fill=BOTH, expand=1)


#กำหนด Label ให้กับ GUI
L = Label (T1 , text='ใบแจ้งซ่อม', font=FONT1)
L.place(x=80, y=10)

#กำหนด Field
#----- ชื่อผู้แจ้ง -------------------------------------------------
L = Label (T1 , text='ชื่อผู้แจ้ง', font=FONT2)
L.place(x=30, y=50)
v_name = StringVar() #กำหนดคลาส
E1 = ttk.Entry(T1,textvariable=v_name, font=FONT2) #เพิ่ม Field
E1.place(x=150, y=50)

#----- แผนก -------------------------------------------------
L = Label (T1 , text='แผนก', font=FONT2)
L.place(x=30, y=100)
v_department = StringVar() #กำหนดคลาส
E2 = ttk.Entry(T1,textvariable=v_department, font=FONT2) #เพิ่ม Field
E2.place(x=150, y=100)

#----- อุปกรณ์/ เครื่อง -------------------------------------------------
L = Label (T1 , text='อุปกรณ์/ เครื่อง', font=FONT2)
L.place(x=30, y=150)
v_machine = StringVar() #กำหนดคลาส
E3 = ttk.Entry(T1, textvariable=v_machine, font=FONT2) #เพิ่ม Field
E3.place(x=150, y=150)

#----- อาการเสีย -------------------------------------------------
L = Label (T1 , text='อาการเสีย', font=FONT2)
L.place(x=30, y=200)
v_problem = StringVar() #กำหนดคลาส
E4 = ttk.Entry(T1, textvariable=v_problem, font=FONT2) #เพิ่ม Field
E4.place(x=150, y=200)

#----- หมายเลข -------------------------------------------------
L = Label (T1 , text='หมายเลข', font=FONT2)
L.place(x=30, y=250)
v_number = StringVar() #กำหนดคลาส
E5 = ttk.Entry(T1, textvariable=v_number, font=FONT2) #เพิ่ม Field
E5.place(x=150, y=250)

#----- เบอร์โทร -------------------------------------------------
L = Label (T1 , text='เบอร์โทร', font=FONT2)
L.place(x=30, y=300)
v_tel = StringVar() #กำหนดคลาส
E6 = ttk.Entry(T1, textvariable=v_tel, font=FONT2) #เพิ่ม Field
E6.place(x=150, y=300)

#สร้างฟังก์ชั่นให้แสดงป๊อบอัพเมื่อกดบันทึก
def save():
    name = v_name.get() #.get คือการดึงค่าออกมาจาก StringVar()
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง : ' + name + '\n'
    text = text + 'แผนก : ' + department + '\n'
    text = text + 'อุปกรณ์/ เครื่อง : ' + machine + '\n'
    text = text + 'อาการเสีย : ' + problem + '\n'
    text = text + 'หมายเลข : ' + number + '\n'
    text = text + 'เบอร์โทร : ' + tel + '\n'


# กำหนด Datetime Format
    dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#Generate tsid
    tsid = str(int(datetime.now().strftime('%Y%m%d%H%M%S')) + 12345678987654)

#INSERT ข้อมูลเข้า DB
    insert_mtworkorder(tsid, name, department, machine, problem, number, tel)

# แสดงรายละเอียดหลังกดบันทึก
    messagebox.showinfo('บันทึกข้อมูลแล้ว', text)

#เครียร์ค่าหลังบันทึก และอัพเดทข้อมูลในหน้ารายงาน
    v_name.set('')
    v_department.set('')
    v_machine.set('')
    v_problem.set('')
    v_number.set('')
    v_tel.set('')
    update_table()

#Export ข้อมูบที่บันทึกเป็นไฟล์ CSV
#    writecsv(datalist)

#เมื่อบันทึกแล้ว ให้ส่งไลน์แจ้งข้อมูลที่บันทึก
"""    
    messenger.sendtext(['\n' + 'วันที่ : ' + dt + '\n' + 'ชื่อผู้แจ้ง : ' + name + '\n' + 'แผนก : ' + department + '\n' + 'อุปกรณ์/ เครื่อง : ' + machine + '\n' +
                        'อาการเสีย : ' + problem + '\n' + 'หมายเลข : ' + number + '\n' + 'เบอร์โทร : ' + tel + '\n'])
"""

#เพิ่มปุ่มบันทึก
B = ttk.Button(T1, text='บันทึก', command=save)
B.place(x=200, y=350)



############################### Tab 2 ############################### columns=header, show='headings', height=10
#สร้าง Tree View
header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']
headerw = [100,150,150,200,250,150,150]


#กำหนดการแสดงข้อมูล กำหนดคอลัมน์เป็น header, height เป็นการกำหนดว่าจะแสดงข้อมูลกี่ Row
mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=20)
mtworkorderlist.pack()

for h, w in zip(header, headerw):
    mtworkorderlist.heading(h, text=h)
    mtworkorderlist.column(h, width=w)


#เพิ่มข้อมูลในหน้ารายงาน
def update_table():
    mtworkorderlist.delete(*mtworkorderlist.get_children()) #ลบข้อมูลในตารางก่อนแสดงข้อมูลใหม่อีกที เพื่อป้องกันการแสดงข้อมูลซ้ำ
    data = view_mtworkorder()
#Print data
    for d in data:
        d = list(d) #Change data Tuple format to List format
        del d[0] #Delete ID form database before preview data in report
        mtworkorderlist.insert('', 'end', values=d)

#เมื่อเปิดโปรแกรมจะให้ฟังก์ชั่นอะไรทำงาน
update_table()

GUI.mainloop()