#Yellow Book (Laboratory Register)
from tkinter import *
from cgitb import text
from dataclasses import fields
from textwrap import fill
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql
from tkinter import font
from turtle import width


win = tk.Tk()
win.geometry('1350x200')
win.title("Laboratory Register")

win.config(bg="black")

title_label1 = tk.Label(win, text = "Laboratory Register", font=("Arial",30,"bold"),border=12,relief=tk.GROOVE, bg ="yellow",foreground="black") 
title_label1.pack(side=tk.TOP,fill=tk.X)

detail_frame = tk.LabelFrame(win,text="Enter Lab Record", font=("Arial,25"), bg="black",foreground="yellow",relief=tk.GROOVE)
detail_frame.place(x=20,y=150,width=450,height=550)

data_frame = tk.Frame(win,bd=12,bg = "black", relief = tk.GROOVE)
data_frame.place(x=475,y=90,width=1050,height=680)

"""Variables"""

exp_no = tk.StringVar()
batch = tk.StringVar()
rollno = tk.StringVar()
dose = tk.StringVar()
docoe = tk.StringVar()
edoec = tk.StringVar()
doec = tk.StringVar()
marks = tk.StringVar()

search_by = tk.StringVar()

"""DONE"""

"""Entry"""

expno_lb1 = tk.Label(detail_frame,text="Exp No",font=("Arial",17), bg = "yellow",)
expno_lb1.grid(row=0,column=0,padx=2,pady=2)

expno_ent1 = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=exp_no)
expno_ent1.grid(row=0,column=1,padx=2,pady=2)


batch_lb2 = tk.Label(detail_frame,text="Batch",font=("Arial",17), bg = "yellow",)
batch_lb2.grid(row=1,column=0,padx=2,pady=2)

batch_ent2 = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=batch)
batch_ent2.grid(row=1,column=1,padx=2,pady=2)

rollno_lb1 = tk.Label(detail_frame,text="Roll No",font=("Arial",17), bg = "yellow",)
rollno_lb1.grid(row=2,column=0,padx=2,pady=2)

rollno_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=rollno)
rollno_ent.grid(row=2,column=1,padx=2,pady=2)

dose_lb1 = tk.Label(detail_frame,text="Date of Starting Exp",font=("Arial",17), bg = "yellow",)
dose_lb1.grid(row=3,column=0,padx=2,pady=2)

dose_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=dose)
dose_ent.grid(row=3,column=1,padx=2,pady=2)

doef_lb1 = tk.Label(detail_frame,text="Date of Completion of Exp",font=("Arial",17), bg = "yellow",)
doef_lb1.grid(row=4,column=0,padx=2,pady=2)

docoe_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=docoe)
docoe_ent.grid(row=4,column=1,padx=2,pady=2)

edoec_lb1 = tk.Label(detail_frame,text="Expected Date of Exp Checking",font=("Arial",17), bg = "yellow",)
edoec_lb1.grid(row=5,column=0,padx=2,pady=2)

edoec_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=edoec)
edoec_ent.grid(row=5,column=1,padx=2,pady=2)

doec_lb1 = tk.Label(detail_frame,text="Date of Exp Checked",font=("Arial",17), bg = "yellow",)
doec_lb1.grid(row=6,column=0,padx=2,pady=2)

doec_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=doec)
doec_ent.grid(row=6,column=1,padx=2,pady=2)

marks_lb1 = tk.Label(detail_frame,text="Marks",font=("Arial",17), bg = "yellow",)
marks_lb1.grid(row=7,column=0,padx=2,pady=2)

marks_ent = tk.Entry(detail_frame,bd=7,font=("Arial",17),textvariable=marks)
marks_ent.grid(row=7,column=1,padx=2,pady=2)

"""********"""

"""FUNCTIONS"""

def fetch_data():
    conn = pymysql.connect(host="Localhost",user="root",password="",database="labregister")
    curr = conn.cursor()
    curr.execute("SELECT * FROM lab_details")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert("",tk.END,values=row)
        conn.commit()
    conn.close()    

def add_function():
    if exp_no.get() == "" or batch.get() == "" or rollno.get() == "" or dose.get() == "" or docoe.get() == "" or edoec.get() == "" or doec.get() == ""or marks.get() == "":
        messagebox.showerror("Error!", "Please fill all the fields!")
    else:
        conn = pymysql.connect(host="Localhost",user="root",password="",database="labregister")
        curr = conn.cursor()
        curr.execute("INSERT INTO lab_details VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",(exp_no.get(),batch.get(),rollno.get(),dose.get(),docoe.get(),edoec.get(),doec.get(),marks.get()))
        conn.commit() 
        conn.close()  

        fetch_data()

