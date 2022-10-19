from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime
import os

def main():
    root =Tk()
    root.configure(width=1500,height=1500,bg='light blue')
    app = Window1(root)

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("PHARMACY MANAGEMENT SYSTEM")  #project title
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.username=StringVar()
        self.password=StringVar()

        self.LabelTitle =Label(self.frame,text='PHARMACY MANAGEMENT SYSTEM',font=('arial',50,'bold'),bd=20)
        self.LabelTitle.grid(row=0,column=0,columnspan=2,pady=20)

        self.Loginframe1=Frame(self.frame, width=1010,height=300,bd=20,relief='ridge')               #labels
        self.Loginframe1.grid(row=1,column=0)

        self.Loginframe2=Frame(self.frame,width=1000,height=100,bd=20,relief='ridge')
        self.Loginframe2.grid(row=2,column=0)

        self.Loginframe3=Frame(self.frame,width=1000,height=300,bd=20,relief='ridge')
        self.Loginframe3.grid(row=3,column=0,pady=2)
        #========================================
        self.lusername =Label(self.Loginframe1,text='Username',font=('arial',20,'bold'),bd=20)
        self.lusername.grid(row=0,column=0)
        self.txtusername =Entry(self.Loginframe1,font=('arial',20,'bold'),bd=20,textvariable=self.username)
        self.txtusername.grid(row=0,column=1 )

        self.lpassword =Label(self.Loginframe1,text='Password',font=('arial',20,'bold'),bd=20)
        self.lpassword.grid(row=1,column=0)
        self.txtpassword =Entry(self.Loginframe1,font=('arial',20,'bold'),bd=20,textvariable=self.password)
        self.txtpassword.grid(row=1,column=1,padx=85 )
        
        #========================================


        self.btnlogin=Button(self.Loginframe2,width=13 ,font=('arial',20,'bold'), text="LOGIN",command=self.login_sys)
        self.btnlogin.grid(row=0,column=0)

        self.btnreset=Button(self.Loginframe2,width=13 ,font=('arial',20,'bold'),text="RESET",command=self.reset)
        self.btnreset.grid(row=0,column=1)

        self.btnexit=Button(self.Loginframe2,width=13 ,font=('arial',20,'bold'),text="EXIT",command=self.exit1)
        self.btnexit.grid(row=0,column=2)
        #========================================

        self.btnRegistration = Button(self.Loginframe3,text="PHARMACY PORTAL",state=DISABLED,command =self.regis_window,font=('arial',20,'bold'))
        self.btnRegistration.grid(row = 0 , column =0)

        #========================================
    def login_sys(self):
        user=(self.username.get())
        pass1=(self.password.get())

        if (user == str(1234)) and (pass1 == str(12345)):           #username and password for login
            self.btnRegistration.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System","You have entred invalid Login details")
            self.btnRegistration.config(state = DISABLED)
            self.username.set("")
            self.password.set("")
            self.txtusername.focus()

            
    def reset(self):
        self.btnRegistration.config(state = DISABLED)
        self.username.set("")                                   #reset option
        self.password.set("")
        self.txtusername.focus()

    def exit1(self):
        self.exit1=tkinter.messagebox.askyesno("Pharmacy Management System","confirm if you want to exit")
        if self.exit1 > 0 :
            self.master.destroy()
            return
        #========================================


    def regis_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


