import tkinter as tk

def go_to_yourpet():
    root.destroy()
    import yourpet

def calendar():
        root.destroy()
        import calender1

def weather():
        root.destroy()
        import weather

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

#logo
try:
    logo_image = tk.PhotoImage(file="images/logo.png")
    logo_image = logo_image.subsample(4, 4)
    logo_label = tk.Label(root, image=logo_image)
    logo_label.place(x=0, y=0)
except:
    print("Logo image not found")

#PETTRACK text next to logo
pettrack_label = tk.Label(root, text="PETTRACK", font=("Arial", 24, "bold"))
pettrack_label.place(x=130, y=60)

#title for PET
title_label_pet = tk.Label(root, text="PET", font=("Arial", 100, "bold"))
title_label_pet.place(x=860, y=350)

#title for TRACK
title_label_track = tk.Label(root, text="TRACK", font=("Arial", 100))
title_label_track.place(x=850, y=450)

#button for "your Pet" and logo next to it
yourpet_button = tk.Button(
    root, text="Your Pet", font=("Arial", 12), command=go_to_yourpet
)
yourpet_button.place(x=1300, y=70)
try:
    yourpet_image = tk.PhotoImage(file="images/yourpet.png")
    yourpet_image = yourpet_image.subsample(6, 6)
    yourpet_label = tk.Label(root, image=yourpet_image)
    yourpet_label.place(x=1200, y=40)
except:
    print("Your pet image not found")

#button for "calendar"
calendar_button = tk.Button(
    root, text="Calendar", font=("Arial", 12), command=calendar
)
calendar_button.place(x=900, y=70)
try:
    calendar_image = tk.PhotoImage(file="images/calendar.png")
    calendar_image = calendar_image.subsample(6, 6)
    calendar_label = tk.Label(root, image=calendar_image)
    calendar_label.place(x=800, y=40)
except:
    print("Calendar image not found")

#button for "weather"
weather_button = tk.Button(
    root, text="Weather", font=("Arial", 12), command=weather
)
weather_button.place(x=500, y=70)
try:
    weather_image = tk.PhotoImage(file="images/weather.png")
    weather_image = weather_image.subsample(6, 6)
    weather_label = tk.Label(root, image=weather_image)
    weather_label.place(x=400, y=40)
except:
    print("Weather image not found")

root.mainloop()