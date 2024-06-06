from tkinter import *
from PIL import ImageTk  # to install this module, write this code in the python terminal --> pip install pillow

#Issue with the toggle button

root = Tk()
root.title("The WOK- Admin or Customer")
root.geometry("1920x1080+0+0")
root.config(bg='#31140E')
root.attributes("-fullscreen", True)

# Background image
root.bg = ImageTk.PhotoImage(file=r"C:\Users\user\PycharmProjects\Food_Ordering_System\Images\chineseFood.jpg")
root.bg_image = Label(root, image=root.bg).place(x=0, y=0, relwidth=1, relheight=1)


def switchCustomerLogin():
    root.destroy()  # Close the welcome page
    import Customer_Login


def switchAdminLogin():
    root.destroy()  # Close the welcome page
    import Admin_Login


def customerAdmin():
    global customerAdminFrame
    customerAdminFrame = Frame(root, bg='#EEE3AD', width=500, height=350)
    customerAdminFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    lbl_title = Label(customerAdminFrame, text="Admin or Customer?", font=('times new roman', 30, 'bold'), bd=10, bg='#EEE3AD', fg='#A52A2A')
    lbl_title.place(relx=0.5, rely=0.2, anchor=CENTER)

    # Button for Customer leading to Customer Login Page
    btn_customer = Button(customerAdminFrame, text="Customer", font=('times new roman', 20), width=20, bg='#A52A2A',
                          fg='white', relief='raised', command=switchCustomerLogin)
    btn_customer.bind("<Enter>", lambda e: btn_customer.config(bg='#EBA743', fg='white'))
    btn_customer.bind("<Leave>", lambda e: btn_customer.config(bg='#A52A2A', fg='white'))
    btn_customer.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Button for Admin leading to Admin Login Page
    btn_admin = Button(customerAdminFrame, text="Admin", font=('times new roman', 20), width=20, bg='#A52A2A',
                       fg='white', relief='raised', command=switchAdminLogin)
    btn_admin.bind("<Enter>", lambda e: btn_admin.config(bg='#EBA743', fg='white'))
    btn_admin.bind("<Leave>", lambda e: btn_admin.config(bg='#A52A2A', fg='white'))
    btn_admin.place(relx=0.5, rely=0.7, anchor=CENTER)


customerAdmin()

root.mainloop()
