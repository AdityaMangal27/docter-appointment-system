import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Doctersystem import*
t=tkinter.Tk()
t.geometry('1500x1500')
t.configure(bg='peach puff')
t.title('login screen') 
#c1=Canvas(t,height=500,width=500,bg='skyblue')
#c1.place(x=800,y=100)
def login():
    x=b.get()
    y=int(bb.get())
    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
    cur=db.cursor()
    sql="select count(*) from users where userid='%s' and password=%d"%(x,y)
    cur.execute(sql)
    data=cur.fetchone()
    if data[0]==0:
        messagebox.showerror('Error','Login not found')
    else:
        messagebox.showinfo('Success','Login sucess')
        mainsc()
def showpassword():
    if bb.cget('show')=='*':
        bb.config(show='')
    else:
        bb.config(show='*')
        
def userinsert():
    c1=Canvas(t,height=300,width=500,bg='skyblue')
    c1.place(x=800,y=100)
    def savedata():
        if len(b.get())==0 or len(d.get())==0:
            messagebox.showerror('Error','please fill all data')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',db='das')
            cur=db.cursor()
            aa=b.get()
            bb=int(d.get())
            
            sql="insert into users values('%s',%d)"%(aa,bb)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Success','Saved')
            b.delete(0,100)
            d.delete(0,100)
           
    def checkdata():
        x=b.get()
        db=pymysql.connect(host='localhost',user='root',password='root',db='das')
        cur=db.cursor()
        sql="select count(*) from users where userid='%s'"%(x)
        cur.execute(sql)
        data=cur.fetchone()
        if data[0]==0:
            lt.config(text='Ok Pls go ahead',fg='green')
        else:
            lt.config(text='Sorry not available',fg='red')
        
    def showpass():
        if d.cget('show')=='*':
            d.config(show='')
        else:
            d.config(show='*')
            
    def close():
        c1.destroy()
        db.close()
        
    a=Label(c1,text="USER.ID:",font=('bold',10),bg='peachpuff')
    a.place(x=50,y=50)
    b=Entry(c1,width=10,show=None)
    b.pack()
    b.place(x=150,y=50)
    bt=Button(c1,text='CHECK',command=checkdata,font=('bold',10),bg='brown')
    bt.place(x=300,y=50)
    lt=Label(c1,text='Status',font=('bold',10),bg='yellow')
    lt.place(x=380,y=50)

    c=Label(c1,text="PASSWORD:",font=('bold',10),bg='peachpuff')
    c.place(x=50,y=100)
    d=Entry(c1,width=10,show='*')
    d.pack()
    d.place(x=150,y=100)
    bt1=Button(c1,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
    bt1.place(x=150,y=200)
    bt2=Button(c1,text='EXIT',command=close,font=10,bg='cyan')
    bt2.place(x=250,y=200)
    rm=Checkbutton(c1,text='Show password',bg='skyblue',command=showpass)
    rm.place(x=280,y=100)
    db.close()
a1=Label(t,text='DOCTER APPOINTMENT SYSTEM',font=15,bg='peach puff')
a1.place(x=300,y=20)
a=Label(t,text='User_id:',font='15',bg='peach puff')
a.place(x=50,y=100)
b=Entry(t,width=30,show=None)
b.pack()
b.place(x=200,y=100)
aa=Label(t,text='Password:',font='15',bg='peach puff')
aa.place(x=50,y=200)
bb=Entry(t,width=30,show='*')
bb.pack()
bb.place(x=200,y=200)
rm=Checkbutton(t,text='Show password',bg='peach puff',command=showpassword)
rm.place(x=400,y=200)
bt=Button(t,text='Login',command=login,font='15')
bt.place(x=300,y=300)
ba=Button(t,text='New User',font=15,command=userinsert)
ba.place(x=180,y=300)
t.mainloop()

