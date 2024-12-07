import sqlite3
from typing import Self
class Database :
    def _init_(self,db):
        self.con = sqlite3 .Connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREAT TABLE IF NOT EXISTS emoloyees (
           id Integer Primary Key, 
           name text,
           age text, 
           job text, 
           email text, 
           gender text ,
           mobile text ,
           address text,
        )
        """
        self.cur.execute (sql) 
        Self.con.commit ()

    def insert(self,name,age,job,email,gender,mobile,address):
        self.cur.execute("insert into employee values (NULL,?,?,?,?,?,?,?)",
                         (name,age,job,email,gender,mobile,address)
        )
        self.con.commit()

    def fetch(self):
        self.cur.execute (" SELECT * FROM employess") 
        rows = self.cur.fetchall ()
        return rows

    def remove(self):
        self.cur.execute("delete from employees where id=?",(id,)) 
        self.con.commit()

    def update(self,name,age,job,email,gender,mobile,address):
        self.cur.execute("update employees set name=?, age=?, job=?, email=?,gender=?, mobile=?, address=? where id=?",
                         )


#aya
def delete():
    db.remove(row[0])
    Clear()
    displayAll()
def Clear():
    name.set("")
    age.set("")
    job.set("")
    genders.set("")
    email.set("")
    mobile.set("")
    txtAddress.delete(1.0,END)
def add_employee():
    if txtName.get() == "" or txtAge.get() =="" or txtjob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtEmail.get()=="" or txtAdress.get(1.0,END)  == "" :
        messagebox.showerror("Error" ,"Please Fill all the entry")
        return
    
    db.insert(
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtmobile.get(),
        txtAdress.get(1.0,END)
    )
    messagebox.showinfo("Success","Added new Employee")
    clear()
    displayAll()

def update():
    if txtName.get() == "" or txtAge.get() =="" or txtjob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtEmail.get()=="" or txtAdress.get(1.0,END)  == "" :
        messagebox.showerror("Error" ,"Please Fill all the entry")
        return
    
    db.update(row[0],
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtmobile.get(),
        txtAdress.get(1.0,END)
    )
    messagebox.showinfo('Success',The emploee data is update)
    Clear()
    displayAll()
    

tv.heading("6", text="Gender")
tv.column("6", width="90")
tv.heading("7", text="Mobile")
tv.column("7", width="150")
tv.heading("8", text="Address")
tv.column("8", width="150")
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", getData)
tv.place(x=1 ,y=1,height=610,width=875)

displayAll()
root.mainloop()
                             
