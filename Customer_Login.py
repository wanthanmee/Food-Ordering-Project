import sqlite3
import tkinter.messagebox as messagebox
from tkinter import Tk, StringVar, Toplevel, Frame, Label, Entry, Button, Menu
from tkinter import *

root = Tk()
root.title("The WOK - Chinese Restaurant")
root.geometry("1920x1080+0+0")  # window size and position
root.config(bg='#31140E')  # used to customize the window (bg colour, title)
#root.state("zoomed")  # maximize the root window to fill the entire screen
root.attributes("-fullscreen", True)

# Constants
WIDTH = 800
HEIGHT = 700

# Create variables
USERNAME_LOGIN = StringVar()
PASSWORD_LOGIN = StringVar()
USERNAME_REGISTER = StringVar()
PASSWORD_REGISTER = StringVar()
FULLNAME = StringVar()
EMAIL = StringVar()
PHONENUMBER = StringVar()

conn = None  # connection to database
cursor = None  # use to execute the sql queries and fetch results from db


def Database():  # creating connection to database and creating table
    global conn, cursor
    conn = sqlite3.connect("Customer/db_customer.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `customer` (cust_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, "
        "password TEXT, fullname TEXT, email TEXT, phone_no TEXT)")



def switchWelcomePage():
    root.destroy()
    import Welcome_Page

def Exit():
    result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()


# Switch window
def Home():
    global HomeFrame
    RegisterFrame = Frame(root)
    root.withdraw()  # Hide the main login window
    HomeFrame = Toplevel()  # Create a new window
    HomeFrame.title("Home")

    # Set the size of HomeFrame to match the login or register frame
    HomeFrame.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, (root.winfo_screenwidth() - WIDTH) / 2, (root.winfo_screenheight() - HEIGHT) / 2))

    lbl_home = Label(HomeFrame, text="Welcome to the Home Page", font=('times new roman', 20, 'bold'))
    lbl_home.place(relx=0.5, rely=0.2, anchor=CENTER)

    btn_logout = Button(HomeFrame, text="Logout", font=('times new roman', 16), width=20, command=Logout, bg='blue', fg='white', relief='raised')
    btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="lightblue"))
    btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="blue"))
    btn_logout.place(relx=0.5, rely=0.4, anchor=CENTER)


def Logout():
    global root
    root.deiconify()  # Show the main login window again
    HomeFrame.destroy()  # Close the home window
    # Clear the username and password fields
    USERNAME_LOGIN.set("")
    PASSWORD_LOGIN.set("")


