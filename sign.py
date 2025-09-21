import tkinter as tk
from tkinter import messagebox

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

def nextpage():
    root.destroy()
    import login

def signup():
    username = username_entry.get()
    password = password_entry.get()
    
    #Checks if the username already exists
    try:
        username_exists = False
        try:
            with open("login.txt", "r") as file:
                for line in file:
                    stored_username = line.strip().split(":")[0]
                    if username == stored_username:
                        username_exists = True
                        break
        except FileNotFoundError:
            pass
        
        if username_exists:
            messagebox.showinfo("Error", "Username already exists")
            return
        
        with open("login.txt", "a") as file:
            file.write(f"{username}:{password}\n")
        
        messagebox.showinfo("Success", "Account created successfully!")
        nextpage()
        
    except Exception as e:
        messagebox.showinfo("Error", f"An error occurred: {str(e)}")

#the frame of the header
header = tk.Frame(root, bg="#333")
header.pack(side=tk.TOP, fill=tk.X)

#the text thats on the header
header_label = tk.Label(header, text="PETTRACK", fg="white", bg="#333")
header_label.pack(side=tk.LEFT, padx=11, pady=5)

#frame for the signup box
signup_frame = tk.Frame(root)
signup_frame.pack(expand=True)

#title
title_label = tk.Label(signup_frame, text="SIGN UP", font=("Arial", 30, "bold"))
title_label.grid(row=0, column=1, pady=10)

#username and text box 
tk.Label(signup_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
username_entry = tk.Entry(signup_frame)
username_entry.grid(row=1, column=1, padx=10, pady=10)

#password and textbox
tk.Label(signup_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(signup_frame, show="*")
password_entry.grid(row=2, column=1, padx=10, pady=10)

#signup button
tk.Button(signup_frame, text="Sign Up", command=signup).grid(row=3, column=0, columnspan=2, pady=10)

#back to login button
tk.Button(signup_frame, text="Back to Login", command=nextpage).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()