import tkinter as tk
from tkinter import messagebox
import sqlite3
from argon2 import PasswordHasher

root = tk.Tk()
root.title("Sign Up")
root.geometry("1500x1500")

ph = PasswordHasher()

def sign_up():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username:
        messagebox.showerror("Error", "Please enter a username")
        return

    if len(password) < 8 or len(password) > 15:
        messagebox.showerror(
            "Error", "Password must be between 8 and 15 characters long"
        )
        return

    conn = sqlite3.connect("pettrack.db")
    cursor = conn.cursor()

    #makes sure that the users table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    #checks if the username input exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        messagebox.showerror("Error", "Username already exists")
        conn.close()
        return

    #Hashes the password and stores it in the database
    hashed_password = ph.hash(password)
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (username, hashed_password)
    )
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Account created successfully")
    root.destroy()
    import login

#GUI
signup_frame = tk.Frame(root)
signup_frame.pack(expand=True)

title_label = tk.Label(
    signup_frame, 
    text="Sign Up", 
    font=("Arial", 30, "bold")
    )
title_label.grid(row=0, column=1, pady=10)

tk.Label(signup_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(signup_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(signup_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(signup_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

tk.Button(signup_frame, text="Sign Up", command=sign_up).grid(
    row=3, column=0, columnspan=2, pady=10
    )

root.mainloop()