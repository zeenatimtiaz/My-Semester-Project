# =========================
# IMPORTS
# =========================

from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image,ImageTk
from auth import register_user, login_user, delete_user
from product import add_product, get_products
import os

# =========================
# MAIN WINDOW
# =========================

window = Tk()

window.title("OLX Desktop Clone")
window.geometry("900x650")
window.configure(bg="#dff6f0")

window.resizable(False, False)

# =========================
# MAIN FRAME
# =========================

main_frame = Frame(window, bg="#dff6f0")
main_frame.pack(expand=True)

# =========================
# LOGO
# =========================

current_folder = os.path.dirname(__file__)

logo_path = os.path.join(current_folder, "logo.png")

logo = PhotoImage(file=logo_path)

logo = logo.subsample(15, 15)

logo_label = Label(
    main_frame,
    image=logo,
    bg="#dff6f0"
)

logo_label.pack(pady=20)

# =========================
# TITLE
# =========================

title = Label(
    main_frame,
    text="Buy & Sell Anything Easily",
    font=("Helvetica", 30, "bold"),
    bg="#dff6f0",
    fg="#002f34"
)

title.pack(pady=10)

subtitle = Label(
    main_frame,
    text="Pakistan's Modern Desktop Marketplace",
    font=("Helvetica", 12),
    bg="#dff6f0",
    fg="gray"
)

subtitle.pack(pady=(0, 30))

# =========================
# HOVER EFFECTS
# =========================

def on_enter_green(e):
    e.widget["bg"] = "#008b87"

def on_leave_green(e):
    e.widget["bg"] = "#00a49f"

def on_enter_blue(e):
    e.widget["bg"] = "#245de6"

def on_leave_blue(e):
    e.widget["bg"] = "#3a77ff"

def on_enter_red(e):
    e.widget["bg"] = "#e63939"

def on_leave_red(e):
    e.widget["bg"] = "#ff4d4d"

# =========================
# DASHBOARD
# =========================

