import tkinter as tk
from tkinter import messagebox
import sqlite3
from argon2 import PasswordHasher

root = tk.Tk()
root.title("Pet Tracker Login")
root.geometry("1500x1500")

ph = PasswordHasher()

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    conn = sqlite3.connect("pettrack.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?", (username,)
    )
    result = cursor.fetchone()

    if result is None:
        messagebox.showerror(
            "Login Failed", "Incorrect username or password. Please try again."
            )
        conn.close()
        return

    stored_password = result[0]

    try:
        ph.verify(stored_password, password)

        #tracks who the current user is
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS current_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL
            )
        """)
        cursor.execute("DELETE FROM current_user")
        cursor.execute("INSERT INTO current_user (username) VALUES (?)", (username,))
        conn.commit()
        conn.close()

        #goes to home page
        root.destroy()
        import home

    except:
        messagebox.showerror(
            "Login Failed", "Incorrect username or password. Please try again."
            )
        conn.close()

def nextpage():
    root.destroy()
    import sign

#GUI
header = tk.Frame(root, bg="#333")
header.pack(side=tk.TOP, fill=tk.X)
header_label = tk.Label(header, text="PETTRACK", fg="white", bg="#333")
header_label.pack(side=tk.LEFT, padx=11, pady=5)

login_frame = tk.Frame(root)
login_frame.pack(expand=True)

title_label = tk.Label(
    login_frame, 
    text="PETTRACK", 
    font=("Arial", 30, "bold"))
title_label.grid(row=0, column=1, pady=10)

tk.Label(login_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(login_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(login_frame, text="Login", command=login).grid(
    row=3, 
    column=0, 
    columnspan=2, 
    pady=10)
tk.Button(login_frame, text="Sign Up", command=nextpage).grid(
    row=4, 
    column=0, 
    columnspan=2, 
    pady=10)

root.mainloop()