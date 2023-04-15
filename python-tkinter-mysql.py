from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
#def hello(): print ('Hello, world')
def insert():
    id = e_id.get();
    name = e_name.get();
    phone = e_phone.get();
    bill = e_bill.get();

    if(id=="" or name=="" or phone=="" or bill==""):
        MessageBox.showinfo("Insert Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("insert into customer values('"+ id +"','"+ name +"','"+ phone +"','"+ bill +"')")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully!")
        con.close();

def delete():
    if(e_id.get() == "" ):
        MessageBox.showinfo("Delete Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("delete from customer where id='"+ e_id.get() +"'")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully!")
        con.close();

def update():
    id = e_id.get();
    name = e_name.get();
    phone = e_phone.get();
    bill = e_bill.get();

    if(id=="" or name=="" or phone=="" or bill==""):
        MessageBox.showinfo("Update Status", "All Fields are Required!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("update customer set name='"+ name +"', phone='"+ phone +"', bill='"+ bill +"' where id='"+ id +"'")
        cursor.execute("commit");
        e_id.delete(0, 'end')
        e_name.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_bill.delete(0, 'end')
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully!")
        con.close();

def get():
    if(e_id.get() == "" ):
        MessageBox.showinfo("Fetch Status", "You need to specify ID!")
    else:
        con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("select * from customer where id='"+ e_id.get() +"'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])
            e_phone.insert(0, row[2])
            e_bill.insert(0, row[3])
            
        con.close();

def show():
    con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
    cursor = con.cursor()
    cursor.execute("select * from customer")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row[0])+'      '+ row[1]#+ int(row[2])+'     '
        list.insert(list.size()+1, insertData)

    con.close();
    
root = Tk()
root.geometry('600x300')
root.title('Customer Records');

id = Label(root, text='Enter ID',font=('bold',10))
id.place(x=20,y=30)

name = Label(root, text='Enter Name',font=('bold',10))
name.place(x=20,y=60)

phone = Label(root, text='Enter Phone',font=('bold',10))
phone.place(x=20,y=90)

bill = Label(root, text='Enter Pending Bills',font=('bold',10))
bill.place(x=20,y=120)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

e_phone = Entry()
e_phone.place(x=150, y=90)

e_bill = Entry()
e_bill.place(x=150, y=120)

insert = Button(root, text="Insert", font=("italic", 10), bg="green", command=insert)
insert.place(x=20, y=160)

delete = Button(root, text="Delete", font=("italic", 10), bg="gold", command=delete)
delete.place(x=90, y=160)

update = Button(root, text="Update", font=("italic", 10), bg="red", command=update)
update.place(x=160, y=160)

get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=240, y=160)

list = Listbox(root)
list.place(x=290, y=30)
show()

















#btn = Button(root, text='Hello ', command=hello)
#btn.pack(padx=100, pady=100)
mainloop()
