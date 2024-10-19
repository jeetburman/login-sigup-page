from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql

#-------------------------Functionality--------------------------------#
def change_password():
    if emailEntry.get() == '' or passwordEntry.get() == '' or confirmEntry.get() == '':
        messagebox.showerror('Error','Fields cannot be empty',parent=reset_password)
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Password & Confirm password not matching',parent=reset_password)
    else:
        con = pymysql.connect(host='localhost',user='root',password='@Maheyk0902',database='userdata')
        mycursor = con.cursor()
        query = 'select * from data where email=%s'
        mycursor.execute(query,(emailEntry.get(),))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error',"Incorrect Email",parent=reset_password)
        else:
            query = 'update data set password=%s where email=%s'
            mycursor.execute(query,(passwordEntry.get(),emailEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success","Password was reset",parent=reset_password)
            reset_password.destroy()



#--------------------------GUI------------------------------------------#

reset_password = Tk()
reset_password.title('Forgot password') #Title of dialogue box
reset_password.resizable(FALSE,FALSE) #Disabling screen maximizing and minimizing
background = ImageTk.PhotoImage(file='imgs/bg.jpg')

bgLabel = Label(reset_password,image=background)
bgLabel.grid()

frame = Frame(reset_password,bg='white')
frame.place(x=554,y=100)

#heading
heading = Label(frame,text='Password Reset',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1',pady=10)
heading.grid(row=0,column=0)

heading=Label(frame)


#Email box
emaillabel = Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emaillabel.grid(row=1,column=0,sticky='w',padx=25,pady=(30,0))
emailEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

#password box
passwordlabel = Label(frame,text='password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordlabel.grid(row=5,column=0,sticky='w',padx=25,pady=(30,0))
passwordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

#confirm password box
confirmlabel = Label(frame,text='confirm password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmlabel.grid(row=7,column=0,sticky='w',padx=25,pady=(30,0))
confirmEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

#Submit button
signupButton = Button(frame,text='Submit',font=('Microsoft Yahei UI Light',16,'bold'),bd=0
                      ,bg='firebrick1',fg='white',activebackground='firebrick1',activeforeground='white',width=17
                      ,command=change_password)
signupButton.grid(row=10,column=0,pady=(60,0))


reset_password.mainloop()