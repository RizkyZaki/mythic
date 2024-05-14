import tkinter as t
from tkinter import messagebox

def handleClickLogin():
    u = username_input.get()
    p = password_input.get()
    print(f"username = {u}")
    print(f"password = {p}")
    if u == "admin" and p == "password":
        print("OK")
        messagebox.showinfo("Login Success", "Welcome, admin!")
    else:
        messagebox.showerror("Login Error", "Wrong username or password")

main = t.Tk()
main.title("Login")

username_label = t.Label(main, text="Username")
username_label.pack()
username_input =t.Entry(main)
username_input.pack()
password_label = t.Label(main, text="Password")
password_label.pack()
password_input =t.Entry(main, show='*')
password_input.pack()
btn = t.Button(main, text="Login COK", command=handleClickLogin)
btn.pack()
main.mainloop()