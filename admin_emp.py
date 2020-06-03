from tkinter import *
from tkinter.font import Font
import sqlite3 as db
conn = db.connect('gui5555.db')
cur = conn.cursor()
cur.execute(''' CREATE TABLE IF NOT EXISTS ADMIN(Auser_name TEXT,Apassword INTEGER,Amail TEXT)''')
cur.execute(''' CREATE TABLE IF NOT EXISTS EMP(Euser_name TEXT,Epassword INTEGER,Email TEXT)''')
cur.close()
conn.commit()
conn.close()

def put1():   
    conn = db.connect('gui5555.db')
    cur = conn.cursor()
    cur.execute("insert into ADMIN values('%s','%d','%s')"%( Auser_name.get(),Apassword.get(),Amail.get())) 
    cur.execute("insert into EMP values('%s','%d','%s')"%( Euser_name.get(),Epassword.get(),Email.get()))
    cur.close()
    conn.commit()
    conn.close()
    status.set('Data Adding sucessfully')
    Estatus.set('Data Adding sucessfully')

def page2():
    top=Toplevel()
    top.geometry('320x300')
    top['bg']='#800000'
    
    new2Font=Font(family='Times New Roman',size=16,weight='bold')
    Label(top,text='IF YOU ARE A EMPLOYE THEN',font=new2Font,bg='yellow').grid(row=1,column=2)
    Label(top,text='FILL UP HERE',font=new2Font,bg='orange').grid(row=5,column=2)
    Label(top,text='USER NAME',bg='YELLOW').grid(row=10,column=2)
    Entry(top,textvariable =Euser_name,bd=5).grid(row=12,column=2)
    Label(top,text='PASSWORD',bg='YELLOW').grid(row=15,column=2)
    Entry(top,textvariable =Epassword,bd=5).grid(row=17,column=2)
    Label(top,text='EMAIL',bg='YELLOW').grid(row=22,column=2)
    Entry(top,textvariable =Email,bd=5).grid(row=25,column=2)
    Label(top , text= ' ', textvariable=Estatus,font=new2Font).grid(row=34,column=2)
    Button(top,text="SUBMIT" ,command = put1).grid(row=32,column=2)
    Button(top,text="SKIP").grid(row=36,column=2)
      
to = Tk()
to.geometry('500x200')
to['bg']='orange'

#variables
Auser_name = StringVar()
Apassword =IntVar()
Amail =StringVar()
status = StringVar()
Euser_name = StringVar()
Epassword =IntVar()
Email = StringVar()
Estatus = StringVar()

def page1():
    newFont=Font(family='Times New Roman',size=16,weight='bold')
    Label(to, text='ADMIN MANAGEMENT PERPOSE:',font=newFont,bg='YELLOW').grid(row =2 , column=1)
    Label(to, text='user name:',font=newFont,bg='orange').grid(row =3 , column=1)
    Label(to , text='password:',font=newFont,bg='orange').grid(row =4 ,column =1)
    Label(to , text='email',font=newFont,bg='orange').grid(row =6 ,column =1)
    Label(to , text= ' ', textvariable=status,font=newFont).grid(row=9,columnspan=2)
#entry box
    Entry(to, textvariable =Auser_name,bd=8).grid(row=3,column=2)
    Entry(to, textvariable =Apassword,bd=8).grid(row=4,column=2)
    Entry(to, textvariable =Amail,bd=8).grid(row=6,column=2)
#Button
    Button(to,text="SUBMIT" ,command = put1).grid(row=8,columnspan=2)
    Button(to,text="SKIP" ,command = page2).grid(row=12,columnspan=2)
   
    
    
#label
newFont=Font(family='Times New Roman',size=16,weight='bold')
Label(to, text='EMPLOYE MANAGEMENT',font=newFont,bg='YELLOW').grid(row =2 , column=1)
Button(to,text="SKIP" ,command = page1).grid(row=12,columnspan=2)
mainloop()