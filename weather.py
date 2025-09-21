import tkinter as tk
from PIL import Image, ImageTk
import requests

# Function to fetch weather data for Auckland
def fetch_weather():
    try:
        # Latitude and longitude for Auckland
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
            
            # Update the weather label
            weather_label.config(text=f"City: {city}\nTemperature: {temperature}°C\nDescription: {description.capitalize()}")
        else:
            weather_label.config(text="Error fetching weather data")
    except Exception as e:
        weather_label.config(text=f"Error: {str(e)}")

#GUI setup
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")


root.mainloop()