def open_dashboard(user):

    dashboard = Toplevel(window)

    dashboard.title("Dashboard")

    dashboard.geometry("600x500")

    dashboard.configure(bg="#dff6f0")

    user_name = user[1]
    user_email = user[2]

    welcome_label = Label(
        dashboard,
        text=f"Welcome, {user_name}",
        font=("Helvetica", 24, "bold"),
        bg="#dff6f0",
        fg="#002f34"
    )

    welcome_label.pack(pady=25)

    email_label = Label(
        dashboard,
        text=f"Email: {user_email}",
        font=("Helvetica", 11),
        bg="#dff6f0",
        fg="gray"
    )

    email_label.pack(pady=10)

    # SELL PRODUCT BUTTON

    sell_btn = Label(
        dashboard,
        text="Sell Product",
        bg="#00a49f",
        fg="white",
        font=("Helvetica", 14, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    sell_btn.pack(pady=15)

    sell_btn.bind(
        "<Button-1>",
        lambda e: open_add_product(user)
    )

    sell_btn.bind("<Enter>", on_enter_green)
    sell_btn.bind("<Leave>", on_leave_green)

    # VIEW PRODUCTS BUTTON

    view_btn = Label(
        dashboard,
        text=" View Products",
        bg="#3a77ff",
        fg="white",
        font=("Helvetica", 14, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    view_btn.pack(pady=15)

    view_btn.bind(
        "<Button-1>",
        lambda e: open_products_window()
    )

    view_btn.bind("<Enter>", on_enter_blue)
    view_btn.bind("<Leave>", on_leave_blue)

    # LOGOUT BUTTON

    logout_btn = Label(
        dashboard,
        text="Logout",
        bg="#ff4d4d",
        fg="white",
        font=("Helvetica", 14, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    logout_btn.pack(pady=30)

    logout_btn.bind(
        "<Button-1>",
        lambda e: dashboard.destroy()
    )

    logout_btn.bind("<Enter>", on_enter_red)
    logout_btn.bind("<Leave>", on_leave_red)

# =========================
# ADD PRODUCT WINDOW
# =========================

def open_add_product(user):

    add_window = Toplevel(window)

    add_window.title("Sell Product")

    add_window.geometry("500x650")

    add_window.configure(bg="#dff6f0")
    add_window.grab_set()  

    seller_name = user[1]

    heading = Label(
        add_window,
        text="Sell Your Product",
        font=("Helvetica", 22, "bold"),
        bg="#dff6f0",
        fg="#002f34"
    )

    heading.pack(pady=20)

    # PRODUCT TITLE

    Label(
        add_window,
        text="Product Title",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    title_entry = Entry(
        add_window,
        width=35,
        font=("Helvetica", 11)
    )

    title_entry.pack(pady=8)

    # PRICE

    Label(
        add_window,
        text="Price",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    price_entry = Entry(
        add_window,
        width=35,
        font=("Helvetica", 11)
    )

    price_entry.pack(pady=8)

    # DESCRIPTION

    Label(
        add_window,
        text="Description",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    desc_text = Text(
        add_window,
        width=35,
        height=6,
        font=("Helvetica", 11)
    )

    desc_text.pack(pady=8)

    # IMAGE UPLOAD
# IMAGE UPL    # IMAGE UPLOAD

    image_path = StringVar()

    def upload_image():

        file = filedialog.askopenfilename(
            parent=add_window,
            title="Select Product Image",
            filetypes=[
                ("PNG Files", "*.png"),
                ("JPG Files", "*.jpg"),
                ("JPEG Files", "*.jpeg")
            ]
        )

        if file:
            image_path.set(file)
            image_label.config(text="✅ Image Selected")

    # UPLOAD BUTTON

    upload_btn = Label(
        add_window,
        text="📷 Upload Image",
        bg="#3a77ff",
        fg="white",
        font=("Helvetica", 12, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    upload_btn.pack(pady=15)

    upload_btn.bind(
        "<Button-1>",
        lambda e: upload_image()
    )

    # IMAGE LABEL

    image_label = Label(
        add_window,
        text="No Image Selected",
        font=("Helvetica", 10),
        bg="#dff6f0",
        fg="gray"
    )

    image_label.pack()

    # SAVE PRODUCT

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

        add_product(
            title,
            price,
            description,
            seller_name,
            image_path.get()
        )

        messagebox.showinfo(
            "Success",
            "Product Added Successfully"
        )

        add_window.destroy()

    # SAVE BUTTON

    save_btn = Label(
        add_window,
        text="💰 Sell Product",
        bg="#00a49f",
        fg="white",
        font=("Helvetica", 13, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    save_btn.pack(pady=25)

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
    products_window.geometry("850x650")
    products_window.configure(bg="#dff6f0")

    heading = Label(
        products_window,
        text="Available Products",
        font=("Helvetica", 24, "bold"),
        bg="#dff6f0",
        fg="#002f34"
    )
    heading.pack(pady=20)

    canvas = Canvas(
        products_window,
        bg="#dff6f0",
        highlightthickness=0
    )

    scrollbar = Scrollbar(
        products_window,
        orient="vertical",
        command=canvas.yview
    )

    scrollable_frame = Frame(canvas, bg="#dff6f0")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    products = get_products()

    row = 0
    col = 0

    for product in products:

        title = product[1]
        price = product[2]
        description = product[3]
        seller = product[4]
        image_path = product[5]   # ✅ IMPORTANT FIX

        card = Frame(
            scrollable_frame,
            bg="white",
            width=320,
            height=300,
            padx=15,
            pady=15,
            highlightbackground="#d9d9d9",
            highlightthickness=2
        )

        card.grid(row=row, column=col, padx=20, pady=20)
        card.grid_propagate(False)

        # ======================
        # IMAGE SECTION (FIXED)
        # ======================
        try:
            if image_path:
                img = Image.open(image_path)
                img = img.resize((200, 150))
                img = ImageTk.PhotoImage(img)

                image_label = Label(card, image=img)
                image_label.image = img
                image_label.pack(pady=10)

            else:
                raise Exception("No Image")

        except:
            image_label = Label(
                card,
                text="No Image Available",
                bg="#eeeeee",
                fg="gray",
                width=25,
                height=6
            )
            image_label.pack(pady=10)

        # TITLE
        Label(
            card,
            text=title,
            font=("Helvetica", 16, "bold"),
            bg="white",
            fg="#002f34",
            wraplength=250
        ).pack()

        # PRICE
        Label(
            card,
            text=f"Rs. {price}",
            font=("Helvetica", 14, "bold"),
            bg="white",
            fg="#00a49f"
        ).pack(pady=5)

        # DESCRIPTION
        Label(
            card,
            text=description,
            font=("Helvetica", 10),
            bg="white",
            fg="gray",
            wraplength=250
        ).pack()

        # SELLER
        Label(
            card,
            text=f"Seller: {seller}",
            font=("Helvetica", 10, "italic"),
            bg="white",
            fg="gray"
        ).pack(pady=5)

        col += 1
        if col == 2:
            col = 0
            row += 1
# =========================
# REGISTER WINDOW
# =========================

def open_register():

    register_window = Toplevel(window)

    register_window.title("Register")

    register_window.geometry("400x400")

    register_window.configure(bg="#dff6f0")

    heading = Label(
        register_window,
        text="Create Your Account",
        font=("Helvetica", 20, "bold"),
        bg="#dff6f0",
        fg="#002f34"
    )

    heading.pack(pady=20)

    Label(
        register_window,
        text="Name",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    name_entry = Entry(register_window, width=30)
    name_entry.pack(pady=8)

    Label(
        register_window,
        text="Email",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    email_entry = Entry(register_window, width=30)
    email_entry.pack(pady=8)

    Label(
        register_window,
        text="Password",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    password_entry = Entry(
        register_window,
        width=30,
        show="*"
    )

    password_entry.pack(pady=8)

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

    register_btn = Label(
        register_window,
        text="Register",
        bg="#00a49f",
        fg="white",
        font=("Helvetica", 13, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    register_btn.pack(pady=20)

    register_btn.bind(
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

    login_window.configure(bg="#dff6f0")

    heading = Label(
        login_window,
        text="Login To Your Account",
        font=("Helvetica", 20, "bold"),
        bg="#dff6f0",
        fg="#002f34"
    )

    heading.pack(pady=20)

    Label(
        login_window,
        text="Email",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    email_entry = Entry(login_window, width=30)
    email_entry.pack(pady=8)

    Label(
        login_window,
        text="Password",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    password_entry = Entry(
        login_window,
        width=30,
        show="*"
    )

    password_entry.pack(pady=8)

    def login_user_gui():

        email = email_entry.get()
        password = password_entry.get()

        user = login_user(email, password)

        if user:

            login_window.destroy()

            open_dashboard(user)

        else:

            messagebox.showerror(
                "Error",
                "Invalid Email or Password"
            )

    login_btn = Label(
        login_window,
        text="Login",
        bg="#3a77ff",
        fg="white",
        font=("Helvetica", 13, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    login_btn.pack(pady=20)

    login_btn.bind(
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

    delete_window.configure(bg="#dff6f0")

    heading = Label(
        delete_window,
        text="Delete Your Account",
        font=("Helvetica", 20, "bold"),
        bg="#dff6f0",
        fg="red"
    )

    heading.pack(pady=20)

    Label(
        delete_window,
        text="Email",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    email_entry = Entry(delete_window, width=30)
    email_entry.pack(pady=8)

    Label(
        delete_window,
        text="Password",
        font=("Helvetica", 12, "bold"),
        bg="#dff6f0"
    ).pack()

    password_entry = Entry(
        delete_window,
        width=30,
        show="*"
    )

    password_entry.pack(pady=8)

    def delete_account():

        email = email_entry.get()
        password = password_entry.get()

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
        bg="#ff4d4d",
        fg="white",
        font=("Helvetica", 13, "bold"),
        width=20,
        height=2,
        cursor="hand2"
    )

    delete_btn.pack(pady=20)

    delete_btn.bind(
        "<Button-1>",
        lambda e: delete_account()
    )

# =========================
# MAIN WINDOW BUTTONS
# =========================

register_btn = Label(
    main_frame,
    text="Register",
    bg="#00a49f",
    fg="white",
    font=("Helvetica", 14, "bold"),
    width=22,
    height=2,
    cursor="hand2"
)

register_btn.pack(pady=10)

register_btn.bind(
    "<Button-1>",
    lambda e: open_register()
)

login_btn = Label(
    main_frame,
    text="Login",
    bg="#3a77ff",
    fg="white",
    font=("Helvetica", 14, "bold"),
    width=22,
    height=2,
    cursor="hand2"
)

login_btn.pack(pady=10)

login_btn.bind(
    "<Button-1>",
    lambda e: open_login()
)

delete_account_btn = Label(
    main_frame,
    text="Delete Account",
    bg="#ff4d4d",
    fg="white",
    font=("Helvetica", 14, "bold"),
    width=22,
    height=2,
    cursor="hand2"
)

delete_account_btn.pack(pady=10)

delete_account_btn.bind(
    "<Button-1>",
    lambda e: open_delete_account()
)

# =========================
# RUN APP
# =========================

window.mainloop()