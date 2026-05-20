from tkinter import *
from tkinter import ttk, messagebox
from auth import register_user, login_user

# Main Window
window = Tk()
window.title("OLX Desktop Clone")
window.geometry("700x500")
window.configure(bg="#f2f2f2")

# Fix for macOS
style = ttk.Style()
style.theme_use("clam")
style.configure("Green.TButton", background="green", foreground="white", font=("Arial", 12, "bold"), padding=10)
style.configure("Blue.TButton", background="blue", foreground="white", font=("Arial", 12, "bold"), padding=10)
style.configure("Orange.TButton", background="orange", foreground="white", font=("Arial", 12, "bold"), padding=10)

try:
    logo = PhotoImage(file="olx_logo.png")
    Label(window, image=logo, bg="#f2f2f2").pack(pady=10)
except:
    pass

Label(window, text="Welcome to the OLX Clone",
      font=("Arial", 22, "bold"), bg="#f2f2f2", fg="darkgreen").pack(pady=20)

# Register
def open_register():
    win = Toplevel(window)
    win.title("Register")
    win.geometry("400x300")

    Label(win, text="Name").pack()
    name = Entry(win, width=30)
    name.pack(pady=5)

    Label(win, text="Email").pack()
    email = Entry(win, width=30)
    email.pack(pady=5)

    Label(win, text="Password").pack()
    password = Entry(win, show="*", width=30)
    password.pack(pady=5)

    def save():
        if name.get() == "" or email.get() == "" or password.get() == "":
            messagebox.showerror("Error", "Fill all fields!")
            return
        success = register_user(name.get(), email.get(), password.get())
        if success:
            messagebox.showinfo("Success", "Registered Successfully!")
            win.destroy()
        else:
            messagebox.showerror("Error", "Email already exists!")

    ttk.Button(win, text="Register", style="Green.TButton", command=save).pack(pady=10)

# Login
def open_login():
    win = Toplevel(window)
    win.title("Login")
    win.geometry("400x250")

    Label(win, text="Email").pack()
    email = Entry(win, width=30)
    email.pack(pady=5)

    Label(win, text="Password").pack()
    password = Entry(win, show="*", width=30)
    password.pack(pady=5)

    def check():
        name = login_user(email.get(), password.get())
        if name:
            messagebox.showinfo("Welcome", f"Welcome, {name}!")
            win.destroy()
        else:
            messagebox.showerror("Error", "Wrong email or password!")

    ttk.Button(win, text="Login", style="Blue.TButton", command=check).pack(pady=10)

# Main Buttons
ttk.Button(window, text="Register", width=20, style="Green.TButton", command=open_register).pack(pady=10)
ttk.Button(window, text="Login", width=20, style="Blue.TButton", command=open_login).pack(pady=10)
ttk.Button(window, text="View Products", width=20, style="Orange.TButton").pack(pady=10)

window.mainloop()