import tkinter
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def mainsc():
    t=tkinter.Tk()
    t.geometry('1800x1800')
    t.title('DOCTER APPOINTMENT SYSTEM')
    c1=Canvas(t,height=1000,width=1000,bg='orange')
    c1.place(x=0,y=10)
    c2=Canvas(t,height=800,width=400,bg='white')
    c2.place(x=185,y=10)
    c3=Canvas(t,height=1100,width=1100,bg='green')
    c3.place(x=350,y=10)
    c4=Canvas(t,height=800,width=50,bg='blue')
    c4.place(x=1455,y=10)
    def showclinicdatabutton():
        def clinicfind():
            c3=Canvas(t,height=800,width=650,bg='orange')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select ClinicID from clinicdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,Phone_no,Email_id,RegNo from clinicdata where ClinicID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,data[3])
                n.insert(0,data[4])
                r.insert(0,data[5])
                db.close()
            def close():
                c3.destroy()
            a=Label(c3,text="CLINIC.ID",font=('bold',10),bg='orange')
            a.place(x=50,y=50)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=400,y=50)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=150,y=50)
            c=Label(c3,text="NAME",font=('bold',10),bg='orange')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='orange')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=150,y=150)
            g=Label(c3,text="CITY",font=('bold',10),bg='orange')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=150,y=200)
            j=Label(c3,text='PHONE_NO',font=('bold',10),bg='orange')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='EMAIL',bg='orange')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='REG_NO',font=('bold',10),bg='orange')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=200,y=450)
        def clinicupdate():
            c3=Canvas(t,height=800,width=650,bg='aqua')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select ClinicID from clinicdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,Phone_no,Email_id,RegNo from clinicdata where ClinicID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
    
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,str(data[2]))
                k.insert(0,data[3])
                n.insert(0,str(data[4]))
                r.insert(0,data[5])
                db.close()
            def updatedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                bb=d.get()
                cc=f.get()
                dd=h.get()
                ee=k.get()
                ff=n.get()
                gg=int(r.get())
                
                
                sql="update clinicdata set Name='%s',Address='%s',City='%s',Phone_no='%s',Email_id='%s',RegNo=%d where Institute_id=%d"%(bb,cc,dd,ee,ff,gg,aa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Data Saved')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
            def close():
                c3.destroy()
               
                db.close()
            t.title('CLINIC DATA')
            a=Label(c3,text="CLINIC.ID",font=('bold',10),bg='aqua')
            a.place(x=50,y=50)
            a1=Button(c3,text='FIND',font=('bold',10),command=finddata)
            a1.place(x=300,y=50)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=150,y=50)
            c=Label(c3,text="NAME",font=('bold',10),bg='aqua')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='aqua')
            e.place(x=50,y=150)
            f=Entry(c3,width=20)
            f.place(x=150,y=150)
            g=Label(c3,text="CITY",font=('bold',10),bg='aqua')
            g.place(x=50,y=200)
            h=Entry(c3,width=20)
            h.place(x=150,y=200)
            j=Label(c3,text='PHONE_NO',font=('bold',10),bg='aqua')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='EMAIL',font=('bold',10),bg='aqua')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='REG_NO',font=('bold',10),bg='aqua')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            bt1=Button(c3,text='UPDATE',font=('bold',10),command=updatedata)
            bt1.place(x=200,y=400)
            bt=Button(c3,text='CLOSE',font=('bold',10),command=close)
            bt.place(x=300,y=400)
        def clinicdelete():
            c3=Canvas(t,height=800,width=650,bg='cyan')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select ClinicID from clinicdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                    
            def deletedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                sql="delete from clinicdata where ClinicID=%d"%(aa)
                cur.execute(sql)
                db.commit()
                db.close()
                b.delete(0,100)
                messagebox.showinfo('Hi','Data delete')
            def close():
                c3.destroy()
                
                
            a=Label(c3,text="CLINIC.ID",font=('bold',10),bg='olive')
            a.place(x=50,y=50)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=150,y=50)
            c=Button(c3,text='DELETE',command=deletedata,font=('bold',10),bg='cyan')
            c.place(x=150,y=200)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=200)
        def clinicinsert():
            c3=Canvas(t,height=800,width=650,bg='yellow')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=d.get()
                    cc=f.get()
                    dd=h.get()
                    ee=k.get()
                    ff=n.get()
                    gg=int(r.get())
                    sql="insert into clinicdata values(%d,'%s','%s','%s','%s','%s',%d)"%(aa,bb,cc,dd,ee,ff,gg)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    n.delete(0,100)
                    r.delete(0,100)
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from clinicdata where ClinicID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
            def exit():
                c3.destroy()
    
            a=Label(c3,text="CLINIC.ID",font=('bold',10),bg='yellow')
            a.place(x=50,y=50)
            b=Entry(c3,width=30)
            b.place(x=150,y=50)
            bt=Button(c3,text='CHECK',command=checkdata,font=('bold',10),bg='brown')
            bt.place(x=400,y=50)
            lt=Label(c3,text='Status',font=('bold',10),bg='yellow')
            lt.place(x=500,y=50)
    
            c=Label(c3,text="NAME",font=('bold',10),bg='yellow')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='yellow')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=150,y=150)
            g=Label(c3,text="CITY",font=('bold',10),bg='yellow')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=150,y=200)
            j=Label(c3,text='PHONE_NO',font=('bold',10),bg='yellow')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='EMAIL',font=('bold',10),bg='yellow')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='REG_NO',font=('bold',10),bg='yellow')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
            bt2=Button(c3,text='EXIT',command=exit,font=('bold',15),bg='cyan')
            bt2.place(x=300,y=450)
        def clinicshowall():
            c3=Canvas(t,height=800,width=650,bg='bisque')
            c3.place(x=350,y=10)
            at=[]
            bt=[]
            ct=[]
            dt=[]
            et=[]
            ft=[]
            gt=[]
            i=0
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select * from clinicdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    at.append(res[0])
                    bt.append(res[1])
                    ct.append(res[2])
                    dt.append(res[3])
                    et.append(res[4])
                    ft.append(res[5])
                    gt.append(res[6])
                    
                db.close()
    
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
               
    
            def showprevious():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
            def showlast():
                global i
                i=len(at)-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
            def exit():
                c3.destroy()
            a=Label(c3,text='DOCTER.ID',bg='bisque')
            a.place(x=50,y=50)
            b=Entry(c3,width=30)
            b.place(x=150,y=50 )
            c=Label(c3,text='Name',bg='bisque')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text='ADDRESS',bg='bisque')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=150,y=150)
            g=Label(c3,text='CITY',bg='bisque')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=150,y=200)
            j=Label(c3,text='PHONE_NO',bg='bisque',font=('bold',10))
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='EMAIL',bg='bisque',font=('bold',10))
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='REG_NO',bg='bisque',font=('bold',10))
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            b1=Button(c3,text='First',command=showfirst)
            b1.place(x=50,y=420)
            b2=Button(c3,text='Next',command=shownext)
            b2.place(x=150,y=420)
            b3=Button(c3,text='Last',command=showlast)
            b3.place(x=250,y=420)
            b4=Button(c3,text='Previous',command=showprevious)
            b4.place(x=350,y=420)
            b5=Button(c3,text='EXIT',font=('bold',15),fg='cyan',command=exit)
            b5.place(x=200,y=500)
            filldata()
            showfirst()
    
        at=Label(c3,text='CLINIC OPERATIONS',font=('arial',30))
        at.place(x=50,y=10)
        ba=Button(c2,text='Insert',fg='black',bg='gray70',font=('arial',15),command=clinicinsert)
        ba.place(x=50,y=150)
        bb=Button(c2,text='Delete',fg='black',bg='gray70',font=('arial',15),command=clinicdelete)
        bb.place(x=50,y=250)    
        bc=Button(c2,text='Update',fg='black',bg='gray70',font=('arial',15),command=clinicupdate)
        bc.place(x=50,y=350)    
        bd=Button(c2,text='Find',fg='black',bg='gray70',font=('arial',15),command=clinicfind)
        bd.place(x=50,y=450)    
        be=Button(c2,text='ShowAll',fg='black',bg='gray70',font=('arial',15),command=clinicshowall)
        be.place(x=50,y=550)  
        
    def showdoctersdatabutton():
        def docterfind():
            c3=Canvas(t,height=800,width=650,bg='orange')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select DocID from docdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,PhoneNumber,EmailAddress,Specialization from docdata where DocID=%d"%aa
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,data[3])
                n.insert(0,data[4])
                r.insert(0,data[5])
                db.close()
            def close():
                c3.destroy()
            a=Label(c3,text="DOCTER.ID",font=('bold',10),bg='orange')
            a.place(x=50,y=50)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=400,y=50)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=150,y=50)
            c=Label(c3,text="DOCTER_NAME",font=('bold',10),bg='orange')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='orange')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=150,y=150)
            g=Label(c3,text="CITY",font=('bold',10),bg='orange')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=150,y=200)
            j=Label(c3,text='EMAIL',font=('bold',10),bg='orange')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='PHONE_NO',bg='orange')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='SPECIALITY',font=('bold',10),bg='orange')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=200,y=450)
        def docterupdate():
            c3=Canvas(t,height=800,width=650,bg='aqua')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select DocID from docdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,PhoneNumber,EmailAddress,Specialization from docdata where DocID=%d"%aa
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
    
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,data[3])
                n.insert(0,data[4])
                r.insert(0,data[5])
                db.close()
            def updatedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                bb=d.get()
                cc=f.get()
                dd=h.get()
                ee=k.get()
                ff=n.get()
                gg=r.get()
                
                
                sql="update docdata set Name='%s',Address='%s',City='%s',PhoneNumber='%s',EmailAddress='%s',Specialization='%s' where DocID=%d"%(bb,cc,dd,ee,ff,gg,aa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Data Saved')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
            def close():
                c3.destroy()
               
                db.close()
            t.title('DOCTER DATA')
            a=Label(c3,text="DOCTER.ID",font=('bold',10),bg='aqua')
            a.place(x=50,y=50)
            a1=Button(c3,text='FIND',font=('bold',10),command=finddata)
            a1.place(x=300,y=50)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=150,y=50)
            c=Label(c3,text="DOCTER_NAME",font=('bold',10),bg='aqua')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text="ADDRESS",font=('bold',10))
            e.place(x=50,y=150)
            f=Entry(c3,width=20)
            f.place(x=150,y=150)
            g=Label(c3,text="City",font=('bold',10),bg='aqua')
            g.place(x=50,y=200)
            h=Entry(c3,width=20)
            h.place(x=150,y=200)
            j=Label(c3,text='Phone No.',font=('bold',10),bg='aqua')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='Email',font=('bold',10),bg='aqua')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='Specialization',font=('bold',10),bg='aqua')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            bt1=Button(c3,text='UPDATE',font=('bold',10),command=updatedata)
            bt1.place(x=200,y=400)
            bt=Button(c3,text='CLOSE',font=('bold',10),command=close)
            bt.place(x=300,y=400)
        def docterdelete():
            c3=Canvas(t,height=800,width=650,bg='olive')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select DocID from docdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                    
            def deletedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                sql="delete from docdata where DocID=%d"%(aa)
                cur.execute(sql)
                db.commit()
                db.close()
                b.delete(0,100)
                messagebox.showinfo('Hi','Data delete')
            def close():
                c3.destroy()
                
                
            a=Label(c3,text="DOCTER.ID",font=('bold',10),bg='olive')
            a.place(x=50,y=50)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=150,y=50)
            c=Button(c3,text='DELETE',command=deletedata,font=('bold',10),bg='cyan')
            c.place(x=150,y=200)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=200)
        def docterinsert():
            c3=Canvas(t,height=800,width=650,bg='yellow')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=d.get()
                    cc=f.get()
                    dd=h.get()
                    ee=k.get()
                    ff=n.get()
                    gg=r.get()
                    sql="insert into docdata values(%d,'%s','%s','%s','%s','%s','%s')"%(aa,bb,cc,dd,ee,ff,gg)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    n.delete(0,100)
                    r.delete(0,100)
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from docdata where DocID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
            def exit():
                c3.destroy()
    
            a=Label(c3,text="Doc.ID",font=('bold',10),bg='yellow')
            a.place(x=50,y=50)
            b=Entry(c3,width=30)
            b.place(x=150,y=50)
            bt=Button(c3,text='CHECK',command=checkdata,font=('bold',10),bg='brown')
            bt.place(x=400,y=50)
            lt=Label(c3,text='Status',font=('bold',10),bg='yellow')
            lt.place(x=500,y=50)
    
            c=Label(c3,text="NAME",font=('bold',10),bg='yellow')
            c.place(x=50,y=100)
            d=Entry(c3,width=20)
            d.place(x=150,y=100)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='yellow')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=150,y=150)
            g=Label(c3,text="CITY",font=('bold',10),bg='yellow')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=150,y=200)
            j=Label(c3,text='Phone No.',font=('bold',10),bg='yellow')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='Email',font=('bold',10),bg='yellow')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='Specialization',font=('bold',10),bg='yellow')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
            bt2=Button(c3,text='EXIT',command=exit,font=('bold',15),bg='cyan')
            bt2.place(x=300,y=450)
        def doctershowall():
            c3=Canvas(t,height=800,width=650,bg='bisque')
            c3.place(x=350,y=10)
            at=[]
            bt=[]
            ct=[]
            dt=[]
            et=[]
            ft=[]
            gt=[]
            i=0
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select * from docdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    at.append(res[0])
                    bt.append(res[1])
                    ct.append(res[2])
                    dt.append(res[3])
                    et.append(res[4])
                    ft.append(res[5])
                    gt.append(res[6])
                    
                db.close()
    
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
               
    
            def showprevious():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
            def showlast():
                global i
                i=len(at)-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
            def exit():
                c3.destroy()
            a=Label(c3,text='DOCTER.ID',bg='bisque')
            a.place(x=50,y=50)
            b=Entry(c3,width=20)
            b.place(x=170,y=50 )
            c=Label(c3,text='Name',bg='bisque')
            c.place(x=50,y=100)
            d=Entry(c3,width=30)
            d.place(x=170,y=100)
            e=Label(c3,text='ADDRESS',bg='bisque')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=170,y=150)
            g=Label(c3,text='CITY',bg='bisque')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=170,y=200)
            j=Label(c3,text='PHONE NO',bg='bisque',font=('bold',10))
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=170,y=250)
            m=Label(c3,text='EMAIL',bg='bisque',font=('bold',10))
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=170,y=300)
            p=Label(c3,text='SPECIALIZATION',bg='bisque',font=('bold',10))
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=170,y=350)
            b1=Button(c3,text='First',command=showfirst)
            b1.place(x=50,y=420)
            b2=Button(c3,text='Next',command=shownext)
            b2.place(x=150,y=420)
            b3=Button(c3,text='Last',command=showlast)
            b3.place(x=250,y=420)
            b4=Button(c3,text='Previous',command=showprevious)
            b4.place(x=350,y=420)
            b5=Button(c3,text='EXIT',font=('bold',15),fg='cyan',command=exit)
            b5.place(x=200,y=500)
            filldata()
            showfirst()
        
        at=Label(c3,text='DOCTER OPERATIONS',font=('arial',30))
        at.place(x=50,y=10)
        ba=Button(c2,text='Insert',fg='white',bg='brown',font=('arial',15),command=docterinsert)
        ba.place(x=50,y=150)
        bb=Button(c2,text='Delete',fg='white',bg='brown',font=('arial',15),command=docterdelete)
        bb.place(x=50,y=250)    
        bc=Button(c2,text='Update',fg='white',bg='brown',font=('arial',15),command=docterupdate)
        bc.place(x=50,y=350)    
        bd=Button(c2,text='Find',fg='white',bg='brown',font=('arial',15),command=docterfind)
        bd.place(x=50,y=450)    
        be=Button(c2,text='ShowAll',fg='white',bg='brown',font=('arial',15),command=doctershowall)
        be.place(x=50,y=550)
        
    def showpatientbutton():
        def patientfind():
            c3=Canvas(t,height=800,width=800,bg='cornsilk')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select PatientID from patientdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,Phoneno,Emailid from patientdata where PatientID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,data[3])
                n.insert(0,data[4])
                
                db.close()
            def close():
                c3.destroy()
            a=Label(c3,text="PATIENT.ID",bg='cornsilk',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=550,y=100)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=310,y=100)
            c=Label(c3,text="PATIENT_NAME",bg='cornsilk',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="ADDRESS",bg='cornsilk',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="CITY",bg='cornsilk',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='PHONE NO.',bg='cornsilk',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=30)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',bg='cornsilk',font=('bold',10))
            m.place(x=180,y=350)
            n=Entry(c3,width=30)
            n.place(x=310,y=350)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=450)
        def patientupdate():
            c3=Canvas(t,height=800,width=800,bg='darkkhaki')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select PatientID from patientdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,Phoneno,Emailid from patientdata where PatientID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
    
                d.insert(0,str(data[0]))
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,str(data[3]))
                n.insert(0,data[4])
                
                db.close()
            def updatedata():
                c3=Canvas(t,height=800,width=800,bg='orange')
                c3.place(x=150,y=10)
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                bb=d.get()
                cc=f.get()
                dd=h.get()
                ee=k.get()
                ff=n.get()
                
                
                
                sql="update patientdata set Name='%s',Address='%s',City='%s',Phoneno=%d,Emailid='%s' where PatientID=%d"%(bb,cc,dd,ee,ff,aa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Data Saved')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
            def close():
                c3.destroy()
               
                db.close()
            t.title('PATIENT DATA')
    
            a=Label(c3,text="PATIENT.ID",font=('bold',10),bg='darkkhaki')
            a.place(x=180,y=100)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=550,y=100)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=300,y=100)
            c=Label(c3,text="PATIENT_NAME",font=('bold',10),bg='darkkhaki')
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='darkkhaki')
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="CITY",font=('bold',10),bg='darkkhaki')
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='PHONE_NO',font=('bold',10),bg='darkkhaki')
            j.place(x=180,y=300)
            k=Entry(c3,width=30)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',bg='darkkhaki')
            m.place(x=180,y=350)
            n=Entry(c3,width=30)
            n.place(x=310,y=350)
            bt1=Button(c3,text='UPDATE',font=('bold',10),bg='cyan',command=updatedata)
            bt1.place(x=400,y=450)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=450)
        def patientdelete():
            c3=Canvas(t,height=800,width=800,bg='crimson')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select PatientID from patientdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                    
            def deletedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                sql="delete from patientdata where PatientID=%d"%(aa)
                cur.execute(sql)
                db.commit()
                db.close()
                b.delete(0,100)
                messagebox.showinfo('Hi','Data delete')
            def close():
                c3.destroy()
                
                
            a=Label(c3,text="PATIENT.ID",font=('bold',10),bg='crimson')
            a.place(x=200,y=100)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=300,y=100)
            c=Button(c3,text='DELETE',command=deletedata,font=('bold',15),bg='cyan')
            c.place(x=250,y=200)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=350,y=200)
        def patientinsert():
            c3=Canvas(t,height=800,width=800,bg='darkgoldenrod')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=d.get()
                    cc=f.get()
                    dd=h.get()
                    ee=int(k.get())
                    ff=n.get()
                    
                    sql="insert into patientdata values(%d,'%s','%s','%s',%d,'%s')"%(aa,bb,cc,dd,ee,ff)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    n.delete(0,100)
                    
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from patientdata where PatientID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
                
            def close():
                c3.destroy()
    
    
            a=Label(c3,text="PATIENT.ID",bg='darkgoldenrod',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='CHECK',bg='darkgoldenrod',command=checkdata,font=('bold',10))
            a1.place(x=550,y=100)
            lt=Label(c3,text='Status',bg='darkgoldenrod',font=('bold',10))
            lt.place(x=620,y=100)
    
            b=Entry(c3,width=30)
            b.place(x=310,y=100)
            c=Label(c3,text="PATIENT_NAME",bg='darkgoldenrod',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="ADDRESS",bg='darkgoldenrod',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="CITY",bg='darkgoldenrod',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='PHONE_NO',bg='darkgoldenrod',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=30)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',bg='darkgoldenrod',font=('bold',10))
            m.place(x=180,y=350)
            n=Entry(c3,width=30)
            n.place(x=310,y=350)
    
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
        def patientshowall():
            c3=Canvas(t,height=800,width=800,bg='darkorange')
            c3.place(x=350,y=10)
            at=[]
            bt=[]
            ct=[]
            dt=[]
            et=[]
            ft=[]
    
            i=0
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select * from Patientdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    at.append(res[0])
                    bt.append(res[1])
                    ct.append(res[2])
                    dt.append(res[3])
                    et.append(res[4])
                    ft.append(res[5])
                    
                    
                db.close()
    
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,str(et[i]))
                n.insert(0,ft[i])
                
    
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,str(et[i]))
                n.insert(0,ft[i])
                
    
               
    
            def showprevious():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,str(et[i]))
                n.insert(0,ft[i])
                
    
            def showlast():
                global i
                i=len(at)-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
               
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,str(et[i]))
                n.insert(0,ft[i])
            def close():
                c3.destroy()
                
    
            a=Label(c3,text="PATIENT.ID",font=('bold',10),bg='darkorange')
            a.place(x=180,y=100)
            b=Entry(c3,width=30)
            b.place(x=310,y=100)
            c=Label(c3,text="PATIENT_NAME",font=('bold',10),bg='darkorange')
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="ADDRESS",font=('bold',10),bg='darkorange')
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="CITY",font=('bold',10),bg='darkorange')
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='PHONE_NO',font=('bold',10),bg='darkorange')
            j.place(x=180,y=300)
            k=Entry(c3,width=30)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',font=('bold',10),bg='darkorange')
            m.place(x=180,y=350)
            n=Entry(c3,width=30)
            n.place(x=310,y=350)
            b1=Button(c3,text='First',font=('bold',15),bg='cyan',command=showfirst)
            b1.place(x=200,y=500)
            b2=Button(c3,text='Next',font=('bold',15),bg='cyan',command=shownext)
            b2.place(x=300,y=500)
            b3=Button(c3,text='Last',font=('bold',15),bg='cyan',command=showlast)
            b3.place(x=400,y=500)
            b4=Button(c3,text='Previous',font=('bold',15),bg='cyan',command=showprevious)
            b4.place(x=500,y=500)
            b5=Button(c3,text='Back',font=('bold',15),bg='cyan',command=close)
            b5.place(x=350,y=600)
            filldata()
            showfirst()
    
        at=Label(c3,text='PATIENT OPERATIONS',font=('arial',30))
        at.place(x=50,y=10)
        ba=Button(c2,text='Insert',fg='white',bg='crimson',font=('arial',15),command=patientinsert)
        ba.place(x=50,y=150)
        bb=Button(c2,text='Delete',fg='white',bg='crimson',font=('arial',15),command=patientdelete)
        bb.place(x=50,y=250)    
        bc=Button(c2,text='Update',fg='white',bg='crimson',font=('arial',15),command=patientupdate)
        bc.place(x=50,y=350)    
        bd=Button(c2,text='Find',fg='white',bg='crimson',font=('arial',15),command=patientfind)
        bd.place(x=50,y=450)    
        be=Button(c2,text='ShowAll',fg='white',bg='crimson',font=('arial',15),command=patientshowall)
        be.place(x=50,y=550)
        
    def showstaffbutton():
        def stafffind():
            c3=Canvas(t,height=800,width=800,bg='darksalmon')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select StaffID from staffdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,Phoneno,Emailid from staffdata where StaffID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,str(data[3]))
                n.insert(0,data[4])
                
                
                db.close()
            def close():
                c3.destroy()
            a=Label(c3,text="Staff_id",bg='darksalmon',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=550,y=100)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=310,y=100)
            c=Label(c3,text="NAME",bg='darksalmon',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="ADDRESS",bg='darksalmon',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="CITY",bg='darksalmon',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='PHONE',bg='darksalmon',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=50)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',bg='darksalmon',font=('bold',10))
            m.place(x=180,y=350)
            n=Entry(c3,width=20)
            n.place(x=310,y=350)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=450)
        def staffinsert():
            c3=Canvas(t,height=800,width=800,bg='darkseagreen')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=d.get()
                    cc=f.get()
                    dd=h.get()
                    ee=k.get()
                    ff=n.get()
                    
                    sql="insert into staffdata values(%d,'%s','%s','%s','%s','%s')"%(aa,bb,cc,dd,ee,ff)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    n.delete(0,100)
                    
                    
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from staffdata where StaffID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
                
            def close():
                c3.destroy()
            a=Label(c3,text="Staff_id",bg='darkseagreen',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='CHECK',command=checkdata,font=('bold',10))
            a1.place(x=550,y=100)
            b=Entry(c3,width=30)
            b.place(x=310,y=100)
            lt=Label(c3,text='Status',bg='darkseagreen',font=('bold',10))
            lt.place(x=620,y=100)
            c=Label(c3,text="name",bg='darkseagreen',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="address",bg='darkseagreen',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="city",bg='darkseagreen',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='phone_no',bg='darkseagreen',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=10)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',bg='darksalmon',font=('bold',10))
            m.place(x=180,y=350)
            n=Entry(c3,width=20)
            n.place(x=310,y=350)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
        def staffdelete():
            c3=Canvas(t,height=800,width=800,bg='floralwhite')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select StaffID from staffdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                    
            def deletedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                sql="delete from staffdata where StaffID=%d"%(aa)
                cur.execute(sql)
                db.commit()
                db.close()
                b.delete(0,100)
                messagebox.showinfo('Hi','Data delete')
            def close():
                c3.destroy()
                            
            a=Label(c3,text="STAFF.ID:",font=('bold',15),bg='floralwhite')
            a.place(x=200,y=100)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=345,y=105)
            c=Button(c3,text='DELETE',command=deletedata,font=('bold',15),bg='cyan')
            c.place(x=250,y=200)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=350,y=200)
        
        def staffupdate():
            c3=Canvas(t,height=800,width=800,bg='deepskyblue')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select StaffID from staffdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select Name,Address,City,Phoneno,Emailid from staffdata where StaffID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                
    
                d.insert(0,str(data[0]))
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,str(data[3]))
                n.insert(0,data[4])
                
                db.close()
            def updatedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                bb=d.get()
                cc=f.get()
                dd=h.get()
                ee=k.get()
                ff=n.get()
                
                
                
                
                sql="update staffdata set Name='%s',Address='%s',City='%s',Phoneno='%s',Emailid='%s'"%(bb,cc,dd,ee,ff,aa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Data Saved')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
            def close():
                c3.destroy()
               
                db.close()
            t.title('STAFF INFO')
            a=Label(c3,text="Staff_id",bg='deepskyblue',font=('bold',15))
            a.place(x=180,y=100)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',15))
            a1.place(x=550,y=90)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=310,y=100)
            c=Label(c3,text="name",bg='deepskyblue',font=('bold',15))
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=150)
            e=Label(c3,text="address",bg='deepskyblue',font=('bold',15))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="city",bg='deepskyblue',font=('bold',15))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='phone_no',bg='deepskyblue',font=('bold',15))
            j.place(x=180,y=300)
            k=Entry(c3,width=35)
            k.place(x=310,y=300)
            m=Label(c3,text='EMAIL',bg='darksalmon',font=('bold',10))
            m.place(x=180,y=350)
            n=Entry(c3,width=20)
            n.place(x=310,y=350)
            bt1=Button(c3,text='UPDATE',font=('bold',15),bg='cyan',command=updatedata)
            bt1.place(x=400,y=450)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
        def staffshowall():
            c3=Canvas(t,height=800,width=800,bg='gold')
            c3.place(x=350,y=10)
            at=[]
            bt=[]
            ct=[]
            dt=[]
            et=[]
            ft=[]
    
            i=0
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select * from staffdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    at.append(res[0])
                    bt.append(res[1])
                    ct.append(res[2])
                    dt.append(res[3])
                    et.append(res[4])
                    ft.append(res[5])
                    
                    
                db.close()
    
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                
    
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                
    
               
    
            def showprevious():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                
    
            def showlast():
                global i
                i=len(at)-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
               
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
            def close():
                c3.destroy()
                
            a=Label(c3,text="Staff_id",bg='gold',font=('bold',15))
            a.place(x=180,y=100)
            b=Entry(c3,width=30)
            b.place(x=310,y=110)
            c=Label(c3,text="name",bg='gold',font=('bold',15))
            c.place(x=180,y=150)
            d=Entry(c3,width=20)
            d.place(x=310,y=160)
            e=Label(c3,text="address",bg='gold',font=('bold',15))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=210)
            g=Label(c3,text="city",bg='gold',font=('bold',15))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=260)
            j=Label(c3,text='phone_no',bg='gold',font=('bold',15))
            j.place(x=180,y=300)
            k=Entry(c3,width=50)
            k.place(x=310,y=310)
            m=Label(c3,text='EMAIL',bg='gold',font=('bold',15))
            m.place(x=180,y=350)
            n=Entry(c3,width=20)
            n.place(x=310,y=350)
            b1=Button(c3,text='First',font=('bold',15),bg='cyan',command=showfirst)
            b1.place(x=200,y=400)
            b2=Button(c3,text='Next',font=('bold',15),bg='cyan',command=shownext)
            b2.place(x=300,y=400)
            b3=Button(c3,text='Last',font=('bold',15),bg='cyan',command=showlast)
            b3.place(x=400,y=400)
            b4=Button(c3,text='Previous',font=('bold',15),bg='cyan',command=showprevious)
            b4.place(x=500,y=400)
    
            b5=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            b5.place(x=350,y=470)
            filldata()
            showfirst()
      
        at=Label(c3,text='STAFF OPERATIONS',font=('arial',30))
        at.place(x=50,y=10)
        ba=Button(c2,text='Insert',fg='blue',bg='white',font=('arial',15),command=staffinsert)
        ba.place(x=50,y=150)
        bb=Button(c2,text='Delete',fg='blue',bg='white',font=('arial',15),command=staffdelete)
        bb.place(x=50,y=250)    
        bc=Button(c2,text='Update',fg='blue',bg='white',font=('arial',15),command=staffupdate)
        bc.place(x=50,y=350)    
        bd=Button(c2,text='Find',fg='blue',bg='white',font=('arial',15),command=stafffind)
        bd.place(x=50,y=450)    
        be=Button(c2,text='ShowAll',fg='blue',bg='white',font=('arial',15),command=staffshowall)
        be.place(x=50,y=550)
        
    def showappointmentbutton():
        def appointmentfind():
            c3=Canvas(t,height=800,width=650,bg='azure')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select AppID from appointmentdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select PatID,DocID,DateofAppointment,TimeVisit,Disease,Remarks from appointmentdata where AppID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                d.insert(0,str(data[0]))
                f.insert(0,str(data[1]))
                h.insert(0,data[2])
                k.insert(0,data[3])
                n.insert(0,data[4])
                r.insert(0,data[5])
                db.close()
            def close():
                c3.destroy()
            a=Label(c3,text="APPOINTMENT.ID",font=('bold',10),bg='azure')
            a.place(x=50,y=50)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=400,y=50)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=170,y=50)
            c=Label(c3,text="PATIENT_ID",font=('bold',10),bg='azure')
            c.place(x=50,y=100)
            d=Entry(c3,width=10)
            d.place(x=170,y=100)
            e=Label(c3,text="DOCTER_ID",font=('bold',10),bg='azure')
            e.place(x=50,y=150)
            f=Entry(c3,width=10)
            f.place(x=170,y=150)
            g=Label(c3,text="DATE_OF_APPOINTMENT",font=('bold',10),bg='azure')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=170,y=200)
            j=Label(c3,text='TIME_VISIT',font=('bold',10),bg='azure')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=170,y=250)
            m=Label(c3,text='DISEASE',bg='azure')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=170,y=300)
            p=Label(c3,text='REMARK',font=('bold',10),bg='azure')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=170,y=350)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='azure',command=close)
            bt.place(x=200,y=450)
        def appointmentupdate():
            c3=Canvas(t,height=800,width=650,bg='aqua')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select AppID from appointmentdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select PatID,DocID,DateofAppointment,TimeVisit,Disease,Remarks from appointmentdata where AppID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
    
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,str(data[2]))
                k.insert(0,data[3])
                n.insert(0,str(data[4]))
                r.insert(0,data[5])
                db.close()
            def updatedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                bb=d.get()
                cc=f.get()
                dd=h.get()
                ee=k.get()
                ff=int(n.get())
                gg=r.get()
                
                
                sql="update appointmentdata set PatID=%d,DocID=%d,DateofAppointment='%s',TimeVisit='%s',Disease='%s',Remarks='%s' where AppID =%d"%(bb,cc,dd,ee,ff,gg,aa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Data Saved')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
            def close():
                c3.destroy()
               
                db.close()
            t.title('APPOINTMENT DATA')
            a=Label(c3,text="APPOINTMENT.ID",font=('bold',10),bg='aqua')
            a.place(x=50,y=50)
            a1=Button(c3,text='FIND',font=('bold',10),command=finddata)
            a1.place(x=350,y=50)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=170,y=50)
            c=Label(c3,text="PATIENT ID",font=('bold',10),bg='aqua')
            c.place(x=50,y=100)
            d=Entry(c3,width=10)
            d.place(x=170,y=100)
            e=Label(c3,text="DOCTER_ID",font=('bold',10),bg='aqua')
            e.place(x=50,y=150)
            f=Entry(c3,width=10)
            f.place(x=170,y=150)
            g=Label(c3,text="DOA",font=('bold',10),bg='aqua')
            g.place(x=50,y=200)
            h=Entry(c3,width=20)
            h.place(x=170,y=200)
            j=Label(c3,text='TIME_VISIT',font=('bold',10),bg='aqua')
            j.place(x=50,y=250)
            k=Entry(c3,width=10)
            k.place(x=170,y=250)
            m=Label(c3,text='DISEASE',font=('bold',10),bg='aqua')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=170,y=300)
            p=Label(c3,text='REMARK',font=('bold',10),bg='aqua')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=170,y=350)
            bt1=Button(c3,text='UPDATE',font=('bold',10),command=updatedata)
            bt1.place(x=200,y=400)
            bt=Button(c3,text='CLOSE',font=('bold',10),command=close)
            bt.place(x=300,y=400)
        def appointmentdelete():
            c3=Canvas(t,height=800,width=650,bg='olive')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select AppID from appointmentdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                    
            def deletedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                sql="delete from appointmentdata where AppID=%d"%(aa)
                cur.execute(sql)
                db.commit()
                db.close()
                b.delete(0,100)
                messagebox.showinfo('Hi','Data delete')
            def close():
                c3.destroy()
                
                
            a=Label(c3,text="APPOINTMENT.ID",font=('bold',10),bg='olive')
            a.place(x=50,y=50)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=170,y=50)
            c=Button(c3,text='DELETE',command=deletedata,font=('bold',10),bg='cyan')
            c.place(x=150,y=200)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=200)
        def appointmentinsert():
            c3=Canvas(t,height=800,width=650,bg='yellow')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=int(d.get())
                    cc=int(f.get())
                    dd=h.get()
                    ee=k.get()
                    ff=n.get()
                    gg=r.get()
                    sql="insert into clinicdata values(%d,%d,%d,'%s','%s','%s','%s')"%(aa,bb,cc,dd,ee,ff,gg)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    n.delete(0,100)
                    r.delete(0,100)
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from appointmentdata where AppID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
            def exit():
                c3.destroy()
    
            a=Label(c3,text="APPOINTMENT.ID",font=('bold',10),bg='yellow')
            a.place(x=50,y=50)
            b=Entry(c3,width=30)
            b.place(x=220,y=50)
            bt=Button(c3,text='CHECK',command=checkdata,font=('bold',10),bg='brown')
            bt.place(x=420,y=50)
            lt=Label(c3,text='Status',font=('bold',10),bg='yellow')
            lt.place(x=500,y=50)
    
            c=Label(c3,text="PATIENT_NAME",font=('bold',10),bg='yellow')
            c.place(x=50,y=100)
            d=Entry(c3,width=30)
            d.place(x=220,y=100)
            e=Label(c3,text="DOCTER_ID",font=('bold',10),bg='yellow')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=220,y=150)
            g=Label(c3,text="DATE_OF_APPOINTMENT",font=('bold',10),bg='yellow')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=220,y=200)
            j=Label(c3,text='TIME_VISIT',font=('bold',10),bg='yellow')
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=220,y=250)
            m=Label(c3,text='DISEASE',font=('bold',10),bg='yellow')
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=220,y=300)
            p=Label(c3,text='REMARK',font=('bold',10),bg='yellow')
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=220,y=350)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
            bt2=Button(c3,text='EXIT',command=exit,font=('bold',15),bg='cyan')
            bt2.place(x=300,y=450)
        def appointmentshowall():
            c3=Canvas(t,height=800,width=650,bg='bisque')
            c3.place(x=350,y=10)
            at=[]
            bt=[]
            ct=[]
            dt=[]
            et=[]
            ft=[]
            gt=[]
            i=0
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select * from appointmentdata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    at.append(res[0])
                    bt.append(res[1])
                    ct.append(res[2])
                    dt.append(res[3])
                    et.append(res[4])
                    ft.append(res[5])
                    gt.append(res[6])
                    
                db.close()
    
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
               
    
            def showprevious():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
    
            def showlast():
                global i
                i=len(at)-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                n.delete(0,100)
                r.delete(0,100)
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                n.insert(0,ft[i])
                r.insert(0,gt[i])
            def exit():
                c3.destroy()
            a=Label(c3,text='APPOINTMENT.ID',bg='bisque')
            a.place(x=50,y=50)
            b=Entry(c3,width=30)
            b.place(x=150,y=50 )
            c=Label(c3,text='PATIENT_NAME',bg='bisque')
            c.place(x=50,y=100)
            d=Entry(c3,width=30)
            d.place(x=150,y=100)
            e=Label(c3,text='DOCTER_ID',bg='bisque')
            e.place(x=50,y=150)
            f=Entry(c3,width=30)
            f.place(x=150,y=150)
            g=Label(c3,text='DATE_OF_APPOINTMENT',bg='bisque')
            g.place(x=50,y=200)
            h=Entry(c3,width=30)
            h.place(x=150,y=200)
            j=Label(c3,text='TIME_VISIT',bg='bisque',font=('bold',10))
            j.place(x=50,y=250)
            k=Entry(c3,width=30)
            k.place(x=150,y=250)
            m=Label(c3,text='DISEASE',bg='bisque',font=('bold',10))
            m.place(x=50,y=300)
            n=Entry(c3,width=30)
            n.place(x=150,y=300)
            p=Label(c3,text='REMARK',bg='bisque',font=('bold',10))
            p.place(x=50,y=350)
            r=Entry(c3,width=30)
            r.place(x=150,y=350)
            b1=Button(c3,text='First',command=showfirst)
            b1.place(x=50,y=420)
            b2=Button(c3,text='Next',command=shownext)
            b2.place(x=150,y=420)
            b3=Button(c3,text='Last',command=showlast)
            b3.place(x=250,y=420)
            b4=Button(c3,text='Previous',command=showprevious)
            b4.place(x=350,y=420)
            b5=Button(c3,text='EXIT',font=('bold',15),fg='cyan',command=exit)
            b5.place(x=200,y=500)
            filldata()
            showfirst()
        
        at=Label(c3,text='DOCTER OPERATIONS',font=('arial',30))
        at.place(x=50,y=10)
        ba=Button(c2,text='Insert',fg='blue',bg='yellow',font=('arial',15),command=appointmentinsert)
        ba.place(x=50,y=150)
        bb=Button(c2,text='Delete',fg='blue',bg='yellow',font=('arial',15),command=appointmentdelete)
        bb.place(x=50,y=250)    
        bc=Button(c2,text='Update',fg='blue',bg='yellow',font=('arial',15),command=appointmentupdate)
        bc.place(x=50,y=350)    
        bd=Button(c2,text='Find',fg='blue',bg='yellow',font=('arial',15),command=appointmentfind)
        bd.place(x=50,y=450)    
        be=Button(c2,text='ShowAll',fg='blue',bg='yellow',font=('arial',15),command=appointmentshowall)
        be.place(x=50,y=550)
        
    def showfeesdatabutton():
        def feesdatafind():
            c3=Canvas(t,height=800,width=800,bg='darksalmon')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select AppID from feedata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select PatID,DocID,DateofBill,Amount from feedata where AppID=%d"%(aa)
                cur.execute(sql)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                
                
                d.insert(0,data[0])
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,data[3])
                
                
                db.close()
            def close():
                c3.destroy()
            a=Label(c3,text="APPOINTMENT_ID",bg='darksalmon',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=550,y=100)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=310,y=100)
            c=Label(c3,text="PATIENT_ID",bg='darksalmon',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=30)
            d.place(x=310,y=150)
            e=Label(c3,text="DOCTER_ID",bg='darksalmon',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="DATE_OF_BILL",bg='darksalmon',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='AMOUNT',bg='darksalmon',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=50)
            k.place(x=310,y=300)
            bt=Button(c3,text='CLOSE',font=('bold',10),bg='cyan',command=close)
            bt.place(x=300,y=450)
        def feesdatainsert():
            c3=Canvas(t,height=800,width=800,bg='darkseagreen')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=int(d.get())
                    cc=int(f.get())
                    dd=h.get()
                    ee=int(k.get())
                    
                    
                    sql="insert into clinicdata values(%d,%d,%d,'%s',%d,)"%(aa,bb,cc,dd,ee)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    
                    
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from feedata where AppID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
                
            def close():
                c3.destroy()
            a=Label(c3,text="APPOINTMENT_ID",bg='darkseagreen',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='CHECK',command=checkdata,font=('bold',10))
            a1.place(x=550,y=100)
            b=Entry(c3,width=30)
            b.place(x=310,y=100)
            lt=Label(c3,text='Status',bg='darkseagreen',font=('bold',10))
            lt.place(x=620,y=100)
            c=Label(c3,text="PATIENT_ID",bg='darkseagreen',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=30)
            d.place(x=310,y=150)
            e=Label(c3,text="DOCTER_ID",bg='darkseagreen',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="DATE_OF_BILL",bg='darkseagreen',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='AMOUNT',bg='darkseagreen',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=10)
            k.place(x=310,y=300)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
        def feesdatadelete():
            c3=Canvas(t,height=800,width=800,bg='floralwhite')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select AppID from feedata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
                    
            def deletedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                sql="delete from feedata where AppID=%d"%(aa)
                cur.execute(sql)
                db.commit()
                db.close()
                b.delete(0,100)
                messagebox.showinfo('Hi','Data delete')
            def close():
                c3.destroy()
                            
            a=Label(c3,text="APPOINTMENT_ID:",font=('bold',10),bg='floralwhite')
            a.place(x=200,y=100)
            b=ttk.Combobox(c3,width=20)
            filldata()
            b['values']=dt
            b.place(x=345,y=105)
            c=Button(c3,text='DELETE',command=deletedata,font=('bold',15),bg='cyan')
            c.place(x=250,y=200)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=350,y=200)
        def feesdatainsert():
            c3=Canvas(t,height=800,width=800,bg='darkseagreen')
            c3.place(x=350,y=10)
            def savedata():
                if len(b.get())==0 or len(d.get())==0 or len(f.get())==0 or len(h.get())==0:
                    messagebox.showerror('Hi','please fill all data')
                else:
                    db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                    cur=db.cursor()
                    aa=int(b.get())
                    bb=int(d.get())
                    cc=int(f.get())
                    dd=h.get()
                    ee=int(k.get())
                    
                    
                    sql="insert into clinicdata values(%d,%d,%d,'%s',%d)"%(aa,bb,cc,dd,ee)
                    cur.execute(sql)
                    db.commit()
                    messagebox.showinfo('Hi','Saved')
                    b.delete(0,100)
                    d.delete(0,100)
                    f.delete(0,100)
                    h.delete(0,100)
                    k.delete(0,100)
                    
                    
                    db.close()
    
                
            def checkdata():
                x=int(b.get())
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select count(*) from feedata where AppID=%d"%(x)
                cur.execute(sql)
                data=cur.fetchone()
                if data[0]==0:
                    lt.config(text='Ok Pls go ahead',fg='green')
                else:
                    lt.config(text='Sorry not available',fg='red')
                db.close()
                
                
            def close():
                c3.destroy()
            a=Label(c3,text="APPOINTMENT_ID",bg='darkseagreen',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='CHECK',command=checkdata,font=('bold',10))
            a1.place(x=550,y=100)
            b=Entry(c3,width=30)
            b.place(x=310,y=100)
            lt=Label(c3,text='Status',bg='darkseagreen',font=('bold',10))
            lt.place(x=620,y=100)
            c=Label(c3,text="PATIENT_ID",bg='darkseagreen',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=30)
            d.place(x=310,y=150)
            e=Label(c3,text="DOCTER_ID",bg='darkseagreen',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="DATE_OF_BILL",bg='darkseagreen',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='AMOUNT',bg='darkseagreen',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=50)
            k.place(x=310,y=300)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
            bt=Button(c3,text='SAVE',command=savedata,font=('bold',15),bg='cyan')
            bt.place(x=200,y=450)
        def feesdataupdate():
            c3=Canvas(t,height=800,width=800,bg='deepskyblue')
            c3.place(x=350,y=10)
            dt=[]
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select AppID from feedata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    dt.append(res[0])
                db.close()
            def finddata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                
                sql="select PatID,DocID,DateofBill,Amount from feedata where AppID=%d"%(aa)
                cur.execute(sql)
                data=cur.fetchone()
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                
                
    
                d.insert(0,str(data[0]))
                f.insert(0,data[1])
                h.insert(0,data[2])
                k.insert(0,data[3])
                
                
                db.close()
            def updatedata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                aa=int(b.get())
                bb=int(d.get())
                cc=int(f.get())
                dd=h.get()
                ee=int(k.get())
                
                
                
                
                sql="update feedata set PatID=%d,DocID=%d,DateofBill='%s',Amount=%d where AppID=%d"%(bb,cc,dd,ee,aa)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Hi','Data Saved')
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
            def close():
                c3.destroy()
               
                db.close()
            t.title('STAFF INFO')
            a=Label(c3,text="APPOINTMENT_ID",bg='deepskyblue',font=('bold',10))
            a.place(x=180,y=100)
            a1=Button(c3,text='FIND',command=finddata,font=('bold',10))
            a1.place(x=550,y=90)
            b=ttk.Combobox(c3,width=30)
            filldata()
            b['values']=dt
            b.place(x=310,y=100)
            c=Label(c3,text="PATIENT_ID",bg='deepskyblue',font=('bold',10))
            c.place(x=180,y=150)
            d=Entry(c3,width=30)
            d.place(x=310,y=150)
            e=Label(c3,text="DOCTER_ID",bg='deepskyblue',font=('bold',10))
            e.place(x=180,y=200)
            f=Entry(c3,width=30)
            f.place(x=310,y=200)
            g=Label(c3,text="DATE_OF_BILL",bg='deepskyblue',font=('bold',10))
            g.place(x=180,y=250)
            h=Entry(c3,width=30)
            h.place(x=310,y=250)
            j=Label(c3,text='AMOUNT',bg='deepskyblue',font=('bold',10))
            j.place(x=180,y=300)
            k=Entry(c3,width=35)
            k.place(x=310,y=300)
            bt1=Button(c3,text='UPDATE',font=('bold',15),bg='cyan',command=updatedata)
            bt1.place(x=400,y=450)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
            bt=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            bt.place(x=300,y=450)
        def feesdatashowall():
            c3=Canvas(t,height=800,width=800,bg='gold')
            c3.place(x=350,y=10)
            at=[]
            bt=[]
            ct=[]
            dt=[]
            et=[]
            ft=[]
    
            i=0
            def filldata():
                db=pymysql.connect(host='localhost',user='root',password='root',db='das')
                cur=db.cursor()
                sql="select * from feedata"
                cur.execute(sql)
                data=cur.fetchall()
                for res in data:
                    at.append(res[0])
                    bt.append(res[1])
                    ct.append(res[2])
                    dt.append(res[3])
                    et.append(res[4])
                    
                    
                    
                db.close()
    
            def showfirst():
                global i
                i=0
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                
                
    
            def shownext():
                global i
                i=i+1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                
                
    
               
    
            def showprevious():
                global i
                i=i-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                
                
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
                
                
    
            def showlast():
                global i
                i=len(at)-1
                b.delete(0,100)
                d.delete(0,100)
                f.delete(0,100)
                h.delete(0,100)
                k.delete(0,100)
                
               
                b.insert(0,str(at[i]))
                d.insert(0,bt[i])
                f.insert(0,ct[i])
                h.insert(0,dt[i])
                k.insert(0,et[i])
            def close():
                c3.destroy()
                
            a=Label(c3,text="APPOINTMENT_ID",bg='gold',font=('bold',10))
            a.place(x=180,y=110)
            b=Entry(c3,width=10)
            b.place(x=310,y=110)
            c=Label(c3,text="PATIENT_ID",bg='gold',font=('bold',10))
            c.place(x=180,y=160)
            d=Entry(c3,width=10)
            d.place(x=310,y=160)
            e=Label(c3,text="DOCTER_ID",bg='gold',font=('bold',10))
            e.place(x=180,y=210)
            f=Entry(c3,width=10)
            f.place(x=310,y=210)
            g=Label(c3,text="DATE_OF_BILL",bg='gold',font=('bold',10))
            g.place(x=180,y=260)
            h=Entry(c3,width=10)
            h.place(x=310,y=260)
            j=Label(c3,text='AMOUNT',bg='gold',font=('bold',10))
            j.place(x=180,y=310)
            k=Entry(c3,width=10)
            k.place(x=310,y=310)
            b1=Button(c3,text='First',font=('bold',15),bg='cyan',command=showfirst)
            b1.place(x=200,y=400)
            b2=Button(c3,text='Next',font=('bold',15),bg='cyan',command=shownext)
            b2.place(x=300,y=400)
            b3=Button(c3,text='Last',font=('bold',15),bg='cyan',command=showlast)
            b3.place(x=400,y=400)
            b4=Button(c3,text='Previous',font=('bold',15),bg='cyan',command=showprevious)
            b4.place(x=500,y=400)
            b5=Button(c3,text='CLOSE',font=('bold',15),bg='cyan',command=close)
            b5.place(x=350,y=470)
            filldata()
            showfirst()
      
        at=Label(c3,text='FEES DATA',font=('arial',30))
        at.place(x=50,y=10)
        ba=Button(c2,text='Insert',fg='blue',bg='yellow',font=('arial',15),command=feesdatainsert)
        ba.place(x=50,y=150)
        bb=Button(c2,text='Delete',fg='blue',bg='yellow',font=('arial',15),command=feesdatadelete)
        bb.place(x=50,y=250)    
        bc=Button(c2,text='Update',fg='blue',bg='yellow',font=('arial',15),command=feesdataupdate)
        bc.place(x=50,y=350)    
        bd=Button(c2,text='Find',fg='blue',bg='yellow',font=('arial',15),command=feesdatafind)
        bd.place(x=50,y=450)    
        be=Button(c2,text='ShowAll',fg='blue',bg='yellow',font=('arial',15),command=feesdatashowall)
        be.place(x=50,y=550)
    
    a1=Label(c1,text="ALL SCREEN",fg='black',bg='orange',font=('arial',15))
    a1.place(x=30,y=50)    
    b1=Button(c1,text='CLINIC DATA',fg='white',bg='black',font=('arial',15),command=showclinicdatabutton)
    b1.place(x=20,y=150) 
    b2=Button(c1,text='DOCTERS',fg='white',bg='black',font=('arial',15),command=showdoctersdatabutton)
    b2.place(x=20,y=250)
    b3=Button(c1,text='PATIENTS',fg='white',bg='black',font=('arial',15),command=showpatientbutton)
    b3.place(x=20,y=350)
    b4=Button(c1,text='STAFF',fg='white',bg='black',font=('arial',15),command=showstaffbutton)
    b4.place(x=20,y=450)
    b5=Button(c1,text='APPOINTMENT',fg='white',bg='black',font=('arial',15),command=showappointmentbutton)
    b5.place(x=20,y=550)
    b7=Button(c1,text='FEES',fg='white',bg='black',font=('arial',15),command=showfeesdatabutton)
    b7.place(x=20,y=650)
    t.mainloop()
    
