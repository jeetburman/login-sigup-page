from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
#----------------Functionality------------------------#

def reset_password():
    login_window.destroy()
    import forgotpass

def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='' or usernameEntry.get()=='Username' or passwordEntry.get()=='password':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='@Maheyk0902')
            myCursor = con.cursor()
        except:
            messagebox.showerror("Error","Connection not established with Database")
            return
        query = 'use userdata'
        myCursor.execute(query)
        query = 'select * from data where username=%s and password=%s'
        myCursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row = myCursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is Successful')

def sign_up():  #Signup and Signin link func
    login_window.destroy()
    import signup


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)

def password_enter(event):
    if passwordEntry.get() == 'password':
        passwordEntry.delete(0,END)


#Show and hide functions of password:
def show():
    openEye.config(file='imgs/openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
def hide():
    openEye.config(file='imgs/closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

#----------------GUI PART-----------------------------#
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)  #Disabling screen maximizing and minimizing
login_window.title('Python Login Page')  #Title

#BackgroundIMG
bgImage = ImageTk.PhotoImage(file='imgs/bg.jpg')
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)

#Entries Boxes
#UsernameBox
usernameEntry = Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=580,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',user_enter)

#Dash and color of dash
frame1 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=222)

#passwordBox
passwordEntry = Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=580,y=260)
passwordEntry.insert(0,'password')
passwordEntry.bind('<FocusIn>',password_enter)

#Dash and color of dash
frame2 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=282)

#Eye button image
openEye = PhotoImage(file='imgs/openeye.png')
eyeButton = Button(login_window,image=openEye,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=800,y=255)

#Forgot password
forgetButton = Button(login_window,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',
                      font=('Microsoft Yahei UI Light',9,'bold'),
                      fg='firebrick1',activeforeground='firebrick1',command=reset_password)
forgetButton.place(x=715,y=295)

#login button
loginButton = Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',bg='firebrick1',
                     activeforeground='white',activebackground='firebrick1',cursor='hand2',bd=0,width=19,command=login_user)
loginButton.place(x=578,y=350)

#Partition
orLabel = Label(login_window,text='--------------OR---------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=583,y=400)

#Social link options
facebook_logo = PhotoImage(file='imgs/facebook.png')
fbLabel = Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=640,y=440)

google_logo = PhotoImage(file='imgs/google.png')
googleLabel = Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=685,y=440)

twitter_logo = PhotoImage(file='imgs/twitter.png')
twitLabel = Label(login_window,image=twitter_logo,bg='white')
twitLabel.place(x=730,y=440)

#Partition
signupLabel = Label(login_window,text='Dont have an account?',font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=575,y=500)

#signup button
newaccountButton = Button(login_window,text='Create new one',font=('Open Sans',9,'bold underline'),fg='blue',bg='white',
                     activeforeground='blue',activebackground='white',cursor='hand2',bd=0,width=19,command=sign_up)
newaccountButton.place(x=710,y=500)

login_window.mainloop() #Dialog box bringer