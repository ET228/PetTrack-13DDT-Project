import tkinter as tk
from tkinter import messagebox

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    #checks if its in login
    try:
        with open("login.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(":")
                if username == stored_username and password == stored_password:
                    root.destroy()
                    import home
                    return
        
        #if the user get here, it will show login failed
        messagebox.showinfo("Error", "This account does not exist")
    
    except:
        messagebox.showinfo("Error", "Could not read login file")

def nextpage():
    root.destroy()
    import sign

#header
header = tk.Frame(root, bg="#333")
header.pack(side=tk.TOP, fill=tk.X)
header_label = tk.Label(header, text="PETTRACK", fg="white", bg="#333")
header_label.pack(side=tk.LEFT, padx=11, pady=5)

#Login frame
login_frame = tk.Frame(root)
login_frame.pack(expand=True)

#Title
title_label = tk.Label(login_frame, text="PETTRACK", font=("Arial", 30, "bold"))
title_label.grid(row=0, column=1, pady=10)

#Username
tk.Label(login_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

# Password
tk.Label(login_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

#login button
tk.Button(login_frame, text="Login", command=login).grid(row=3, column=0, columnspan=2, pady=10)

#sign Up button
tk.Button(login_frame, text="Sign Up", command=nextpage).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()