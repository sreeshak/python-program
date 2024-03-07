import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = length_var.get()
    
    if not password_length.isdigit():
        result_var.set("Please enter a valid number.")
        return
    
    password_length = int(password_length)
    
    if password_length <= 0:
        result_var.set("Password length must be greater than 0.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    
    result_var.set(generated_password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and configure widgets
length_label = ttk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

length_var = tk.StringVar()
length_entry = ttk.Entry(root, textvariable=length_var, width=5)
length_entry.grid(row=0, column=1, padx=10, pady=10)

generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_var = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_var, foreground="blue")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()