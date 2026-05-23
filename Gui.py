from tkinter import *
from tkinter import messagebox
from auth import register_user, login_user
from product import add_product,get_products
import os

# =========================
# MAIN WINDOW
# =========================

window = Tk()

window.title("OLX Desktop Clone")
window.geometry("700x500")
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
    font=("Arial", 18, "bold"),
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

    # =========================
    # WELCOME LABEL
    # =========================

    welcome_label = Label(
        dashboard,
        text=f"Welcome, {user_name}",
        font=("Arial", 20, "bold"),
        bg="#f5f5f5",
        fg="darkgreen"
    )

    welcome_label.pack(pady=25)

    # =========================
    # SUBTITLE
    # =========================

    subtitle = Label(
        dashboard,
        text="Manage Your Products Easily..!!",
        font=("Arial", 11),
        bg="#f5f5f5",
        fg="gray"
    )

    subtitle.pack(pady=5)

    # =========================
    # EMAIL LABEL
    # =========================

    email_label = Label(
        dashboard,
        text=f"Email: {user_email}",
        font=("Arial", 12),
        bg="#f5f5f5",
        fg="gray"
    )

    email_label.pack(pady=10)

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
        bd=0,
        cursor="hand2"
    )

    add_product_btn.pack(pady=12)
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
        bd=0,
        cursor="hand2"
    )

    view_products_btn.pack(pady=12)
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
        bd=0,
        cursor="hand2"
    )

    logout_btn.pack(pady=30)

    logout_btn.bind(
        "<Button-1>",
        lambda e: dashboard.destroy()
    )

#  =======Add Product Window ============
def open_add_product(user):

    add_window = Toplevel(window)
    add_window.title("Add Product")
    add_window.geometry("520x600")
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

    # =========================
    # SELLER FRAME
    # =========================
    seller_frame = LabelFrame(
        add_window,
        text="Seller Information",
        font=("Arial", 12, "bold"),
        bg="#f5f5f5",
        fg="black",
        padx=10,
        pady=10
    )
    seller_frame.pack(pady=10, fill="x", padx=20)

    seller_name_label = Label(
        seller_frame,
        text=f"Name: {user[1]}",
        bg="#f5f5f5",
        font=("Arial", 11)
    )
    seller_name_label.pack(anchor="w")

    seller_email_label = Label(
        seller_frame,
        text=f"Email: {user[2]}",
        bg="#f5f5f5",
        font=("Arial", 11)
    )
    seller_email_label.pack(anchor="w")

    # Subtitle
    subtitle = Label(
        add_window,
        text="Add Product Info Carefully..!!",
        font=("Arial", 11),
        bg="#f5f5f5",
        fg="gray"
    )
    subtitle.pack(pady=5)

    # Product section title
    product_label = Label(
        add_window,
        text="Product Information",
        font=("Arial", 13, "bold"),
        bg="#f5f5f5",
        fg="black"
    )
    product_label.pack(pady=10)

    # Title
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
        height=5,
        font=("Arial", 11)
    )
    desc_text.pack(pady=5)

    # Save function
    def save_product():

        title = title_entry.get()
        price = price_entry.get()
        description = desc_text.get("1.0", END)

        if title == "" or price == "" or description.strip() == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        add_product(title, price, description, seller_name)

        messagebox.showinfo("Success", "Product Added Successfully")

        add_window.destroy()

    # Save button
    save_btn = Label(
        add_window,
        text="Save Product",
        font=("Arial", 12, "bold"),
        bg="green",
        fg="white",
        width=20,
        height=2,
        cursor="hand2"
    )

    save_btn.pack(pady=20)
    save_btn.bind("<Button-1>", lambda e: save_product())

# =========================
# VIEW PRODUCTS WINDOW
# =========================

def open_products_window():

    products_window = Toplevel(window)

    products_window.title("All Products")

    products_window.geometry("700x600")

    products_window.configure(bg="#f5f5f5")

    products_window.resizable(False, False)

    # =========================
    # HEADING
    # =========================

    heading = Label(
        products_window,
        text="All Products",
        font=("Arial", 20, "bold"),
        bg="#f5f5f5",
        fg="darkgreen"
    )

    heading.pack(pady=15)

    # =========================
    # SEARCH BAR
    # =========================

    search_entry = Entry(
        products_window,
        width=35,
        font=("Arial", 12)
    )

    search_entry.pack(pady=10)

    # =========================
    # PRODUCTS FRAME
    # =========================

    products_frame = Frame(
        products_window,
        bg="#f5f5f5"
    )

    products_frame.pack(fill="both", expand=True)

    # =========================
    # SHOW PRODUCTS FUNCTION
    # =========================

    def show_products(search_text=""):

        # old widgets remove
        for widget in products_frame.winfo_children():
            widget.destroy()

        products = get_products()

        for product in products:

            product_id = product[0]
            title = product[1]
            price = product[2]
            description = product[3]
            seller = product[4]

            # search filter
            if search_text.lower() not in title.lower():
                continue

            # =========================
            # PRODUCT CARD
            # =========================

            card = Frame(
                products_frame,
                bg="white",
                bd=1,
                relief="solid"
            )

            card.pack(
                pady=10,
                padx=20,
                fill="x"
            )

            # Title
            title_label = Label(
                card,
                text=title,
                font=("Arial", 16, "bold"),
                bg="white",
                fg="darkgreen"
            )

            title_label.pack(anchor="w", padx=10, pady=5)

            # Price
            price_label = Label(
                card,
                text=f"Price: Rs. {price}",
                font=("Arial", 12, "bold"),
                bg="white",
                fg="blue"
            )

            price_label.pack(anchor="w", padx=10)

            # Description
            desc_label = Label(
                card,
                text=f"Description: {description}",
                font=("Arial", 11),
                bg="white",
                wraplength=600,
                justify="left"
            )

            desc_label.pack(anchor="w", padx=10, pady=5)

            # Seller
            seller_label = Label(
                card,
                text=f"Seller: {seller}",
                font=("Arial", 10, "italic"),
                bg="white",
                fg="gray"
            )

            seller_label.pack(anchor="w", padx=10, pady=5)

    # =========================
    # SEARCH BUTTON
    # =========================

    search_btn = Label(
        products_window,
        text="Search",
        bg="darkblue",
        fg="white",
        font=("Arial", 11, "bold"),
        width=15,
        height=2,
        cursor="hand2"
    )

    search_btn.pack(pady=10)

    search_btn.bind(
        "<Button-1>",
        lambda e: show_products(search_entry.get())
    )

    # show all products first time
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

    # Heading

    heading = Label(
        register_window,
        text="Create Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="darkgreen"
    )

    heading.pack(pady=15)

    # Name

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

    # Email

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

    # Password

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

    # Save User Function

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

        register_window.destroy()

    # Register Button

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

    # Heading

    heading = Label(
        login_window,
        text="Login To Your Account",
        font=("Arial", 18, "bold"),
        bg="white",
        fg="darkblue"
    )

    heading.pack(pady=20)

    # Email

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

    # Password

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

    # Login Function

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

    # Login Button

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

# =========================
# RUN WINDOW
# =========================


window.mainloop()