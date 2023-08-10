from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

def login():
    if usernameEntry.get()==''or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Abhishek' and passwordEntry.get()=='123':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import air
        
        
    else:
        messagebox.showerror('Error','Please enter correct values')
        


window=Tk()
window.geometry("1540x800+0+0")
window.title('Airline management')

window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='back.jpg')
#image=Image.open('airlineback.jpg')
#reimage=image.resize((100,100))
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

#logoImage=PhotoImage(file='logo.jpg')
#logoLabel=Label(loginFrame,image=logoImage)
#logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

#usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,text='username',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


#passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,text='Password',compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)


loginButton=Button(loginFrame,text='login',font=('times new roman',20,'bold'),width=15,fg='white',bg='cornflowerblue',
                   activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=15)

window.mainloop()
from tkinter import *
import time
#import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
#functionality Part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass
   # set_theme
#def export_data():
#    url=filedialog.asksaveasfilename(defaultextension='.csv')
#    indexing=studentTable.get_children()
#    newlist=[]
#    for index in indexing:
#        content=studentTable.item(index)
#        datalist=content['values']
#        newlist.append(datalist)


#   table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','From','To','Added Date','Added Time'])
#    table.to_csv(url,index=False)
#    messagebox.showinfo(…