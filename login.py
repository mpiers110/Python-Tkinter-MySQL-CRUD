import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os, sys
import mysql.connector as mysql

def challenge():
    con = mysql.connect(host="localhost", user="root", password="", database="python-tkinter")
    cursor = con.cursor()
    user = str(combo1.get())

    if user == "Debby":
        cursor.execute(f"select password from user where name='{id_entry.get()}'")
        cursor = list(cursor)
        if len(cursor) == 0:
            messagebox.showwarning('Bad id', 'No such user found!')
        elif passw_entry.get() != cursor[0][0]:
            messagebox.showerror('Bad pass', 'Incorrect Password!')
        else:
            m.destroy()
            os.system('py python-tkinter-mysql.py')
            
    elif user == "Admin":
        cursor.execute(f"select password from admin where username='{id_entry.get()}'")
        cursor = list(cursor)
        if len(cursor) == 0:
            messagebox.showwarning('Bad id', 'No such user found!')
        elif passw_entry.get() != cursor[0][0]:
            messagebox.showerror('Bad pass', 'Incorrect Password!')
        else:
            m.destroy()
            os.system('py python-tkinter-mysql.py')
        
m = tk.Tk()

m.geometry('620x400')
m.title('DEBBYDASH COMPUTER SERVICES')

tk.Label(
    m,
    text='DebbyDash Sales Records System',
    bg='green',
    fg=('white'),
    relief=("solid"),
    font=('Cooper Black', 18, 'bold'),
    #wrap=400
).pack(padx=90,pady=20)

tk.Label(
    m,
    text='Welcome!\nLogin to continue',
    font=('Cooper Black', 12, 'italic')
).pack(pady=10)

tk.Label(
    m,
    text='Username',
    font=('Cooper Black', 15)
).pack()

id_entry = tk.Entry(
    m,
    font=('Times New Roman', 12),
    width=21
)
id_entry.pack()

# Label5
tk.Label(
    m,
    text='Password:',
    font=('Cooper Black', 15)
).pack()

# toggles between show/hide password
def show_passw():
    if passw_entry['show'] == "●":
        passw_entry['show'] = ""
        B1_show['text'] = '●'
        B1_show.update()
    elif passw_entry['show'] == "":
        passw_entry['show'] = "●"
        B1_show['text'] = '○'
        B1_show.update()
    passw_entry.update()

pass_entry_f = tk.Frame()
pass_entry_f.pack()
# Entry2
passw_entry = tk.Entry(
    pass_entry_f,
    font=('Times New Roman', 12),
    width=15,
    show="●"
)
passw_entry.pack(side=tk.LEFT)

B1_show = tk.Button(
    pass_entry_f,
    text='○',
    font=('Consolas', 12, 'bold'),
    command=show_passw,
    padx=5
)
B1_show.pack(side=tk.LEFT, padx=15)

combo1 = ttk.Combobox(
    m,
    values=['Debby', 'Admin']
)
combo1.pack(pady=15)
combo1.current(0)

tk.Button(
    m,
    text='Login',
    bg='green',
    fg=('black'),
    font=('Cooper Black', 12, 'bold'),
    padx=30,
    command=challenge
).pack(pady=10)

m.mainloop()

