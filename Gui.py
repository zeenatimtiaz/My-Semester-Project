# import auth file and register user function
from auth import register_user
# window and buttons created

from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("OLX Desktop Clone")
window.geometry("700x500")
window.configure(bg="#f2f2f2") # background color of main window
window.iconbitmap(r"C:\Users\M.Arsalan\Desktop\MySemesterProject\olx.ico")

# Logo added 
logo=PhotoImage(file=r"C:\Users\M.Arsalan\Desktop\MySemesterProject\olx_logo.png")
logo_label=Label(window,image=logo,bg="#f2f2f2")
logo_label.pack(pady=10)

#tittle added with the styling
tittle=Label(window, text="Welcome to the OLX Clone", font=("Arial" , 22, "bold"),bg="#f2f2f2",fg="darkgreen")
tittle.pack(pady=20)

# register window function
 
def open_register() :
    register_window=Toplevel(window)
    register_window.configure(bg="#ffffff")
    register_window.title("Register")
    register_window.geometry("400x300")
    heading=Label(register_window,text="Create Your Account",font=("Arial",18,"bold"),bg="white",fg="darkgreen")

    #  Name Box

    Label(register_window,text="Name",font=("Arial",12,"bold"),bg="white").pack()
    name_entry=Entry(register_window,width=30,font=("Arial",11))
    name_entry.pack(pady=5)

    # Email Box

    Label(register_window,text="Email",font=("Arial",12,"bold"),bg="white").pack()
    email_entry=Entry(register_window,width=30,font=("Arial",11))
    email_entry.pack(pady=5)

    # Password Box

    Label(register_window , text="Password",font=("Arial",12,"bold"),bg="white").pack()
    password_entry=Entry(register_window,show="*",width=30,font=("Arial",11))
    password_entry.pack(pady=5)

    # now save user register data 

    def save_user() :
        name=name_entry.get()
        email=email_entry.get()
        password=password_entry.get()
        if name=="" or email=="" or password=="":
            messagebox.showerror("Error!..Please fill all the fields first")
            return

        register_user(name,email,password)
        messagebox.showinfo("Success.!!", "User Registered Successfully")
    Button(register_window,text="Register", command=save_user).pack(pady=10)
# register button
register_btn=Button(window, text="Register" , width=20, bg="green" , fg="white" ,font=("Arial", 12, "bold"),command=open_register) # connect register window to main window
register_btn.pack(pady=10)
# Login Button
Login_btn=Button(window, text="Login",width=20,bg="blue",fg="white",font=("Arial",12,"bold"))
Login_btn.pack(pady=10)
# view products button
view_btn=Button(window, text="View Products",width=20,bg="orange",fg="white",font=("Arial",12,"bold"))
view_btn.pack(pady=10)
window.mainloop()