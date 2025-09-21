import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import sqlite3

#database
def get_logged_in_user():
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM current_user LIMIT 1")
        user = cursor.fetchone()
        conn.close()
        return user[0] if user else None
    except Exception as e:
        print(f"Error getting logged in user: {e}")
        return None

def initialize_database():
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TE


root = tk.Tk()
root.title("Pet Tracker Reminders")
root.geometry("1500x1500")


root.mainloop()
