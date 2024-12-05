

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
                             