import tkinter as tk
from PIL import Image, ImageTk
import requests

#function to get the weather data for Auckland
def get_weather():
    try:
        lat = "-36.8485"
        lon = "174.7633"
        api_key = "781e8530fe2c57936f1bf49139200eac"
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        
        response = requests.get(url)
        weather_data = response.json()
        
        if response.status_code == 200:
            city = weather_data["name"]
            temperature = weather_data["main"]["temp"]
            description = weather_data["weather"][0]["description"]
            weather_label.config(
                text=f"City: {city}\nTemperature: {temperature}°C\nDescription: {description.capitalize()}"
            )
        else:
            weather_label.config(text="Error fetching weather data")
    except Exception as e:
        weather_label.config(text=f"Error: {str(e)}")

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

def go_home():
    root.destroy()
    import home

#frame for title of the page
title_frame = tk.Frame(root)
title_frame.pack(pady=150)
title_label = tk.Label(
    title_frame, 
    text="Current Weather in Auckland", 
    font=("Arial", 30, "bold")
)
title_label.pack()

#frame for the weather 
weather_frame = tk.Frame(root)
weather_frame.pack(pady=80)
weather_label = tk.Label(weather_frame, text="Grabbing weather...",
                         font=("Arial", 16)
                         )
weather_label.pack()

#frame for the button that gets the weather
button_frame = tk.Frame(root)
button_frame.pack(pady=80)
getweather_button = tk.Button(
button_frame, text="Get Weather",
font=("Arial", 16),
command=get_weather
)
getweather_button.pack()

#takes you back to Home page
back_button = tk.Button(root,
text="Back to Home",
font=("Arial", 14),
command=go_home
)
back_button.pack(pady=20)

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

root.mainloop()