def LoginFormCustomer():
    global LoginFrame, lbl_result1
    LoginFrame = Frame(root)
    LoginFrame.config(bg='#EEE3AD')
    LoginFrame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)

    lbl_title = Label(LoginFrame, text="Login:", font=('times new roman', 25, 'bold'), bd=18, bg='#EEE3AD', fg='#A52A2A')
    lbl_title.place(relx=0.5, rely=0.2, anchor=CENTER)

    lbl_username = Label(LoginFrame, text="Username:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_username.place(relx=0.2, rely=0.4, anchor=CENTER)

    lbl_password = Label(LoginFrame, text="Password:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_password.place(relx=0.2, rely=0.5, anchor=CENTER)

    username = Entry(LoginFrame, font=('times new roman', 16), textvariable=USERNAME_LOGIN, width=20)
    username.place(relx=0.6, rely=0.4, anchor=CENTER)

    password = Entry(LoginFrame, font=('times new roman', 16), textvariable=PASSWORD_LOGIN, width=20, show="*")
    password.place(relx=0.6, rely=0.5, anchor=CENTER)

    btn_login = Button(LoginFrame, text="Login", font=('times new roman', 20), width=20, command=Login, bg='#A52A2A', fg='white', relief='raised')
    btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#EBA743", fg="white"))
    btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#A52A2A", fg="white"))
    btn_login.place(relx=0.5, rely=0.7, anchor=CENTER)

    lbl_text = Label(LoginFrame, text="Not a member?", font=('times new roman', 14), bg='#EEE3AD')
    lbl_text.place(relx=0.5, rely=0.85, anchor=CENTER)

    lbl_register = Label(LoginFrame, text="Register Now", fg="#A52A2A", font=('arial', 12, 'bold'), bg='#EEE3AD')
    lbl_register.bind('<Enter>', lambda event, label=lbl_register: label.config(font=('arial', 12, 'underline', 'bold')))
    lbl_register.bind('<Leave>', lambda event, label=lbl_register: label.config(font=('arial', 12, 'bold')))
    lbl_register.bind('<Button-1>', ToggleToRegister)
    lbl_register.place(relx=0.5, rely=0.9, anchor=CENTER)

    lbl_welcome = Label(LoginFrame, text="< Welcome Page", fg="#A52A2A", font=('arial', 12), bg='#EEE3AD')
    lbl_welcome.bind('<Enter>', lambda event, label=lbl_welcome: label.config(font=('arial', 12, 'underline')))
    lbl_welcome.bind('<Leave>', lambda event, label=lbl_welcome: label.config(font=('arial', 12)))
    lbl_welcome.bind('<Button-1>', lambda event: switchWelcomePage())
    lbl_welcome.place(relx=0.15, rely=0.96, anchor=CENTER)


def RegisterFormCustomer():
    global RegisterFrame, lbl_result2, confirm_password_entry
    RegisterFrame = Frame(root)
    RegisterFrame.config(bg='#EEE3AD')
    RegisterFrame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=700)

    lbl_result2 = Label(RegisterFrame, text="Register:", font=('times new roman', 25, 'bold'), bd=18, bg='#EEE3AD', fg='#A52A2A')
    lbl_result2.place(relx=0.5, rely=0.05, anchor=CENTER)

    lbl_username = Label(RegisterFrame, text="Username:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_username.place(relx=0.25, rely=0.15, anchor=CENTER)

    lbl_password = Label(RegisterFrame, text="Password:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_password.place(relx=0.25, rely=0.25, anchor=CENTER)

    lbl_confirm_password = Label(RegisterFrame, text="Confirm Password:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_confirm_password.place(relx=0.25, rely=0.35, anchor=CENTER)

    lbl_fullname = Label(RegisterFrame, text="Fullname:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_fullname.place(relx=0.25, rely=0.45, anchor=CENTER)

    lbl_email = Label(RegisterFrame, text="Email:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_email.place(relx=0.25, rely=0.55, anchor=CENTER)

    lbl_phone_no = Label(RegisterFrame, text="Phone Number:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
    lbl_phone_no.place(relx=0.25, rely=0.65, anchor=CENTER)

    username = Entry(RegisterFrame, font=('times new roman', 16), textvariable=USERNAME_REGISTER, width=20)
    username.place(relx=0.7, rely=0.15, anchor=CENTER)

    password = Entry(RegisterFrame, font=('times new roman', 16), textvariable=PASSWORD_REGISTER, width=20, show="*")
    password.place(relx=0.7, rely=0.25, anchor=CENTER)

    confirm_password_entry = Entry(RegisterFrame, font=('times new roman', 16), width=20, show="*")
    confirm_password_entry.place(relx=0.7, rely=0.35, anchor=CENTER)

    fullname = Entry(RegisterFrame, font=('times new roman', 16), textvariable=FULLNAME, width=20)
    fullname.place(relx=0.7, rely=0.45, anchor=CENTER)

    email = Entry(RegisterFrame, font=('times new roman', 16), textvariable=EMAIL, width=20)
    email.place(relx=0.7, rely=0.55, anchor=CENTER)

    phone_no = Entry(RegisterFrame, font=('times new roman', 16), textvariable=PHONENUMBER, width=20)
    phone_no.place(relx=0.7, rely=0.65, anchor=CENTER)

    btn_register = Button(RegisterFrame, text="Register", font=('times new roman', 20), width=20, command=Register, bg='#A52A2A', fg='white', relief='raised')
    btn_register.bind("<Enter>", lambda e: btn_register.config(bg="#EBA743", fg="white"))
    btn_register.bind("<Leave>", lambda e: btn_register.config(bg="#A52A2A", fg="white"))
    btn_register.place(relx=0.5, rely=0.8, anchor=CENTER)

    lbl_login = Label(RegisterFrame, text="Click to Login", fg="#A52A2A", font=('arial', 12, 'bold'), bg='#EEE3AD')
    lbl_login.bind('<Enter>', lambda event, label=lbl_login: label.config(font=('arial', 12, 'underline', 'bold')))
    lbl_login.bind('<Leave>', lambda event, label=lbl_login: label.config(font=('arial', 12, 'bold')))
    lbl_login.bind('<Button-1>', ToggleToLogin)
    lbl_login.place(relx=0.5, rely=0.9, anchor=CENTER)


def ToggleToLogin(event=None):  # switching from register to login page.
    if RegisterFrame is not None:
        RegisterFrame.destroy()
    LoginFormCustomer()


def ToggleToRegister(event=None):  # switching the interface from login to register after user click the register link
    if LoginFrame is not None:  # if login form is display, then need to deleted and switch to registration form
        LoginFrame.destroy()
    RegisterFormCustomer()


def Register():
    Database()
    if (USERNAME_REGISTER.get() == "" or PASSWORD_REGISTER.get() == "" or
            FULLNAME.get() == "" or EMAIL.get() == "" or PHONENUMBER.get() == "" or
            confirm_password_entry.get() == ""):
        messagebox.showerror("Error", "Please complete all the required fields!")
    elif PASSWORD_REGISTER.get() != confirm_password_entry.get():
        messagebox.showerror("Error", "Password and Confirm Password do not match!")
    else:
        try:
            cursor.execute("SELECT * FROM `customer` WHERE `username` = ?", (USERNAME_REGISTER.get(),))
            if cursor.fetchone() is not None:
                messagebox.showerror("Error", "Username is already taken!")
            else:
                cursor.execute(
                    "INSERT INTO `customer` (username, password, fullname, email, phone_no) VALUES(?, ?, ?, ?, ?)",
                    (str(USERNAME_REGISTER.get()), str(PASSWORD_REGISTER.get()), str(FULLNAME.get()), str(EMAIL.get()),
                     str(PHONENUMBER.get())))
                conn.commit()  # save current data to database
                USERNAME_REGISTER.set("")
                PASSWORD_REGISTER.set("")
                FULLNAME.set("")
                EMAIL.set("")
                PHONENUMBER.set("")
                confirm_password_entry.delete(0, 'end')  # Clear confirm password field
                messagebox.showinfo("Success", "You Successfully Registered. Click to Login")
        except sqlite3.Error as e:
            messagebox.showerror("Error", "Error occurred during registration: {}".format(e))


def Login():
    Database()
    if USERNAME_LOGIN.get() == "" or PASSWORD_LOGIN.get() == "":
        messagebox.showerror("Error", "Please complete the required field!")
    else:
        cursor.execute("SELECT * FROM `customer` WHERE `username` = ? and `password` = ?",
                       (USERNAME_LOGIN.get(), PASSWORD_LOGIN.get()))
        if cursor.fetchone() is not None:
            messagebox.showinfo("Success", "You Successfully Login")
            Home()  # Call Home function after successful login
        else:
            messagebox.showerror("Error", "Invalid Username or password")


LoginFormCustomer()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

if __name__ == '__main__':
    root.mainloop()
