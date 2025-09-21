PETTRACK

Purpose of the Program
The purpose of PETTRACK is to provide pet owners with a single place to organise and manage their pet’s care. By combining pet information, reminders, and weather tracking, the app makes it easier to plan routines and ensure pets receive consistent care.

Features
User Accounts – sign up and log in securely (passwords are hashed using Argon2).
Pet Info Tracking – record and update details about your pet.
Calendar with Reminders – add and view daily reminders.
Weather Integration – fetch live weather updates for Auckland via OpenWeather API.
User-Friendly GUI – clean interface with images and clear navigation.

Tech Stack
Python
Tkinter – GUI framework
SQLite3 – local database for storing user, pet, and reminder data
Argon2 – password hashing for secure login
Requests – fetches live weather data from OpenWeather API
Tkcalendar – calendar widget

How to Run
1. Make sure you have Python 3.x installed.
2. Install the required packages (for example via pip):
3. pip install tkcalendar requests argon2-cffi pillow
4. Place the "images" folder in the project root with the required icons (logo, calendar, weather, etc).
Run the app by starting from the login page:
python login.py
5. From there, you can sign up, log in, and navigate to the Home screen, where you can access:
Your Pet Information
Calendar and Reminders
Weather Tracker

Database
The app uses an SQLite database (pettrack.db) to store:
User accounts
Current logged-in user
Pet information
Reminders