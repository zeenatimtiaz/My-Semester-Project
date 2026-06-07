# =========================
# IMPORTS
# =========================

from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from auth import register_user, login_user, delete_user
from product import add_product, get_products,delete_product,mark_as_sold
import os

current_user = None

# =========================
# MAIN WINDOW
# =========================

window = Tk()

window.title("OLX Desktop Clone")
window.geometry("900x650")
window.configure(bg="#dff6f0")

window.resizable(False, False)
navbar=Frame(window,bg="#002f34",height=60)
navbar.pack(fill="x")
def navbar_enter(e):
    e.widget.config(bg="#004d52")

def navbar_leave(e):
    e.widget.config(bg="#002f34")
home_btn=Label(navbar,text="🏠 Home",bg="#002f34",fg="white",font=("Helvetica",12,"bold"),cursor="hand2")
home_btn.pack(side="left",padx="15")
home_btn.bind("<Enter>", navbar_enter)
home_btn.bind("<Leave>", navbar_leave)
sell_btn=Label(navbar,text="➕ Sell",bg="#002f34",fg="white",font=("Helvetica",12,"bold"),cursor="hand2")
sell_btn.pack(side="left",padx="15")
products_btn=Label(navbar,text="📦 Products",bg="#002f34",fg="white",font=("Helvetica",12,"bold"),cursor="hand2")
products_btn.pack(side="left",padx="15")
products_btn.bind("<Enter>", navbar_enter)
products_btn.bind("<Leave>", navbar_leave)
logout_btn=Label(navbar,text="🚪 Logout",bg="#002f34",fg="white",font=("Helvetica",12,"bold"),cursor="hand2")
logout_btn.pack(side="left",padx="15")
logout_btn.bind("<Enter>", navbar_enter)
logout_btn.bind("<Leave>", navbar_leave)
def open_home():
    for widget in window.winfo_children():
        if isinstance(widget, Toplevel):
            widget.destroy()
    main_frame.pack(expand=True)
    
def open_sell():
    if current_user:

        open_add_product(current_user)

    else:

        messagebox.showerror(
            "Login Required",
            "Please login first"
        )  
def open_products():
    open_products_window()
