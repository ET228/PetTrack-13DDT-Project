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
                username TEXT NOT NULL,
                date TEXT NOT NULL,
                reminder TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()
    except Exception as e:
        messagebox.showinfo("Error", f"Database initialization error: {str(e)}")

#functions
def save_reminder():
    date = cal.get_date()
    reminder = reminder_entry.get().strip()
    if not reminder:
        messagebox.showinfo("Error", "Please enter a reminder.")
        return
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reminders (username, date, reminder) VALUES (?, ?, ?)",
                       (logged_in_user, date, reminder))
        conn.commit()
        conn.close()
        messagebox.showinfo("Saved", f"Reminder saved for {date}!")
        show_reminders()
    except Exception as e:
        messagebox.showinfo("Error", f"Failed to save reminder: {str(e)}")

def show_reminders(event=None):
    date = cal.get_date()
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        cursor.execute("SELECT reminder FROM reminders WHERE username = ? AND date = ?",
                       (logged_in_user, date))
        results = cursor.fetchall()
        conn.close()
        if results:
            reminders_text = "\n".join([f"- {r[0]}" for r in results])
            reminder_label.config(text=f"Reminders:\n{reminders_text}")
        else:
            reminder_label.config(text="Reminders: (none)")
    except Exception as e:
        reminder_label.config(text=f"Error: {str(e)}")

def go_home():
    root.destroy()
    import home  # return to home screen

#GUI
logged_in_user = get_logged_in_user()
initialize_database()

root = tk.Tk()
root.title("Pet Tracker - Reminders")
root.geometry("800x700")

# Title
title_frame = tk.Frame(root)
title_frame.pack(pady=20)
tk.Label(title_frame, text="Pet Care Reminders", font=("Arial", 28, "bold")).pack()

# Calendar
cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
cal.pack(pady=20)
cal.bind("<<CalendarSelected>>", show_reminders)

# Reminder entry
reminder_entry = tk.Entry(root, width=40, font=("Arial", 14))
reminder_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Save Reminder", font=("Arial", 14), command=save_reminder).pack(side="left", padx=5)
tk.Button(button_frame, text="Back to Home", font=("Arial", 14), command=go_home).pack(side="left", padx=5)

# Label for reminders
reminder_label = tk.Label(root, text="Reminders: ", font=("Arial", 14), justify="left")
reminder_label.pack(pady=20)

# Show today's reminders
show_reminders()

# Logo
try:
    logo_image = tk.PhotoImage(file="images/logo.png").subsample(4, 4)
    logo_label = tk.Label(root, image=logo_image)
    logo_label.place(x=0, y=0)
except:
    print("Logo image not found")

# PETTRACK label
tk.Label(root, text="PETTRACK", font=("Arial", 24, "bold")).place(x=130, y=60)

root.mainloop()