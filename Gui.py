from tkinter import *
from tkinter import messagebox
from auth import register_user, login_user
import os

# =========================
# MAIN WINDOW
# =========================

window = Tk()

window.title("OLX Desktop Clone")
window.geometry("700x500")
window.configure(bg="white")

# Prevent resizing
window.resizable(False, False)

# =========================
# MAIN FRAME
# =========================

main_frame = Frame(window, bg="white")
main_frame.pack(expand=True)

# =========================
# LOGO IMAGE
# =========================

current_folder = os.path.dirname(__file__)

logo_path = os.path.join(current_folder, "olx_logo.png")

logo = PhotoImage(file=logo_path)

# Resize image smaller
logo = logo.subsample(3, 3)

logo_label = Label(
    main_frame,
    image=logo,
    bg="white"
)

logo_label.pack(pady=10)

# =========================
# TITLE
# =========================

title = Label(
    main_frame,
    text="Welcome to the OLX Clone",
    font=("Arial", 18, "bold"),
    bg="white",
    fg="darkgreen"
)

title.pack(pady=10)

# =========================
# REGISTER WINDOW
# =========================

def open_register():

    register_window = Toplevel(window)

    register_window.title("Register")

    register_window.geometry("400x400")

    register_window.configure(bg="white")

    register_window.resizable(False, False)

    # Heading
    heading = Label(
        register_window,
        text="Create Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="darkgreen"
    )

    heading.pack(pady=15)

    # =========================
    # NAME
    # =========================

    Label(
        register_window,
        text="Name",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    name_entry = Entry(
        register_window,
        width=30,
        font=("Arial", 11)
    )

    name_entry.pack(pady=5)

    # =========================
    # EMAIL
    # =========================

    Label(
        register_window,
        text="Email",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    email_entry = Entry(
        register_window,
        width=30,
        font=("Arial", 11)
    )

    email_entry.pack(pady=5)

    # =========================
    # PASSWORD
    # =========================

    Label(
        register_window,
        text="Password",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    password_entry = Entry(
        register_window,
        width=30,
        font=("Arial", 11),
        show="*"
    )

    password_entry.pack(pady=5)

    # =========================
    # SAVE USER FUNCTION
    # =========================

    def save_user():

        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        # Validation
        if name == "" or email == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )
            return

        register_user(name, email, password)

        messagebox.showinfo(
            "Success",
            "User Registered Successfully"
        )

    # =========================
    # REGISTER BUTTON
    # =========================

    register_button = Label(
        register_window,
        text="Register",
        bg="green",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    register_button.pack(pady=15)

    register_button.bind(
        "<Button-1>",
        lambda e: save_user()
    )

# =========================
# LOGIN WINDOW
# =========================

def open_login():

    login_window = Toplevel(window)

    login_window.title("Login")

    login_window.geometry("400x350")

    login_window.configure(bg="white")

    login_window.resizable(False, False)

    # =========================
    # HEADING
    # =========================

    heading = Label(
        login_window,
        text="Login To Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="darkblue"
    )

    heading.pack(pady=20)

    # =========================
    # EMAIL
    # =========================

    Label(
        login_window,
        text="Email",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    email_entry = Entry(
        login_window,
        width=30,
        font=("Arial", 11)
    )

    email_entry.pack(pady=5)

    # =========================
    # PASSWORD
    # =========================

    Label(
        login_window,
        text="Password",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    password_entry = Entry(
        login_window,
        width=30,
        font=("Arial", 11),
        show="*"
    )

    password_entry.pack(pady=5)

    # =========================
    # LOGIN FUNCTION
    # =========================

    def login_user_gui():

        email = email_entry.get()
        password = password_entry.get()

        # Validation
        if email == "" or password == "":
            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )
            return

        # Database Login
        user = login_user(email, password)

        if user:

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

        else:

            messagebox.showerror(
                "Error",
                "Invalid Email or Password"
            )

    # =========================
    # LOGIN BUTTON
    # =========================

    login_button = Label(
        login_window,
        text="Login",
        bg="darkblue",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    login_button.pack(pady=20)

    login_button.bind(
        "<Button-1>",
        lambda e: login_user_gui()
    )

# =========================
# MAIN WINDOW BUTTONS
# =========================

# =========================
# REGISTER BUTTON
# =========================

register_btn = Label(
    main_frame,
    text="Register",
    bg="green",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)

register_btn.pack(pady=10)

register_btn.bind(
    "<Button-1>",
    lambda e: open_register()
)

# =========================
# LOGIN BUTTON
# =========================

login_btn = Label(
    main_frame,
    text="Login",
    bg="darkblue",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)

login_btn.pack(pady=10)

login_btn.bind(
    "<Button-1>",
    lambda e: open_login()
)

# =========================
# VIEW PRODUCTS BUTTON
# =========================

view_btn = Label(
    main_frame,
    text="View Products",
    bg="orange",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)

view_btn.pack(pady=10)

# =========================
# RUN WINDOW
# =========================

window.mainloop()