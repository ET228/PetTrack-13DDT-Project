import tkinter as tk

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

#the frame of the header
header = tk.Frame(root, bg="#333")
header.pack(side=tk.TOP, fill=tk.X)

#the text thats on the headr
header_label = tk.Label(header, text="PETTRACK", fg="white", bg="#333")
header_label.pack(side=tk.LEFT, padx=11, pady=5)

#frame for the login box
login_frame = tk.Frame(root)
login_frame.pack(expand=True)

#title
title_label = tk.Label(login_frame, text="PETTRACK", font=("Arial", 30, "bold"))
title_label.grid(row=0, column=1, pady=10)

#username and text box 
tk.Label(login_frame, text="Username").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(login_frame).grid(row=1, column=1, padx=10, pady=10)

#password and textbox
tk.Label(login_frame, text="Password").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(login_frame, show="*").grid(row=2, column=1, padx=10, pady=10)

#login button
tk.Button(login_frame, text="Login").grid(row=3, column=0, columnspan=2, pady=10)

#sign Up button
tk.Button(login_frame, text="Sign Up").grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()