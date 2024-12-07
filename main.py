from tkinter import *
from tkinter import ttk 


root = Tk() 
root.title('Employee Managent System')
root.geometry('1240x515+0+0')
root.resizable(False,False)
root.configure(bg = '#2c3e50')
logo = PhotoImage(file='logo.png')
lbl_logo= Label (root, image=logo, bg='#2c3e50')
lbl_logo.place( x=70, y=500)

#===== Entries Frame ====#
entries_frame =Frame(root, bg='#2c3e50')
entries_frame.place(x=1, y=1, width=360, height=510 )
title = Label(entries_frame, text= 'Employee company', font= ('calibri', 18, 'bold'), bg= '#2c3e50', fg= 'white')
title.place(x= 10, y= 1)

lblName = Label(entries_frame, text="Name", font= ('calibri', 16), bg= '#2c3e50', fg= 'white')
lblName.place(x=10, y=50)
txtName = Entry(entries_frame, width=20, font=('calibri', 16))
txtName.place(x=120, y=50)

lbljob = Label(entries_frame, text="Job", font= ('calibri', 16), bg= '#2c3e50', fg= 'white')
lbljob.place(x=10, y=90)
txtjob = Entry(entries_frame, width=20, font=('calibri', 16))
txtjob.place(x=120, y=90)

lblGender = Label(entries_frame,text="Gender",font=('calibri',16),bg='#2c3e50', fg='white')
lblGender.place(x=10,y=130)
comboGender = ttk.Combobox(entries_frame,state='readonly',width=18,font=('calibri',16))
comboGender['values']=["Male","Female"]
comboGender.place(x=120 , y=130)

lblAge = Label(entries_frame,text="Age",font=('calibri',16),bg='#2c3e50', fg='white')
lblAge.place(x=10,y=170)
txtAge = Entry(entries_frame,width=20,font=('calibri',16))
txtAge.place(x=120,y=170)

lblEmail = Label(entries_frame,text="Email",font=('calibri',16),bg='#2c3e50', fg='white')
lblEmail.place(x=10,y=210)
txtAge = Entry(entries_frame,width=20,font=('calibri',16))
txtAge.place(x=120,y=210)

lblContact = Label(entries_frame,text="Mopile",font=('calibri',16),bg='#2c3e50', fg='white')
lblContact.place(x=10,y=250)
txtAge = Entry(entries_frame,width=20,font=('calibri',16))
txtAge.place(x=120,y=250)

lblAdress= Label(entries_frame,text="Adress",font=('calibri',16),bg='#2c3e50', fg='white')
lblAdress.place(x=10,y=290)
txtAdress = Text(entries_frame,width=30,height=2,font=('calibri',16))
txtAdress.place(x=120,y=330)

#==========buttons Frame  =========
Btn_frame = Frame(entries_frame,bg='white',bd=1,relief=SOLID)
Btn_frame.place(x=10,y=400,width=335,height=100)
btnAdd= Button(Btn_frame ,
        text='Add Details',
        width=14,
        height=1,
        font=('calibri',16),
        fg='white',
        bg='#16a085',
        bd=0,
).place(x=4,y=5)

btnEdit= Button(Btn_frame ,
        text='Update Details',
        width=14,
        height=1,
        font=('calibri',16),
        fg='white',
        bg='#2980b9',
        bd=0,
).place(x=4,y=50)

btnDelete= Button(Btn_frame ,
        text='Delete Details',
        width=14,
        height=1,
        font=('calibri',16),
        fg='white',
        bg='#c0392b',
        bd=0,
).place(x=170,y=5)

btnClear= Button(Btn_frame ,
        text='Clear Details',
        width=14,
        height=1,
        font=('calibri',16),
        fg='white',
        bg='#f39c12',
        bd=0,
).place(x=170,y=50)


### ======== [Table Frame] ====== ###

tree_frame = Frame(root, bg = 'white')
tree_frame.place(x=365, y=1, width=875, height=610 )
style= ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50 )
style.configure("mystyle.Treeview.Heading",font=('Calibri',13))

tv= ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width="40")

tv.heading("2",text="Name")
tv.column("2",width="140")

tv.heading("3",text="Age")
tv.column("3",width="50")

tv.heading("4",text="Job")
tv.column("4",width="120")

tv.heading("5",text="Email")
tv.column("5",width="150")

tv.heading("6",text="Gender")
tv.column("6",width="90")

tv.heading("7",text="Mobile")
tv.column("7",width="150")

tv.heading("8",text="Address")
tv.column("8",width="150")

tv['show']='headings'

tv.place(x=1,y=1,height=610,width=875)
#===== [Define] ======

def hide():
    root.geometry("360x515+0+0")
def show():
     root.geometry('1240x615+0+0')
btnhide = Button(entries_frame, text='HIDE',bg='white',bd=1,relief=SOLID,cursor='hand2', command=hide)
btnhide.place(x=270,y=10)

btnshow = Button(entries_frame, text='SHOW',bg='white',bd=1,relief=SOLID,cursor='hand2', command=show)
btnshow.place(x=310,y=10)



root.mainloop()
