from tkinter import *
from tkinter import messagebox
import sqlite3

conn=sqlite3.connect("hms.db")
#print("connection successful")

c=conn.cursor()

#for appointments
number=[]
patients=[]
sql="select * from appointment"
res=c.execute(sql)
for r in res:
    ids=r[0]
    names=r[1]
    number.append(ids)
    patients.append(names)

#page with functional buttons
class MainPage:
    def __init__(self,master):
        self.master=master
        master.title("Hospital Management System")
        
        self.welcome=Label(master,text="SoftCare Systems",font=("Helvetica", 20),bg="#FFFFFF")
        self.welcome.place(x=300,y=20)

        self.d=PhotoImage(file="display.png")
        self.img1=PhotoImage(file="register.png")
        #img1 = img1.subsample(5)

        self.img2=PhotoImage(file="appointment.png")
        #img2 = img2.subsample(3)

        self.img3=PhotoImage(file="edit.png")
        #img3 = img3.subsample(3)

        self.da=Button(master,image=self.d,height=40,width=170,command=self.disp)
        self.da.place(x=10,y=50)
        
        self.enter1=Button(master,image=self.img1,height=45,width=180,command=self.regist)
        self.enter1.place(x=300,y=150)

        self.enter2=Button(master,image=self.img2,height=45,width=180,command=self.appoint)
        self.enter2.place(x=300,y=250)

        self.enter3=Button(master,image=self.img3,height=45,width=180,command=self.callback)
        self.enter3.place(x=300,y=350)

        self.tail=Label(master,text="Copyright : ET Project 2019",font=("Helvetica", 16),bg="#FFFFFF")
        self.tail.place(x=300,y=500)

    def callback(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        disp=Edit(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")

    def disp(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        disp=Display(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")
        
    def regist(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        regist=Register(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")
        
    def appoint(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        appoint=Appointment(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")


# ***********registration page
class Register:
    def __init__(self,master):
        self.master=master
     
        master.title("Registration")
        
        self.welcome=Label(master,text="SoftCare Systems",font=("Helvetica", 20),bg="#FFFFFF")
        self.welcome.place(x=300,y=20)

        self.img1=PhotoImage(file="home.png")

        self.register=Label(master,text="Registration Page",font=("Helvetica",18),bg="#FFFFFF")
        self.register.place(x=0,y=80)


        self.Name=Label(master,text="Name : ",font=("Helvetica",12),bg="#FFFFFF")
        self.Name.place(x=0,y=150)
        self.r_n=Entry(master)
        self.r_n.place(x=150,y=150)

        self.Age=Label(master,text="Age :",font=("Helvetica",12),bg="#FFFFFF")
        self.Age.place(x=0,y=200)
        self.r_a=Entry(master)
        self.r_a.place(x=150,y=200)

        self.Sex=Label(master,text="Gender :",font=("Helvetica",12),bg="#FFFFFF")
        self.Sex.place(x=0,y=250)
        self.r_s=Entry(master)
        self.r_s.place(x=150,y=250)

        self.Disease=Label(master,text="Disease :",font=("Helvetica",12),bg="#FFFFFF")
        self.Disease.place(x=0,y=300)
        self.r_d=Entry(master)
        self.r_d.place(x=150,y=300)

        self.Phone=Label(master,text="Phone :",font=("Helvetica",12),bg="#FFFFFF")
        self.Phone.place(x=0,y=350)
        self.r_p=Entry(master)
        self.r_p.place(x=150,y=350)

        self.addr=Label(master,text="Address :",font=("Helvetica",12),bg="#FFFFFF")
        self.addr.place(x=0,y=400)
        self.r_ad=Entry(master)
        self.r_ad.place(x=150,y=400)

        self.img=PhotoImage(file="regist.png")
        #img = img.subsample(5)

        self.enter=Button(master,image=self.img,height=35,width=180,command=self.callback)
        self.enter.place(x=300,y=450)

        self.mainpage=Button(master,image=self.img1,height=35,width=180,command=self.mainpage)
        self.mainpage.place(x=0,y=450)

        self.tail=Label(master,text="Copyright : ET Project 2019",font=("Helvetica", 16),bg="#FFFFFF")
        self.tail.place(x=300,y=500)
        
    def callback(self):
        self.name= self.r_n.get()
        self.age= self.r_a.get()
        self.gender= self.r_s.get()
        self.disease= self.r_d.get()
        self.phone= self.r_p.get()
        self.addr= self.r_ad.get()

        if self.name=="" or self.age=="" or self.gender=="" or self.disease=="" or self.phone=="" or self.addr=="":
            messagebox.showinfo('Error', 'Please Fill Everything')
        else:
            sql="insert into 'register'(name,age,gender,phone,addr,t_type) VALUES(?,?,?,?,?,?)"
            c.execute(sql,(self.name,self.age,self.gender,self.phone,self.addr,self.disease))
            conn.commit()
            messagebox.showinfo('Registered', "Account Registered Successfully")

    def mainpage(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        ab=MainPage(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")


#************registration ends here

#-----------Appointment----------------------

class Appointment:
    def __init__(self,master):
        self.master=master
     
        master.title("Registration")

        self.img1=PhotoImage(file="home.png")
        self.img2=PhotoImage(file="book.png")
        
        self.welcome=Label(master,text="SoftCare Systems",font=("Helvetica", 20),bg="#FFFFFF")
        self.welcome.place(x=300,y=20)

        self.phone=Label(master,text="Enter Contact Number : ",font=("Helvetica",12),bg="#FFFFFF")
        self.phone.place(x=0,y=150)
        self.r_p=Entry(master)
        self.r_p.place(x=200,y=150)

        self.search=Button(master,text="Search",height=1,width=10,command=self.search_db)
        self.search.place(x=350,y=150)

        self.mainpage=Button(self.master,image=self.img1,height=45,width=180,command=self.mainpage)
        self.mainpage.place(x=450,y=135)

        self.tail=Label(master,text="Copyright : ET Project 2019",font=("Helvetica", 16),bg="#FFFFFF")
        self.tail.place(x=300,y=500)
    
    def search_db(self):
        self.chk=self.r_p.get()
        sql="SELECT * FROM register WHERE phone LIKE ?"
        self.res=c.execute(sql,(self.chk,))
        for self.row in self.res:
            self.name=self.row[1]
            self.age=self.row[2]
            self.phn=self.row[4]
        
        self.Name=Label(self.master,text="Name : ",font=("Helvetica",12),bg="#FFFFFF")
        self.Name.place(x=0,y=200)
        self.r_n=Entry(self.master)
        self.r_n.place(x=150,y=200)
        self.r_n.insert(END,str(self.name))

        self.Age=Label(self.master,text="Age :",font=("Helvetica",12),bg="#FFFFFF")
        self.Age.place(x=0,y=250)
        self.r_a=Entry(self.master)
        self.r_a.place(x=150,y=250)
        self.r_a.insert(END,str(self.age))

        self.Phone=Label(self.master,text="Phone :",font=("Helvetica",12),bg="#FFFFFF")
        self.Phone.place(x=0,y=300)
        self.r_p=Entry(self.master)
        self.r_p.place(x=150,y=300)
        self.r_p.insert(END,str(self.phn))

        self.book=Button(self.master,image=self.img2,height=45,width=180,command=self.book)
        self.book.place(x=0,y=400)

        

    def book(self):
        self.an=self.name
        self.aphn=self.phn

        sql1="INSERT into 'appointment'(name,phone) VALUES(?,?)"
        c.execute(sql1,(self.an,self.aphn))
        conn.commit()
        messagebox.showinfo('Booked', "Appointment Booked !!!")

    def mainpage(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        ab=MainPage(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")

#-----------Appointment ends here------------


#===============Displating Appointments===========

class Display:
    def __init__(self,master):
        self.master=master
        self.x=0
        
        self.img2=PhotoImage(file="next.png")
        self.img1=PhotoImage(file="home.png")
        self.heading=Label(master,text="Appointments",font=('Helvetica 40 bold'),bg="#FFFFFF")
        self.heading.place(x=200,y=10)
        self.change=Button(master,image=self.img2,width=180,height=45,command=self.func)
        self.change.place(x=500,y=400)

        self.id=Label(master,text="",font=('arial 40 bold'),bg="white")
        self.id.place(x=400,y=100)
        self.name=Label(master,text="",font=('arial 60 bold'),bg="white")
        self.name.place(x=300,y=200)

        self.mainpage=Button(self.master,image=self.img1,height=45,width=180,command=self.mainpage)
        self.mainpage.place(x=0,y=400)

    def func(self):
        self.id.config(text=str(number[self.x]))
        self.name.config(text=str(patients[self.x]))
        self.x +=1

    def mainpage(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        ab=MainPage(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")
        

#=============End=====================

#''''''''''''''''''''''Editing data''''''''''

class Edit:
    def __init__(self,master):
        self.master=master        
        self.img1=PhotoImage(file="home.png")
        self.welcome=Label(master,text="SoftCare Systems",font=("Helvetica", 20),bg="#FFFFFF")
        self.welcome.place(x=300,y=20)

        self.phone=Label(master,text="Enter Contact Number : ",font=("Helvetica",12),bg="#FFFFFF")
        self.phone.place(x=0,y=100)
        self.r_p=Entry(master)
        self.r_p.place(x=200,y=100)

        self.search=Button(master,text="Search",height=1,width=10,command=self.search_db)
        self.search.place(x=350,y=100)

        self.mainpage=Button(self.master,image=self.img1,height=45,width=180,command=self.mainpage)
        self.mainpage.place(x=450,y=100)

        

        self.tail=Label(master,text="Copyright : ET Project 2019",font=("Helvetica", 16),bg="#FFFFFF")
        self.tail.place(x=300,y=550)
        
    def search_db(self):
        self.chk=self.r_p.get()
        sql="SELECT * FROM register WHERE phone LIKE ?"
        self.res=c.execute(sql,(self.chk,))
        for self.row in self.res:
            self.name=self.row[1]
            self.age=self.row[2]
            self.gender=self.row[3]
            self.phn=self.row[4]
            self.addr=self.row[5]
            self.disease=self.row[6]
        
        self.Name=Label(self.master,text="Name : ",font=("Helvetica",12),bg="#FFFFFF")
        self.Name.place(x=0,y=150)
        self.r_n=Entry(self.master)
        self.r_n.place(x=150,y=150)
        self.r_n.insert(END,str(self.name))

        self.Age=Label(self.master,text="Age :",font=("Helvetica",12),bg="#FFFFFF")
        self.Age.place(x=0,y=200)
        self.r_a=Entry(self.master)
        self.r_a.place(x=150,y=200)
        self.r_a.insert(END,str(self.age))

        self.g=Label(self.master,text="Gender : ",font=("Helvetica",12),bg="#FFFFFF")
        self.g.place(x=0,y=250)
        self.r_g=Entry(self.master)
        self.r_g.place(x=150,y=250)
        self.r_g.insert(END,str(self.gender))

        self.Phone=Label(self.master,text="Phone :",font=("Helvetica",12),bg="#FFFFFF")
        self.Phone.place(x=0,y=300)
        self.r_p=Entry(self.master)
        self.r_p.place(x=150,y=300)
        self.r_p.insert(END,str(self.phn))

        self.add=Label(self.master,text="Address : ",font=("Helvetica",12),bg="#FFFFFF")
        self.add.place(x=0,y=350)
        self.r_aa=Entry(self.master)
        self.r_aa.place(x=150,y=350)
        self.r_aa.insert(END,str(self.addr))

        self.dis=Label(self.master,text="Disease : ",font=("Helvetica",12),bg="#FFFFFF")
        self.dis.place(x=0,y=400)
        self.r_d=Entry(self.master)
        self.r_d.place(x=150,y=400)
        self.r_d.insert(END,str(self.disease))

        self.book=Button(self.master,text="Update",height=3,width=20,command=self.update)
        self.book.place(x=75,y=450)

    def update(self):
        self.un=self.r_n.get()
        self.ua=self.r_a.get()
        self.ug=self.r_g.get()
        self.uphn=self.r_p.get()
        self.uadd=self.r_aa.get()
        self.ud=self.r_d.get()

        #print(self.un," ",self.ua," ",self.ug," ",self.uphn," ",self.uadd," ",self.ud)

        sql1="update register set name=?,age=?,gender=?,phone=?,addr=?,t_type=? where phone like ?"
        c.execute(sql1,(self.un,self.ua,self.ug,self.uphn,self.uadd,self.ud,self.r_p.get()))
        conn.commit()
        messagebox.showinfo('Updated', "Data Updated !!!")

    def mainpage(self):
        self.master.withdraw()
        self.newWindow=Toplevel(self.master)
        ab=MainPage(self.newWindow)
        self.newWindow.geometry("800x600")
        self.newWindow.configure(background="#FFFFFF")

#''''''''''''''''''''''Editing Data Ends'''''
root = Tk()
b=MainPage(root)

root.geometry("800x600")
root.configure(background="#FFFFFF")
root.resizable(False,False)

root.mainloop()