def get_cursor(event):
    """This function will fetch data of the selected row"""
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content['values']

    exp_no.set(row[0])
    batch.set(row[1])
    rollno.set(row[2])
    dose.set(row[3])
    docoe.set(row[4])
    edoec.set(row[5])
    doec.set(row[6])
    marks.set(row[7])

def clear():
    """This is function which will clear the entry boxes"""
    exp_no.set("")
    batch.set("")
    rollno.set("")
    dose.set("")
    docoe.set("")
    edoec.set("")
    doec.set("")
    marks.set("")

def update_fun():
    """This function will update data according to user"""
    conn = pymysql.connect(host="Localhost",user="root",password="",database="labregister")
    curr = conn.cursor()
    curr.execute("update lab_details set exp_no=%s,batch=%s,dose=%s,docoe=%s,edoec=%s,doec=%s,marks=%s where rollno=%s",(exp_no.get(),batch.get(),dose.get(),docoe.get(),edoec.get(),doec.get(),marks.get(),rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()

def delete_fun():
    "This function will delete data from database"
    conn = pymysql.connect(host="Localhost",user="root",password="",database="labregister")
    curr = conn.cursor()  
    curr.execute("delete from lab_details where rollno=%s",rollno.get())
    conn.commit()
    conn.close()
    fetch_data()
    clear()

"""DONE"""

"""BUTTON"""

btn_frame = tk.Frame(detail_frame,bg="yellow",bd="10",relief=tk.GROOVE)
btn_frame.place(x=50,y=400,width=370,height=110)

add_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Add",bd=7,font=("Arial",12),width=17,command=add_function)
add_btn.grid(row=0,column=0,padx=2,pady=2)

update_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Update",bd=7,font=("Arial",12),width=16,command=update_fun)
update_btn.grid(row=0,column=1,padx=2,pady=2)

delete_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Delete",bd=7,font=("Arial",11),width=17,command=delete_fun)
delete_btn.grid(row=1,column=0,padx=2,pady=2)

clear_btn = tk.Button(btn_frame,bg="black",fg="yellow",text="Clear",bd=7,font=("Arial",11),width=16,command=clear)
clear_btn.grid(row=1,column=1,padx=2,pady=2)

"""DONE BUTTON"""



"""SEARCH"""

search_frame = tk.Frame(data_frame,bg="black",bd=10,relief=tk.GROOVE)
search_frame.pack(side=tk.TOP,fill=tk.X)

search_lb1 = tk.Label(search_frame,text="Search",fg="yellow",bg="black",font=("Arial",14))
search_lb1.grid(row=0, column=0, padx=12, pady=2)

search_in = ttk.Combobox(search_frame,font=('Arial,14'),state="readonly",textvariable=search_by)
search_in['values'] = ("Name","Roll No","Batch","Exp No")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn = tk.Button(search_frame, text="Search",font=("Arial",13),bd=9,width=14,bg="black",fg="yellow")
search_btn.grid(row=0,column=2,padx=12,pady=2)

search_btn = tk.Button(search_frame, text="Show All",font=("Arial",13),bd=9,width=14,bg="black",fg="yellow")
search_btn.grid(row=0,column=3,padx=12,pady=2)

"""Search Done"""

main_frame = tk.Frame(data_frame,bg="lightgrey",bd=3,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

"""Exp No, Batch, Roll No, Date of Starting Exp, Date of Completion of Exp, Expected Date of Exp Checking, Date of Exp Checked, Marks"""

student_table = ttk.Treeview(main_frame,columns=("Exp No","Batch","Roll No", "Date of Starting Exp", "Date of Completion of Exp", "Expected Date of Exp Checking", "Date of Exp Checked", "Marks"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.pack(fill=tk.BOTH,expand=True)

"""Exp No, Batch, Roll No, Date of Starting Exp, Date of Completion of Exp, Expected Date of Exp Checking, Date of Exp Checked, Marks"""

student_table.heading("Exp No", text="Exp No")
student_table.heading("Batch", text="Batch")
student_table.heading("Roll No", text="Roll No")
student_table.heading("Date of Starting Exp", text="Date of Starting Exp")
student_table.heading("Date of Completion of Exp", text="Date of Completion of Exp")
student_table.heading("Expected Date of Exp Checking", text="Expected Date of Exp Checking")
student_table.heading("Date of Exp Checked", text="Date of Exp Checked")
student_table.heading("Marks", text="Marks")

student_table['show'] = 'headings'



student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)

win.mainloop()