def logout():
    global current_user

    current_user = None
    for widget in window.winfo_children():
        if isinstance(widget, Toplevel):
            widget.destroy()

    messagebox.showinfo(
        "Logout",
        "Logged out successfully"
    )


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

    dashboard_sell_btn = Label(
        dashboard,
        text="Sell Product",
        bg="#00a49f",
        fg="white",
        font=("Helvetica", 14, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    dashboard_sell_btn.pack(pady=15)

    dashboard_sell_btn.bind(
        "<Button-1>",
        lambda e: open_add_product(user)
    )

    dashboard_sell_btn.bind("<Enter>", on_enter_green)
    dashboard_sell_btn.bind("<Leave>", on_leave_green)

    # VIEW PRODUCTS BUTTON

    dashboard_view_btn = Label(
        dashboard,
        text=" View Products",
        bg="#3a77ff",
        fg="white",
        font=("Helvetica", 14, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    dashboard_view_btn.pack(pady=15)

    dashboard_view_btn.bind(
        "<Button-1>",
        lambda e: open_products_window()
    )

    dashboard_view_btn.bind("<Enter>", on_enter_blue)
    dashboard_view_btn.bind("<Leave>", on_leave_blue)

    # LOGOUT BUTTON

    dashboard_logout_btn = Label(
        dashboard,
        text="Logout",
        bg="#ff4d4d",
        fg="white",
        font=("Helvetica", 14, "bold"),
        width=22,
        height=2,
        cursor="hand2"
    )

    dashboard_logout_btn.pack(pady=30)

    dashboard_logout_btn.bind(
        "<Button-1>",
        lambda e: dashboard.destroy()
    )

    dashboard_logout_btn.bind("<Enter>", on_enter_red)
    dashboard_logout_btn.bind("<Leave>", on_leave_red)
    
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

    products_window.geometry("1000x700")

    products_window.configure(bg="#dff6f0")

    # =========================
    # HEADING
    # =========================

    heading = Label(
        products_window,
        text="Available Products",
        font=("Helvetica", 28, "bold"),
        bg="#dff6f0",
        fg="#002f34"
    )

    heading.pack(pady=20)

    # =========================
    # TOP BAR
    # =========================

    top_frame = Frame(
        products_window,
        bg="#dff6f0"
    )

    top_frame.pack(fill="x", padx=20)

    back_btn = Button(
        top_frame,
        text="← Back",
        bg="#ff4d4d",
        fg="white",
        font=("Helvetica", 11, "bold"),
        relief="flat",
        cursor="hand2",
        padx=15,
        pady=5,
        command=products_window.destroy
    )

    back_btn.pack(side=LEFT)

    # =========================
    # SEARCH BAR
    # =========================

    search_frame = Frame(
        products_window,
        bg="#dff6f0"
    )

    search_frame.pack(pady=10)

    search_entry = Entry(
        search_frame,
        width=40,
        font=("Helvetica", 13),
        relief="solid",
        bd=1
    )

    search_entry.pack(
        side=LEFT,
        ipady=8,
        padx=10
    )

    search_btn = Button(
        search_frame,
        text="🔍 Search",
        bg="#2f6df6",
        fg="white",
        activebackground="#2457c5",
        activeforeground="white",
        font=("Helvetica", 12, "bold"),
        cursor="hand2",
        relief="flat",
        bd=0,
        padx=20,
        pady=8
    )

    search_btn.pack(side=LEFT)

    # =========================
    # SCROLLABLE AREA
    # =========================

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

    scrollable_frame = Frame(
        canvas,
        bg="#dff6f0"
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
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # =========================
    # LOAD PRODUCTS
    # =========================

    def load_products(search_text=""):

        for widget in scrollable_frame.winfo_children():

            widget.destroy()

        products = get_products()

        row = 0
        col = 0

        for product in products:
            product_id=product[0]

            title = product[1]

            if search_text.lower() not in title.lower():

                continue

            price = product[2]

            description = product[3]

            seller = product[4]

            image_path = product[5]
            status  = product[6]
            if status is None:
                status="available"

            # =========================
            # PRODUCT CARD
            # =========================

            card = Frame(
                scrollable_frame,
                bg="#dff6f0",
                width=340,
                height=500,
                highlightbackground="#dddddd",
                highlightthickness=1
            )

            card.grid(
                row=row,
                column=col,
                padx=18,
                pady=18
            )

            card.grid_propagate(False)

            # =========================
            # IMAGE SECTION
            # =========================

            image_frame = Frame(
                card,
                bg="#f5f5f5",
                width=300,
                height=150
            )

            image_frame.pack(
                pady=15
            )

            image_frame.pack_propagate(False)

            try:

                if image_path:

                    img = Image.open(image_path)

                    img = img.resize((140, 120))

                    img = ImageTk.PhotoImage(img)

                    image_label = Label(
                        image_frame,
                        image=img,
                        bg="#f5f5f5"
                    )

                    image_label.image = img

                    image_label.pack(expand=True)

                else:

                    raise Exception("No Image")

            except:

                image_label = Label(
                    image_frame,
                    text="📷 Product Image",
                    bg="#f5f5f5",
                    fg="gray",
                    font=("Helvetica", 12)
                )

                image_label.pack(expand=True)

            # TITLE

            Label(
                card,
                text=title,
                font=("Helvetica", 18, "bold"),
                bg="#dff6f0",
                fg="#002f34"
            ).pack(pady=(10, 5))

            # PRICE

            Label(
                card,
                text=f"Rs. {price}",
                font=("Helvetica", 15, "bold"),
                bg="#dff6f0",
                fg="#00a49f"
            ).pack()

            # DESCRIPTION

            Label(
                card,
                text=description,
                font=("Helvetica", 10),
                bg="#dff6f0",
                fg="#444444",
                wraplength=250
            ).pack(pady=10)

            # SELLER

            Label(
                card,
                text=f"Seller: {seller}",
                font=("Helvetica", 10, "italic"),
                bg="#dff6f0",
                fg="gray"
            ).pack(pady=5)
            if status == "sold":
                Label(card,text="SOLD OUT",bg="gray",fg="white",font=("Helvetica",12,"bold"),width=15).pack(pady=10)

              

            # BUY FUNCTION

            def buy_product(product_id,button,product_name=title):
                confirm=messagebox.askyesno("Confirm Purchase",f"do you want to buy{product_name}?")
                if confirm:
                    mark_as_sold(product_id)
                    button.config(text="✓ SOLD",bg="gray",state=DISABLED)

                messagebox.showinfo(
                    "Purchase",
                    f"You bought {product_name}"
                )


            # BUY BUTTON

            buy_btn = Button(
                card,
                text="🛍 Buy Now",
                bg="#e22ff6",
                fg="white",
                activebackground="#e22ff6",
                activeforeground="white",
                font=("Helvetica", 11, "bold"),
                cursor="hand2",
                width=14,
                height=1,
                relief="flat",
                bd=0,
                padx=8,
                pady=8
            )

            

            buy_btn.config(command=lambda pid=product_id, btn=buy_btn,name=title:buy_product(pid,btn,name))
            buy_btn.pack(pady=10)

            # DELETE FUNCTION

            def delete_this_product(card_frame=card):

                confirm = messagebox.askyesno(
                    "Delete Product",
                    "Are you sure you want to delete this product?"
                )

                if confirm:

                    card_frame.destroy()

                    messagebox.showinfo(
                        "Deleted",
                        "Product deleted successfully"
                    )

            # DELETE BUTTON

            delete_btn = Button(
                card,
                text="🗑 Delete",
                bg="#ff4d4d",
                fg="white",
                activebackground="#e63939",
                activeforeground="white",
                font=("Helvetica", 11, "bold"),
                cursor="hand2",
                width=14,
                height=1,
                relief="flat",
                bd=0,
                padx=8,
                pady=8,
                command=delete_this_product
            )

            delete_btn.pack(pady=(0, 15))

            col += 1

            if col == 2:

                col = 0

                row += 1

    # SEARCH FUNCTION

    def search_products():

        text = search_entry.get()

        load_products(text)

    search_btn.config(
        command=search_products
    )

    load_products()

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

            global current_user
            current_user=user
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
home_btn.bind(
    "<Button-1>",
    lambda e: open_home()
)

sell_btn.bind(
    "<Button-1>",
    lambda e: open_sell()
)

products_btn.bind(
    "<Button-1>",
    lambda e: open_products()
)

logout_btn.bind(
    "<Button-1>",
    lambda e: logout()
)
window.mainloop()