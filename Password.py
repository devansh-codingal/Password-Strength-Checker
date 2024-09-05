import tkinter as tk
from tkinter import messagebox
import re


# Function to validate the password
def validate_password():
    password = password_var.get()

    # Define the password criteria
    if len(password) < 8:
        messagebox.showwarning("Validation Result", "Password must be at least 8 characters long.")
        return
    if not re.search("[a-z]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one lowercase letter.")
        return
    if not re.search("[A-Z]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one uppercase letter.")
        return
    if not re.search("[0-9]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one digit.")
        return
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        messagebox.showwarning("Validation Result", "Password must contain at least one special character.")
        return

    messagebox.showinfo("Validation Result", "Password is valid!")


# Function to toggle the visibility of the password
def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# Create the main window
root = tk.Tk()
root.title("Password Validator")
root.geometry("300x200")

# Variable to store the entered password
password_var = tk.StringVar()

# Variable for the show password checkbox
show_password_var = tk.BooleanVar()

# Create and place the widgets
label = tk.Label(root, text="Enter Password:")
label.pack(pady=10)

password_entry = tk.Entry(root, textvariable=password_var, width=30, show='*')
password_entry.pack(pady=5)

show_password_check = tk.Checkbutton(root, text="Show Password", variable=show_password_var,
                                     command=toggle_password_visibility)
show_password_check.pack(pady=5)

validate_button = tk.Button(root, text="Validate Password", command=validate_password)
validate_button.pack(pady=5)

# Run the application
root.mainloop()