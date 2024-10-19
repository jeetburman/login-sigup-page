from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

#----------------------Functionality--------------------------------

def clear(): #clearing boxes after submission
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)
def login_page(): #login page linking func
    signup_window.destroy()
    import signin
def connect_database(): #error function
    if emailEntry.get()=="" or usernameEntry.get()=="" or passwordEntry.get()=="" or confirmEntry.get()=="":
        messagebox.showerror('Error','All Fields are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror("Error","T&C not accepted")
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='@Maheyk0902')
            myCursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue')
            return
#MySQL queries and data collection
        try:
            query = 'create database userdata'
            myCursor.execute(query)
            query = 'use userdata'
            myCursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            myCursor.execute(query)
        except:
            myCursor.execute('use userdata')

        # query = 'select * from data where username = %s'
        # myCursor.execute(query,(usernameEntry.get()))
        query = 'select * from data where email = %s'
        myCursor.execute(query,(emailEntry.get()))

        # row = myCursor.fetchone()
        col = myCursor.fetchone()
        if col != None:
            messagebox.showerror('Error','Email already registered')
        # if row != None:
        #     messagebox.showerror('Error','Username already exists')
        else:
            query='insert into data(email,username,password) values(%s,%s,%s)'
            myCursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            import signin



#-----------------------GUI-----------------------------------------
signup_window = Tk()
signup_window.title('SignUp Page') #Title of dialogue box
signup_window.resizable(FALSE,FALSE) #Disabling screen maximizing and minimizing
background = ImageTk.PhotoImage(file='imgs/bg.jpg')

bgLabel = Label(signup_window,image=background)
bgLabel.grid()

frame = Frame(signup_window,bg='white')
frame.place(x=554,y=100)

#heading
heading = Label(frame,text='Create an Account',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0)

heading=Label(frame)

#Email box
emaillabel = Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))
emailEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

#username box
usernamelabel = Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernamelabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))
usernameEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

#password box
passwordlabel = Label(frame,text='password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))
passwordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

#confirm password box
confirmlabel = Label(frame,text='confirm password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmlabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))
confirmEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

#T&C check box
check = IntVar()
termsAndConditions=Checkbutton(frame,text='I agree to the Terms and Condtions',font=('Microsoft Yahei UI Light',10,'bold')
                               ,fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1'
                               ,cursor='hand2',variable=check)
termsAndConditions.grid(row=9,column=0,pady=(15,0),padx=10)


#Signup button
signupButton = Button(frame,text='Sign-Up',font=('Microsoft Yahei UI Light',16,'bold'),bd=0
                      ,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17
                      ,command=connect_database)
signupButton.grid(row=10,column=0,pady=(15,0))

#Already have an account partition
alreadyLabel = Label(frame,text='Already have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
alreadyLabel.grid(row=11,column=0,sticky='w',padx=20,pady=(15,0))

#login button
loginButton = Button(frame,text='Login',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',
                     activeforeground='blue',activebackground='white',cursor='hand2',bd=0,width=10
                     ,command=login_page)
loginButton.place(x=170,y=397)


signup_window.mainloop()