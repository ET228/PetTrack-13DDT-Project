import tkinter as tk
from tkinter import messagebox
import sqlite3

#GUI
root = tk.Tk()
root.title("Sign Up")
root.geometry("1500x1500")

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    
    #adds the user to the database
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        
        #checks if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            messagebox.showinfo("Error", "Username already exists")
        else:
            #puts the new user into the database
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Account created successfully")
            root.destroy()
            import login  #takes you to the login page
    except Exception as e:
        print(f"Error during sign-up: {str(e)}")
        messagebox.showinfo("Error", f"Database error: {str(e)}")

#sign up frame
signup_frame = tk.Frame(root)
signup_frame.pack(expand=True)

#header
header = tk.Frame(root, bg="#333")
header.pack(side=tk.TOP, fill=tk.X)
header_label = tk.Label(header, text="PETTRACK", fg="white", bg="#333")
header_label.pack(side=tk.LEFT, padx=11, pady=5)

#title
title_label = tk.Label(signup_frame, text="Sign Up", font=("Arial", 30, "bold"))
title_label.grid(row=0, column=1, pady=10)

#username
tk.Label(signup_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(signup_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

#password
tk.Label(signup_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(signup_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

#sign up button
tk.Button(signup_frame, text="Sign Up", command=sign_up).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()