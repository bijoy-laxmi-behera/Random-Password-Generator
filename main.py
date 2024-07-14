import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar, IntVar
import random
import string
import pyperclip

def generate_password(length, use_letters, use_numbers, use_symbols):
    character_set = ''
    
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    if not character_set:
        raise ValueError("No character types selected")
    
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def generate():
    try:
        length = int(length_var.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        
        if length < 1:
            raise ValueError
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid password length and select at least one character type.")

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("No password", "Please generate a password first.")

root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x300")

# Variables
length_var = IntVar(value=12)
letters_var = IntVar(value=1)
numbers_var = IntVar(value=1)
symbols_var = IntVar(value=1)
password_var = StringVar()

# GUI Layout
tk.Label(root, text="Password Length:").pack(pady=5)
tk.Entry(root, textvariable=length_var).pack(pady=5)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack(anchor='w', pady=2)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack(anchor='w', pady=2)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack(anchor='w', pady=2)

tk.Button(root, text="Generate Password", command=generate).pack(pady=10)
tk.Entry(root, textvariable=password_var, state='readonly', width=50).pack(pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Start the main event loop
root.mainloop()
