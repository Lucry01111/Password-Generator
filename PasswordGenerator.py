import tkinter as tk
from tkinter import ttk
import random
import string

def update_label(event):
    """Updates the label with the length of the password selected by the slider."""
    current_value = int(slider_length.get())
    length_var.set(f"Password Length: {current_value}")

def generate_password():
    """Generates a password based on the selected characters and specified length."""
    password_characters = ""
    if var_upper.get():
        password_characters += string.ascii_uppercase
    if var_lower.get():
        password_characters += string.ascii_lowercase
    if var_numbers.get():
        password_characters += string.digits
    if var_special.get():
        password_characters += string.punctuation

    if password_characters:
        length = int(slider_length.get())
        password = ''.join(random.choice(password_characters) for _ in range(length))
        password_var.set(password)
    else:
        password_var.set("Select at least one set of characters")

def create_gui():
    """Creates and configures the graphical user interface."""
    global slider_length, length_var, var_upper, var_lower, var_numbers, var_special, password_var

    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("500x400")
    root.configure(bg="#f0f0f0")

    style = ttk.Style(root)
    style.configure("TLabel", font=('Arial', 12), background="#f0f0f0")
    style.configure("TButton", font=('Arial', 12, 'bold'), padding=6)
    style.configure("TCheckbutton", font=('Arial', 12), background="#f0f0f0")
    style.configure("TScale", background="#f0f0f0")
    style.configure("TEntry", font=('Arial', 12, 'bold'))

    length_var = tk.StringVar(value="Password Length: 8")
    var_upper = tk.BooleanVar(value=False)
    var_lower = tk.BooleanVar(value=False)
    var_numbers = tk.BooleanVar(value=False) 
    var_special = tk.BooleanVar(value=False) 
    password_var = tk.StringVar()

    label_length = ttk.Label(root, textvariable=length_var)
    label_length.pack(pady=10)

    """Password length slider"""
    slider_length = ttk.Scale(root, from_=4, to_=20, orient="horizontal", command=update_label)
    slider_length.set(8)
    slider_length.pack(pady=10)

    frame_checks = ttk.Frame(root, padding="10")
    frame_checks.pack(pady=10)

    check_upper = ttk.Checkbutton(frame_checks, text="Include uppercase", variable=var_upper)
    check_upper.grid(row=0, column=0, sticky="w", padx=10)
    check_lower = ttk.Checkbutton(frame_checks, text="Include lowercase", variable=var_lower)
    check_lower.grid(row=0, column=1, sticky="w", padx=10)
    check_numbers = ttk.Checkbutton(frame_checks, text="Include numbers", variable=var_numbers)
    check_numbers.grid(row=1, column=0, sticky="w", padx=10)
    check_special = ttk.Checkbutton(frame_checks, text="Include special characters", variable=var_special)
    check_special.grid(row=1, column=1, sticky="w", padx=10)

    button_generate = ttk.Button(root, text="Generate Password", command=generate_password)
    button_generate.pack(pady=20)

    entry_password = ttk.Entry(root, textvariable=password_var, font=('Arial', 12, 'bold'), foreground="blue", justify='center')
    entry_password.pack(pady=10)
    entry_password.config(state='readonly')

    root.mainloop()

if __name__ == "__main__":
    create_gui()