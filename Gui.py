from tkinter import *
from tkinter import messagebox
from auth import register_user, login_user, delete_user
from product import add_product, get_products
import os

# =========================
# MAIN WINDOW
# =========================

window = Tk()

window.title("OLX Desktop Clone")
window.geometry("700x550")
window.configure(bg="white")

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
    font=("Arial", 20, "bold"),
    bg="white",
    fg="darkgreen"
)

title.pack(pady=10)

# =========================
# DASHBOARD WINDOW
# =========================

def open_dashboard(user):

    dashboard = Toplevel(window)

    dashboard.title("Dashboard")

    dashboard.geometry("550x450")

    dashboard.configure(bg="#f5f5f5")

    dashboard.resizable(False, False)

    user_name = user[1]
    user_email = user[2]

    # Welcome Label

    welcome_label = Label(
        dashboard,
        text=f"Welcome, {user_name}",
        font=("Arial", 22, "bold"),
        bg="#f5f5f5",
        fg="darkgreen"
    )

    welcome_label.pack(pady=25)

    # Subtitle

    subtitle = Label(
        dashboard,
        text="Manage Your Products Easily",
        font=("Arial", 11),
        bg="#f5f5f5",
        fg="gray"
    )

    subtitle.pack()

    # Email

    email_label = Label(
        dashboard,
        text=f"Email: {user_email}",
        font=("Arial", 12),
        bg="#f5f5f5",
        fg="gray"
    )

    email_label.pack(pady=15)

    # =========================
    # ADD PRODUCT BUTTON
    # =========================

    add_product_btn = Label(
        dashboard,
        text="Add Product",
        bg="orange",
        fg="white",
        font=("Arial", 12, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    add_product_btn.pack(pady=10)

    add_product_btn.bind(
        "<Button-1>",
        lambda e: open_add_product(user)
    )

    # =========================
    # VIEW PRODUCTS BUTTON
    # =========================

    view_products_btn = Label(
        dashboard,
        text="View Products",
        bg="darkblue",
        fg="white",
        font=("Arial", 12, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    view_products_btn.pack(pady=10)

    view_products_btn.bind(
        "<Button-1>",
        lambda e: open_products_window()
    )

    # =========================
    # LOGOUT BUTTON
    # =========================

    logout_btn = Label(
        dashboard,
        text="Logout",
        bg="red",
        fg="white",
        font=("Arial", 12, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    logout_btn.pack(pady=25)

    logout_btn.bind(
        "<Button-1>",
        lambda e: dashboard.destroy()
    )

# =========================
# ADD PRODUCT WINDOW
# =========================

def open_add_product(user):

    add_window = Toplevel(window)

    add_window.title("Add Product")

    add_window.geometry("500x550")

    add_window.configure(bg="#f5f5f5")

    add_window.resizable(False, False)

    seller_name = user[1]

    # Heading

    heading = Label(
        add_window,
        text="Add New Product",
        font=("Arial", 20, "bold"),
        bg="#f5f5f5",
        fg="darkgreen"
    )

    heading.pack(pady=20)

    # Seller

    seller_label = Label(
        add_window,
        text=f"Seller: {seller_name}",
        font=("Arial", 12),
        bg="#f5f5f5",
        fg="gray"
    )

    seller_label.pack(pady=5)

    # Product Title

    title_label = Label(
        add_window,
        text="Product Title",
        font=("Arial", 12, "bold"),
        bg="#f5f5f5"
    )

    title_label.pack()

    title_entry = Entry(
        add_window,
        width=40,
        font=("Arial", 11)
    )

    title_entry.pack(pady=5)

    # Price

    price_label = Label(
        add_window,
        text="Price",
        font=("Arial", 12, "bold"),
        bg="#f5f5f5"
    )

    price_label.pack()

    price_entry = Entry(
        add_window,
        width=40,
        font=("Arial", 11)
    )

    price_entry.pack(pady=5)

    # Description

    desc_label = Label(
        add_window,
        text="Description",
        font=("Arial", 12, "bold"),
        bg="#f5f5f5"
    )

    desc_label.pack()

    desc_text = Text(
        add_window,
        width=40,
        height=6,
        font=("Arial", 11)
    )

    desc_text.pack(pady=5)

    # Save Product

    def save_product():

        title = title_entry.get()
        price = price_entry.get()
        description = desc_text.get("1.0", END)

        if title == "" or price == "" or description.strip() == "":

            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )

            return

        add_product(title, price, description, seller_name)

        messagebox.showinfo(
            "Success",
            "Product Added Successfully"
        )

        add_window.destroy()

    # Save Button

    save_btn = Label(
        add_window,
        text="Save Product",
        bg="green",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    save_btn.pack(pady=20)

    save_btn.bind(
        "<Button-1>",
        lambda e: save_product()
    )

# =========================
# VIEW PRODUCTS WINDOW
# =========================

def open_products_window():

    products_window = Toplevel(window)

    products_window.title("All Products")

    products_window.geometry("750x600")

    products_window.configure(bg="#f0f2f5")

    products_window.resizable(False, False)

    # TOP FRAME

    top_frame = Frame(
        products_window,
        bg="#f0f2f5"
    )

    top_frame.pack(fill="x", pady=10)

    # Back Button

    back_btn = Label(
        top_frame,
        text="← Back",
        bg="#f0f2f5",
        fg="darkblue",
        font=("Arial", 12, "bold"),
        cursor="hand2"
    )

    back_btn.pack(side="left", padx=20)

    # Heading

    heading = Label(
        top_frame,
        text="All Products",
        font=("Arial", 22, "bold"),
        bg="#f0f2f5",
        fg="darkgreen"
    )

    heading.pack()

    # Subtitle

    subtitle = Label(
        products_window,
        text="Browse All Available Products",
        font=("Arial", 11),
        bg="#f0f2f5",
        fg="gray"
    )

    subtitle.pack()

    # =========================
    # SEARCH FRAME
    # =========================

    search_frame = Frame(
        products_window,
        bg="#f0f2f5"
    )

    search_frame.pack(pady=15)

    search_entry = Entry(
        search_frame,
        width=35,
        font=("Arial", 12),
        bd=2,
        relief="groove"
    )

    search_entry.grid(row=0, column=0, padx=10)

    search_btn = Label(
        search_frame,
        text="Search",
        bg="darkblue",
        fg="white",
        font=("Arial", 11, "bold"),
        width=15,
        height=2,
        cursor="hand2"
    )

    search_btn.grid(row=0, column=1)

    # =========================
    # SCROLLABLE AREA
    # =========================

    canvas = Canvas(
        products_window,
        bg="#f0f2f5",
        highlightthickness=0
    )

    scrollbar = Scrollbar(
        products_window,
        orient="vertical",
        command=canvas.yview
    )

    scrollable_frame = Frame(
        canvas,
        bg="#f0f2f5"
    )

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (0, 0),
        window=scrollable_frame,
        anchor="nw"
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True,
        padx=10
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # =========================
    # SHOW PRODUCTS FUNCTION
    # =========================

    def show_products(search_text=""):

        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        products = get_products()

        found = False

        row = 0
        col = 0

        for product in products:

            title = product[1]
            price = product[2]
            description = product[3]
            seller = product[4]

            if search_text.lower() not in title.lower():
                continue

            found = True

            # Product Card

            card = Frame(
                scrollable_frame,
                bg="white",
                bd=2,
                relief="ridge",
                padx=10,
                pady=10,
                width=300,
                height=220
            )

            card.grid(
                row=row,
                column=col,
                padx=15,
                pady=15
            )

            card.grid_propagate(False)

            # Title

            title_label = Label(
                card,
                text=title,
                font=("Arial", 16, "bold"),
                bg="white",
                fg="#1b5e20",
                wraplength=250,
                justify="left"
            )

            title_label.pack(anchor="w")

            # Price

            price_label = Label(
                card,
                text=f"Rs. {price}",
                font=("Arial", 14, "bold"),
                bg="white",
                fg="#0d47a1"
            )

            price_label.pack(anchor="w", pady=5)

            # Description

            desc_label = Label(
                card,
                text=description,
                font=("Arial", 10),
                bg="white",
                fg="#333333",
                wraplength=250,
                justify="left"
            )

            desc_label.pack(anchor="w", pady=5)

            # Seller

            seller_label = Label(
                card,
                text=f"Seller: {seller}",
                font=("Arial", 10, "italic"),
                bg="white",
                fg="gray"
            )

            seller_label.pack(anchor="w", pady=5)

            col += 1

            if col == 2:
                col = 0
                row += 1

        if found == False:

            no_product = Label(
                scrollable_frame,
                text="No Products Found",
                font=("Arial", 15, "bold"),
                bg="#f0f2f5",
                fg="red"
            )

            no_product.pack(pady=30)

    # Search Button

    search_btn.bind(
        "<Button-1>",
        lambda e: show_products(search_entry.get())
    )

    # Back Button

    back_btn.bind(
        "<Button-1>",
        lambda e: (
            search_entry.delete(0, END),
            show_products()
        )
    )

    show_products()

# =========================
# REGISTER WINDOW
# =========================

def open_register():

    register_window = Toplevel(window)

    register_window.title("Register")

    register_window.geometry("400x400")

    register_window.configure(bg="white")

    register_window.resizable(False, False)

    heading = Label(
        register_window,
        text="Create Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="darkgreen"
    )

    heading.pack(pady=15)

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

    def save_user():

        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()

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

        register_window.destroy()

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

    register_button.pack(pady=20)

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

    heading = Label(
        login_window,
        text="Login To Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="darkblue"
    )

    heading.pack(pady=20)

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

    def login_user_gui():

        email = email_entry.get()
        password = password_entry.get()

        if email == "" or password == "":

            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )

            return

        user = login_user(email, password)

        if user:

            login_window.destroy()

            open_dashboard(user)

        else:

            messagebox.showerror(
                "Error",
                "Invalid Email or Password"
            )

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
# DELETE ACCOUNT WINDOW
# =========================

def open_delete_account():

    delete_window = Toplevel(window)

    delete_window.title("Delete Account")

    delete_window.geometry("400x350")

    delete_window.configure(bg="white")

    delete_window.resizable(False, False)

    heading = Label(
        delete_window,
        text="Delete Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="red"
    )

    heading.pack(pady=20)

    Label(
        delete_window,
        text="Email",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    email_entry = Entry(
        delete_window,
        width=30,
        font=("Arial", 11)
    )

    email_entry.pack(pady=5)

    Label(
        delete_window,
        text="Password",
        font=("Arial", 12, "bold"),
        bg="white"
    ).pack()

    password_entry = Entry(
        delete_window,
        width=30,
        font=("Arial", 11),
        show="*"
    )

    password_entry.pack(pady=5)

    def delete_account():

        email = email_entry.get()
        password = password_entry.get()

        if email == "" or password == "":

            messagebox.showerror(
                "Error",
                "Please fill all fields"
            )

            return

        confirm = messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete account?"
        )

        if confirm:

            deleted = delete_user(email, password)

            if deleted:

                messagebox.showinfo(
                    "Success",
                    "Account Deleted Successfully"
                )

                delete_window.destroy()

            else:

                messagebox.showerror(
                    "Error",
                    "Invalid Email or Password"
                )

    delete_btn = Label(
        delete_window,
        text="Delete Account",
        bg="red",
        fg="white",
        font=("Arial", 12, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    delete_btn.pack(pady=25)

    delete_btn.bind(
        "<Button-1>",
        lambda e: delete_account()
    )

# =========================
# MAIN WINDOW BUTTONS
# =========================

# Register Button

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

# Login Button

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

# Delete Account Button

delete_account_btn = Label(
    main_frame,
    text="Delete Account",
    bg="red",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20,
    height=2,
    cursor="hand2"
)

delete_account_btn.pack(pady=10)

delete_account_btn.bind(
    "<Button-1>",
    lambda e: open_delete_account()
)

# =========================
# RUN WINDOW
# =========================

window.mainloop()