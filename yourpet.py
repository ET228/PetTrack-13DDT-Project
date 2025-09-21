import tkinter as tk
from tkinter import messagebox

#reads who is logged in
try:
    with open("current_user.txt", "r") as file:
        logged_in_user = file.read().strip()
except:
    logged_in_user = "current_user"

#function to go back to home page
def go_to_home():
    try:
        root.destroy()
        import home
    except Exception as e:
        print(f"Error opening Home page: {e}")

#saves pet info
def save_pet_info():
    try:
        pet_info = f"{logged_in_user}:Name={name_entry.get()},Age={age_var.get()},Breed={breed_entry.get()},Weight={weight_entry.get()},Food={food_var.get()}\n"
        updated_lines = []
        user_found = False
        
        try:
            with open("petinfo.txt", "r") as file:
                for line in file:
                    if line.startswith(logged_in_user + ":"):
                        updated_lines.append(pet_info)
                        user_found = True
                    else:
                        updated_lines.append(line)
        except FileNotFoundError:
            updated_lines = []
        
        if not user_found:
            updated_lines.append(pet_info)
        
        with open("petinfo.txt", "w") as file:
            file.writelines(updated_lines)
        
        messagebox.showinfo("Saved", "Pet information saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save pet information: {str(e)}")

#shows pet info on page
def load_pet_info():
    try:
        with open("petinfo.txt", "r") as file:
            for line in file:
                if line.startswith(logged_in_user + ":"):
                    data = line.strip().split(":", 1)[1]
                    info = dict(item.split("=", 1) for item in data.split(","))
                    
                    # Clear entries first
                    name_entry.delete(0, tk.END)
                    breed_entry.delete(0, tk.END)
                    weight_entry.delete(0, tk.END)
                    
                    # Load data
                    name_entry.insert(0, info.get("Name", ""))
                    age_var.set(info.get("Age", "Select Age"))
                    breed_entry.insert(0, info.get("Breed", ""))
                    weight_entry.insert(0, info.get("Weight", ""))
                    food_var.set(info.get("Food", "Amount"))
                    break
    except Exception as e:
        print(f"Could not load pet info: {e}")

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

#button for Home and logo next to it
home_button = tk.Button(root, text="Home", font=("Arial", 12), command=go_to_home)
home_button.place(x=1400, y=70)

#both titles
your_pet_title = tk.Label(root, text="Your Pet", font=("Arial", 100, "bold"))
your_pet_title.place(x=500, y=100)

your_pet_title = tk.Label(root, text="Pets information", font=("Arial", 20, "bold"))
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

#weight label and text box
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
save_button = tk.Button(root, text="Save", font=("Arial", 16), command=save_pet_info)
save_button.place(x=650, y=650)

#loads the pet info when the page open
load_pet_info()

root.mainloop()
