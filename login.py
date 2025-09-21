import tkinter as tk
from tkinter import messagebox
import sqlite3

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    #checks if the username and password match to whats in the DB
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        
        if user:
            #saves who is logged in to the database
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS current_user (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL
            )
            ''')
            cursor.execute("DELETE FROM current_user")  #clears the last user
            cursor.execute("INSERT INTO current_user (username) VALUES (?)", (username,))
            conn.commit()
            conn.close()
            
            #takes you to the home page
            root.destroy()
            import home
        else:
            messagebox.showinfo("Error", "Invalid username or password")
            conn.close()
    except Exception as e:
        print(f"Error during login: {str(e)}")
        messagebox.showinfo("Error", f"Database error: {str(e)}")

def nextpage():
    root.destroy()
    import sign

#header
header = tk.Frame(root, bg="#333")
header.pack(side=tk.TOP, fill=tk.X)
header_label = tk.Label(header, text="PETTRACK", fg="white", bg="#333")
header_label.pack(side=tk.LEFT, padx=11, pady=5)

#login frame
login_frame = tk.Frame(root)
login_frame.pack(expand=True)

#title
title_label = tk.Label(login_frame, text="PETTRACK", font=("Arial", 30, "bold"))
title_label.grid(row=0, column=1, pady=10)

#username
tk.Label(login_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

#password
tk.Label(login_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

#login button
tk.Button(login_frame, text="Login", command=login).grid(row=3, column=0, columnspan=2, pady=10)

#sign up button
tk.Button(login_frame, text="Sign Up", command=nextpage).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()