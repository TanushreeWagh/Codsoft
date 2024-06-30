import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_numbers else ''
    special = string.punctuation if use_special else ''

    all_characters = lower + upper + digits + special

    if len(all_characters) == 0:
        raise ValueError("No character types selected for password generation")

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def generate():
    try:
        length = int(entry_length.get())
        use_uppercase = var_uppercase.get()
        use_numbers = var_numbers.get()
        use_special = var_special.get()
        
        password = generate_password(length, use_uppercase, use_numbers, use_special)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

root = tk.Tk()
root.title("Password Generator")

label_length = tk.Label(root, text="Password Length:")
label_length.grid(row=0, column=0, padx=20, pady=20)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=2, padx=20, pady=20)

var_uppercase = tk.BooleanVar(value=True)
check_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase)
check_uppercase.grid(row=1, columnspan=4, padx=20, pady=10)

var_numbers = tk.BooleanVar(value=True)
check_numbers = tk.Checkbutton(root, text="Include Numbers", variable=var_numbers)
check_numbers.grid(row=2, columnspan=4, padx=20, pady=10)

var_special = tk.BooleanVar(value=True)
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special)
check_special.grid(row=3, columnspan=4, padx=20, pady=10)

button_generate = tk.Button(root, text="Generate Password", command=generate)
button_generate.grid(row=4, columnspan=4, padx=20, pady=20)

entry_password = tk.Entry(root, width=80)
entry_password.grid(row=5, columnspan=4, padx=20, pady=20)

root.mainloop()