class Window2:
    def __init__(self, master):
        #self.master = master
        #self.master.title("ENTER PHARMACY PORTAL")
        #self.master.geometry('1350x750+0+0')
        #self.frame = Frame(self.master)
        #self.frame.pack()
        #============================================================================
        f=open("database_proj",'a+')
        root = Tk()
        root.title("Poject on Pharmacy Managment System")
        root.configure(width=1500,height=600,bg='light blue')
        var=-1
        #bg_image1 = PhotoImage(file ='phar.png')
        #x = Label(image=bg_image1)
        #x.place(y=2,x=2)
        #bg_image2 = PhotoImage(file ='phar.png')
        #x = Label(image=bg_image2)                         if i want enable back ground image than i will use this option
        #x.place(y=380,x=2)
        #bg_image = PhotoImage(file ='phar.png')
        #x = Label(image=bg_image)
        #x.place(y=2,x=550)
        #bg_image3 = PhotoImage(file ='phar.png')
        #x = Label(image=bg_image3)
        #x.place(y=380,x=550)


        def additem():
            global var
            num_lines = 0
            with open("database_proj", 'r') as f10:
                for line in f10:
                    num_lines += 1
            var=num_lines-1
            e1= entry1.get()
            e2=entry2.get()
            e3=entry3.get()
            e4=entry4.get()
            e5=entry5.get()
            f.write('{0} {1} {2} {3} {4}\n'.format(str(e1),e2,e3,str(e4),e5))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            #f.close()


        def deleteitem():
            e1=entry1.get()
            with open(r"database_proj") as f, open(r"database_proj1", "w") as working:
                for line in f:
                    if str(e1) not in line:
                        working.write(line)
            os.remove(r"database_proj")
            os.rename(r"database_proj1", r"database_proj")
            f.close()
            working.close()
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)

        def firstitem():
            global var
            var=0
            f.seek(var)
            c=f.readline()
            v=list(c.split(" "))
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry1.insert(0,str(v[0]))
            entry2.insert(0,str(v[1]))
            entry3.insert(0,str(v[2]))
            entry4.insert(0,str(v[3]))
            entry5.insert(0,str(v[4]))

        def nextitem():
            global var
            var = var + 1
            f.seek(var)
            try:
                c=f.readlines()
                xyz = c[var]
                v = list(xyz.split(" "))
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)
                entry1.insert(0, str(v[0]))
                entry2.insert(0, str(v[1]))
                entry3.insert(0, str(v[2]))
                entry4.insert(0, str(v[3]))
                entry5.insert(0, str(v[4]))
            except:
                tkinter.messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")
        def previousitem():
                global var
                var=var-1
                f.seek(var)
                try:
                    z = f.readlines()
                    xyz=z[var]
                    v = list(xyz.split(" "))
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    entry3.delete(0, END)
                    entry4.delete(0, END)
                    entry5.delete(0, END)

                    entry1.insert(0, str(v[0]))
                    entry2.insert(0, str(v[1]))
                    entry3.insert(0, str(v[2]))
                    entry4.insert(0, str(v[3]))
                    entry5.insert(0, str(v[4]))
                except:
                    tkinter.messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


        def lastitem():
            global var
            f4=open("database_proj",'r')
            x=f4.read().splitlines()
            last_line= x[-1]
            num_lines = 0
            with open("database_proj", 'r') as f8:
                for line in f8:
                    num_lines += 1
            var=num_lines-1
            print(last_line)
            try:
                v = list(last_line.split(" "))
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                entry5.delete(0, END)

                entry1.insert(0, str(v[0]))
                entry2.insert(0, str(v[1]))
                entry3.insert(0, str(v[2]))
                entry4.insert(0, str(v[3]))
                entry5.insert(0, str(v[4]))
            except:
                messagebox.showinfo("Title", "SORRY!...NO MORE RECORDS")


        def updateitem():

            e1 = entry1.get()
            e2 = entry2.get()
            e3 = entry3.get()
            e4 = entry4.get()
            e5 = entry5.get()
            with open(r"database_proj") as f1, open(r"database_proj1", "w") as working:
                for line in f1:
                    if str(e1) not in line:
                        working.write(line)
                    else:
                        working.write('{0} {1} {2} {3} {4}'.format(str(e1), e2, e3, str(e4), e5))
            os.remove(r"database_proj")
            os.rename(r"database_proj1", r"database_proj")


        def searchitem():
            i=0
            e11 = entry1.get()
            with open(r"database_proj") as working:
                for line in working:
                    i=i+1
                    if str(e11) in line:
                        break
                try:
                    v = list(line.split(" "))
                    entry1.delete(0, END)
                    entry2.delete(0, END)
                    entry3.delete(0, END)
                    entry4.delete(0, END)
                    entry5.delete(0, END)
                    entry1.insert(0, str(v[0]))
                    entry2.insert(0, str(v[1]))
                    entry3.insert(0, str(v[2]))
                    entry4.insert(0, str(v[3]))
                    entry5.insert(0, str(v[4]))
                except:
                    messagebox.showinfo("Title", "error end of file")
            working.close()
            f.close()


        def clearitem():
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
        #fn1353
        label0= Label(root,text="PHARMACY MANAGEMENT SYSTEM ",bg="black",fg="white",font=("algerian", 30))
        label1=Label(root,text="ENTER ITEM NAME",bg="light blue",relief="ridge",fg="black",font=("Times", 12,"bold"),width=30)
        entry1=Entry(root , font=("Times", 12),width=40)
        label2=Label(root, text="ENTER ITEM PRICE",bd="2",relief="ridge",height="1",bg="light blue",fg="black", font=("Times", 12,"bold"),width=30)
        entry2= Entry(root, font=("Times", 12),width=40)
        label3=Label(root, text="ENTER ITEM QUANTITY",bd="2",relief="ridge",bg="light blue",fg="black", font=("Times", 12,"bold"),width=30)
        entry3= Entry(root, font=("Times", 12),width=40)
        label4=Label(root, text="ENTER ITEM CATEGORY",bd="2",relief="ridge",bg="light blue",fg="black", font=("Times", 12,"bold"),width=30)
        entry4= Entry(root, font=("Times", 12),width=40)
        label5=Label(root, text="ENTER ITEM DISCOUNT",bg="light blue",relief="ridge",fg="black", font=("Times", 12,"bold"),width=30)
        entry5= Entry(root, font=("Times", 12),width=40)
        button1= Button(root, text="ADD ITEM", bg="light green", fg="black", width=20, font=("Times", 12,"bold"),command=additem)
        button2= Button(root, text="DELETE ITEM", bg="light green", fg="black", width =20, font=("Times", 12,"bold"),command=deleteitem)
        button3= Button(root, text="VIEW FIRST ITEM" , bg="light green", fg="black", width =20, font=("Times", 12,"bold"),command=firstitem)
        button4= Button(root, text="VIEW NEXT ITEM" , bg="light green", fg="black", width =20, font=("Times", 12,"bold"), command=nextitem)
        button5= Button(root, text="VIEW PREVIOUS ITEM", bg="light green", fg="black", width =20, font=("Times", 12,"bold"),command=previousitem)
        button6= Button(root, text="VIEW LAST ITEM", bg="light green", fg="black", width =20, font=("Times", 12,"bold"),command=lastitem)
        button7= Button(root, text="UPDATE ITEM", bg="light green", fg="black", width =20, font=("Times", 12,"bold"),command=updateitem)
        button8= Button(root, text="SEARCH ITEM", bg="light green", fg="black", width =20, font=("Times", 12,"bold"),command=searchitem)
        button9= Button(root, text="CLEAR SCREEN", bg="light green", fg="black", width=20, font=("Times", 12,"bold"),command=clearitem)
        label0.grid(columnspan=6, padx=10, pady=10)
        label1.grid(row=1,column=0, sticky=W, padx=10, pady=10)
        label2.grid(row=2,column=0, sticky=W, padx=10, pady=10)
        label3.grid(row=3,column=0, sticky=W, padx=10, pady=10)
        label4.grid(row=4,column=0, sticky=W, padx=10, pady=10)
        label5.grid(row=5,column=0, sticky=W, padx=10, pady=10)
        entry1.grid(row=1,column=1, padx=40, pady=10)
        entry2.grid(row=2,column=1, padx=10, pady=10)
        entry3.grid(row=3,column=1, padx=10, pady=10)
        entry4.grid(row=4,column=1, padx=10, pady=10)
        entry5.grid(row=5,column=1, padx=10, pady=10)
        button1.grid(row=6,column=0, padx=30, pady=10)
        button2.grid(row=6,column=1, padx=30, pady=10)
        button3.grid(row=6,column=2, padx=30, pady=10)
        button4.grid(row=7,column=0, padx=30, pady=10)
        button5.grid(row=7,column=1, padx=30, pady=10)
        button6.grid(row=7,column=2, padx=30, pady=10)
        button7.grid(row=8,column=0, padx=30, pady=10)
        button8.grid(row=8,column=1, padx=30, pady=10)
        button9.grid(row=8,column=2, padx=30, pady=10)
        root.mainloop()

if __name__ == '__main__':
    main()
         
