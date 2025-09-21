import tkinter as tk
from tkinter import messagebox
import sqlite3

#gets the currently logged in user from the database
def get_logged_in_user():
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM current_user LIMIT 1")
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return user[0]
        else:
            return "current_user"
    except Exception as e:
        print(f"Error getting logged in user: {str(e)}")
        return "current_user"

#gets the logged in user
logged_in_user = get_logged_in_user()

#initialises the pet_info table in the database
def initialize_database():
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        
        #createsn the pet_info table if it doesnt exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS pet_info (
            username TEXT PRIMARY KEY,
            pet_name TEXT,
            pet_age TEXT,
            pet_breed TEXT,
            pet_weight TEXT,
            pet_food TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        )
        ''')
        
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database initialisation error: {str(e)}")
        messagebox.showinfo("Error", f"Database initialisation error: {str(e)}")

#saves pet info
def save_pet_info():
    try:
        pet_name = name_entry.get()
        pet_age = age_var.get()
        pet_breed = breed_entry.get()
        pet_weight = weight_entry.get()
        pet_food = food_var.get()
        
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        
        #checks if user already has their pets info in the database
        cursor.execute(
            "SELECT * FROM pet_info WHERE username = ?", 
            (logged_in_user,)
            )
        existing_info = cursor.fetchone()
        
        if existing_info:
            #updates the users existing information
            cursor.execute('''
            UPDATE pet_info 
            SET pet_name = ?, pet_age = ?, pet_breed = ?, pet_weight = ?, pet_food = ?
            WHERE username = ?
            ''', (pet_name, pet_age, pet_breed, pet_weight, pet_food, logged_in_user))
        else:
            #puts new information in the database
            cursor.execute('''
            INSERT INTO pet_info (username, pet_name, pet_age, pet_breed, pet_weight, pet_food)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (logged_in_user, pet_name, pet_age, pet_breed, pet_weight, pet_food))
        
        conn.commit()
        conn.close()
        
        messagebox.showinfo("Saved", "Pet information saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save pet information: {str(e)}")

#shows pet info on the GUI
def load_pet_info():
    try:
        conn = sqlite3.connect('pettrack.db')
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT pet_name, pet_age, pet_breed, pet_weight, pet_food 
        FROM pet_info 
        WHERE username = ?
        ''', (logged_in_user,))
        
        pet_data = cursor.fetchone()
        conn.close()
        
        if pet_data:
            name_entry.delete(0, tk.END)
            breed_entry.delete(0, tk.END)
            weight_entry.delete(0, tk.END)
            
            name_entry.insert(0, pet_data[0] if pet_data[0] else "")
            age_var.set(pet_data[1] if pet_data[1] else "Select Age")
            breed_entry.insert(0, pet_data[2] if pet_data[2] else "")
            weight_entry.insert(0, pet_data[3] if pet_data[3] else "")
            food_var.set(pet_data[4] if pet_data[4] else "Amount")
    except Exception as e:
        print(f"Could not load pet info: {e}")

#GUI
root = tk.Tk()
root.title("Pet Tracker")
root.geometry("1500x1500")

#initialises the database
initialize_database()

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

#both titles
your_pet_title = tk.Label(root, text="Your Pet", font=("Arial", 100, "bold"))
your_pet_title.place(x=500, y=100)

your_pet_title = tk.Label(root, 
                          text="Pets information", 
                          font=("Arial", 20, "bold")
                          )
your_pet_title.place(x=650, y=250)

#name label and text box
name_label = tk.Label(root, text="Name:", font=("Arial", 16))
name_label.place(x=550, y=350)
name_entry = tk.Entry(root, font=("Arial", 16))
name_entry.place(x=650, y=350)

#age label and dropdown menu
age_label = tk.Label(root, text="Age:", font=("Arial", 16))
age_label.place(x=550, y=400)
age_var = tk.StringVar(root)
age_var.set("Select Age")
age_options = [str(i) for i in range(1, 21)]
age_dropdown = tk.OptionMenu(root, age_var, *age_options)
age_dropdown.config(font=("Arial", 14))
age_dropdown.place(x=650, y=400)

#breed label and text box
breed_label = tk.Label(root, text="Breed:", font=("Arial", 16))
breed_label.place(x=550, y=450)
breed_entry = tk.Entry(root, font=("Arial", 16))
breed_entry.place(x=650, y=450)

# weight label and text box
weight_label = tk.Label(root, text="Weight(kg):", font=("Arial", 16))
weight_label.place(x=550, y=500)
weight_entry = tk.Entry(root, font=("Arial", 16))
weight_entry.place(x=650, y=500)

#cups of food per meal label and dropdown menu
food_label = tk.Label(root, text="Cups of Food per Meal:", font=("Arial", 16))
food_label.place(x=450, y=550)
food_var = tk.StringVar(root)
food_var.set("Amount")
food_options = [str(i) for i in range(1, 6)]
food_dropdown = tk.OptionMenu(root, food_var, *food_options)
food_dropdown.config(font=("Arial", 14))
food_dropdown.place(x=650, y=550)

#save button
save_button = tk.Button(
    root, 
    text="Save", 
    font=("Arial", 16), 
    command=save_pet_info
    )
save_button.place(x=650, y=650)

#loads the pet info when the page open
load_pet_info()

root.mainloop()