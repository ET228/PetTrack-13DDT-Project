import tkinter as tk
from PIL import Image, ImageTk

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

#logo
logo_image = tk.PhotoImage(file="images/logo.png")
logo_image = logo_image.subsample(4, 4)
logo_label = tk.Label(root, image=logo_image)
logo_label.place(x=0, y=0)

#title for PET (didnt work with the other title)
#title_label = tk.Label(root, text="PET", font=("Arial", 100, "bold"))
#title_label.grid(row=5, column=10, padx=750, pady=300)

#title for TRACK (didnt work with the other title)
#title_label = tk.Label(root, text="TRACK", font=("Arial", 100))
#title_label.grid(row=6, column=10, padx=1000, pady=1)

#title for PET
title_label_pet = tk.Label(root, text="PET", font=("Arial", 100, "bold"))
title_label_pet.place(x=860, y=300)

#title for TRACK
title_label_track = tk.Label(root, text="TRACK", font=("Arial", 100))
title_label_track.place(x=850, y=400)

#button for "your account"
account_button = tk.Button(root, text="Your Account", font=("Arial", 12))
account_button.place(x=1300, y=70)

#button for "calender"
account_button = tk.Button(root, text="Calendar", font=("Arial", 12))
account_button.place(x=1000, y=70)

#button for "weather"
account_button = tk.Button(root, text="Weather", font=("Arial", 12))
account_button.place(x=700, y=70)

root.mainloop()