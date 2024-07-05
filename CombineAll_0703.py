from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime
import math
import random
import os
import itertools
import sqlite3
import ast
import requests
import json
from tkinter import *
from tkinter import messagebox, scrolledtext
from threading import Thread
from fpdf import FPDF
from tkinter import filedialog

root = tk.Tk()
root.geometry('1920x1080')
root.attributes("-fullscreen", True)
conn = None
cursor = None
current_review_index = 0
reviews = []
tableNoFrame = None
LoginFrame = None
main_frame2 = None
main_frame3 = None
drinks_frame = None
tree = None
selected_TableOption = None
other_remarks = None
price_Entry = None
tablenumEntry = None
visit_id_2 = None
cust_id = 1  # Assuming a default customer ID, please adjust as per your actual setup
table_no_2 = None  # Initialize to None initially
payby_label = None
payby_label2 = None

USERNAME_LOGIN = StringVar()
PASSWORD_LOGIN = StringVar()
USERNAME_REGISTER = StringVar()
PASSWORD_REGISTER = StringVar()
FULLNAME = StringVar()
EMAIL = StringVar()
PHONENUMBER = StringVar()

conn = sqlite3.connect('db_thewok1.db')
c = conn.cursor()
'''
c.execute(
   "CREATE TABLE IF NOT EXISTS customer(cust_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT NOT NULL)"
)

# Create reviews table if it doesn't exist
c.execute(
   "CREATE TABLE IF NOT EXISTS reviews(review_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, customer_rating INTEGER NOT NULL, customer_review TEXT NOT NULL, cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(cust_id))"
)

conn.commit()
'''





def tableNo():
  global tableNoFrame
  tableNoFrame = Frame(root) # Create a new window
  tableNoFrame.place(x=0, y=0, width=1920, height=1080)


  lbl_tableno = Label(tableNoFrame, text="Please Enter your Table No", font=('Verdana', 20, 'bold'))
  lbl_tableno.place(x=960, y=300, anchor=CENTER)


  lbl_text1 = Label(tableNoFrame, text="(If Dining In)", font=('Verdana', 16))
  lbl_text1.place(x=960, y=350, anchor=CENTER)


  entry_tableno = Entry(tableNoFrame, font=('Verdana', 20))
  entry_tableno.place(x=960, y=450, anchor=CENTER)


  #btn_confirm = Button(tableNoFrame, text="Confirm", font=('Verdana', 16, 'bold'), width=10, bg='#A52A2A', fg='#EEE3AD', relief='raised', command=lambda: validate_table_no(entry_tableno))
  btn_confirm = Button(tableNoFrame, text="Confirm", font=('Verdana', 16, 'bold'), width=10, bg='#A52A2A',
                       fg='#EEE3AD', relief='raised', command=lambda: validate_table_no(entry_tableno))
  btn_confirm.place(x=850, y=600, anchor=CENTER)


  btn_dineOut = Button(tableNoFrame, text="Dine Out", font=('Verdana', 16, 'bold'), width=10, bg='#A52A2A', fg='#EEE3AD', relief='raised', command=link_home_page)
  btn_dineOut.place(x=1070, y=600, anchor=CENTER)


  btn_logout = Button(tableNoFrame, text="Logout", font=('Verdana', 16, 'bold'), width=10, command=Logout, bg='blue', fg='white', relief='raised')
  btn_logout.bind("<Enter>", lambda e: btn_logout.config(bg="lightblue"))
  btn_logout.bind("<Leave>", lambda e: btn_logout.config(bg="blue"))
  btn_logout.place(x=960, y=800, anchor=CENTER)


'''
def close_register_window(event=None):
   if registerwindow is not None:
       registerwindow.destroy()
'''

def validate_table_no(entry):
   global visit_id_2, chat_objective, order_id_2, visit_id_3  # Define global variable
   chat_objective = 1

   try:
       table_no = int(entry.get())
       if 1 <= table_no <= 7:
           messagebox.showinfo("Success", f"All set for Table {table_no}!")
           loginwindow.destroy()
           tableNoFrame.destroy()

           cursor.execute(
               "INSERT INTO visiting (cust_id, table_no) VALUES (?, ?)",
               (cust_id, table_no)
           )
           conn.commit()

           # Retrieve the visit_id of the inserted record
           visit_id_2 = cursor.lastrowid
           print(visit_id_2)
           visit_id_3 = int(visit_id_2)

           get_order_id()  # Ensure order_id_2 is set

           home_page()

       else:
           messagebox.showerror("Error", "Please enter a table number between 1 and 7.")
   except ValueError:
       messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 7.")
   except Exception as e:
       messagebox.showerror("Error", f"An error occurred: {e}")

def get_order_id():
   global order_id_2, visit_id_3  # Ensure visit_id_3 is global and accessible
   cursor.execute("INSERT INTO orders (visit_id) VALUES (?)", (visit_id_3,))
   conn.commit()
   order_id_2 = cursor.lastrowid
   order_id_2 = int(order_id_2)
   messagebox.showinfo('received an order_id_2',f'{order_id_2}')


def get_table_no():
   cursor.execute("SELECT table_no FROM visiting WHERE visit_id = ? AND cust_id = ?",
                  (visit_id_2, cust_id))
   row = cursor.fetchone()
   if row is not None:
       table_no_3 = row[0]
       return table_no_3


def Logout():
  global root
  tableNoFrame.destroy()  # Close the home window
  registerwindow.destroy()
  LoginFormCustomer()  # Show the main login window again
  # Clear the username and password fields
  USERNAME_LOGIN.set("")
  PASSWORD_LOGIN.set("")

def link_home_page():
   global chat_objective
   loginwindow.destroy()
   tableNoFrame.destroy()
   chat_objective =2
   home_page()
   registerwindow.destroy()



def LoginFormCustomer():
  global LoginFrame, loginwindow
  loginwindow= Frame(root,width=1920, height=1080)
  loginwindow.place(x=0,y=0)

  thewok_name = Label(loginwindow, text=f'Nice to have you.\n We are {restaurant_name4}.', font=('Times new roman',40,'bold'), fg='brown')
  thewok_name.place(x=960,y=180, anchor='center')
  LoginFrame = Frame(loginwindow)
  LoginFrame.config(bg='#EEE3AD')
  root.config(bg='#31140E')
  LoginFrame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=400)


  lbl_title = Label(LoginFrame, text="Login:", font=('times new roman', 25, 'bold'), bd=18, bg='#EEE3AD',
                    fg='#A52A2A')
  lbl_title.place(relx=0.5, rely=0.2, anchor=CENTER)


  lbl_username = Label(LoginFrame, text="Username:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
  lbl_username.place(relx=0.2, rely=0.4, anchor=CENTER)


  lbl_password = Label(LoginFrame, text="Password:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
  lbl_password.place(relx=0.2, rely=0.5, anchor=CENTER)


  username = Entry(LoginFrame, font=('times new roman', 16), textvariable=USERNAME_LOGIN, width=20)
  username.place(relx=0.6, rely=0.4, anchor=CENTER)


  password = Entry(LoginFrame, font=('times new roman', 16), textvariable=PASSWORD_LOGIN, width=20, show="*")
  password.place(relx=0.6, rely=0.5, anchor=CENTER)


  btn_login = Button(LoginFrame, text="Login", font=('times new roman', 20), width=20, command=Login, bg='#A52A2A',
                     fg='white', relief='raised')
  btn_login.bind("<Enter>", lambda e: btn_login.config(bg="#EBA743", fg="white"))
  btn_login.bind("<Leave>", lambda e: btn_login.config(bg="#A52A2A", fg="white"))
  btn_login.place(relx=0.5, rely=0.7, anchor=CENTER)


  lbl_text = Label(LoginFrame, text="Not a member?", font=('times new roman', 14), bg='#EEE3AD')
  lbl_text.place(relx=0.5, rely=0.85, anchor=CENTER)


  lbl_register = Label(LoginFrame, text="Register Now", fg="#A52A2A", font=('arial', 12, 'bold'), bg='#EEE3AD')
  lbl_register.bind('<Enter>',
                    lambda event, label=lbl_register: label.config(font=('arial', 12, 'underline', 'bold')))
  lbl_register.bind('<Leave>', lambda event, label=lbl_register: label.config(font=('arial', 12, 'bold')))
  lbl_register.bind('<Button-1>', ToggleToRegister)
  lbl_register.place(relx=0.5, rely=0.9, anchor=CENTER)

'''
  lbl_welcome = Label(LoginFrame, text="< Welcome Page", fg="#A52A2A", font=('arial', 12), bg='#EEE3AD')
  lbl_welcome.bind('<Enter>', lambda event, label=lbl_welcome: label.config(font=('arial', 12, 'underline')))
  lbl_welcome.bind('<Leave>', lambda event, label=lbl_welcome: label.config(font=('arial', 12)))
  lbl_welcome.bind('<Button-1>', lambda event: switchWelcomePage())
  lbl_welcome.place(relx=0.15, rely=0.96, anchor=CENTER)
'''



def RegisterFormCustomer():
   global RegisterFrame, lbl_result2, confirm_password_entry, registerwindow
   registerwindow = Frame(root, width=1920, height=1080)
   registerwindow.place(x=0, y=0)

   RegisterFrame = Frame(registerwindow)
   RegisterFrame.config(bg='#EEE3AD')
   root.config(bg='#31140E')
   RegisterFrame.place(relx=0.5, rely=0.5, anchor=CENTER, width=500, height=700)


   lbl_result2 = Label(RegisterFrame, text="Register:", font=('times new roman', 25, 'bold'), bd=18, bg='#EEE3AD',
                      fg='#A52A2A')
   lbl_result2.place(relx=0.5, rely=0.05, anchor=CENTER)


   lbl_username = Label(RegisterFrame, text="Username:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
   lbl_username.place(relx=0.25, rely=0.15, anchor=CENTER)


   lbl_password = Label(RegisterFrame, text="Password:", font=('times new roman', 16), bd=18, bg='#EEE3AD')
   lbl_password.place(relx=0.25, rely=0.25, anchor=CENTER)


   lbl_confirm_password = Label(RegisterFrame, text="Confirm Password:", font=('times new roman', 16), bd=18,
                               bg='#EEE3AD')
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


   btn_register = Button(RegisterFrame, text="Register", font=('times new roman', 20), width=20, command=Register,
                        bg='#A52A2A', fg='white', relief='raised')
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
   loginwindow.destroy()
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
  global cust_id, cust_name, contact
  Database()
  if USERNAME_LOGIN.get() == "" or PASSWORD_LOGIN.get() == "":
      messagebox.showerror("Error", "Please complete the required field!")
  else:
      cursor.execute("SELECT cust_id, fullname, phone_no FROM customer WHERE username = ? AND password = ?",
                     (USERNAME_LOGIN.get(), PASSWORD_LOGIN.get()))
      row = cursor.fetchone()
      if row is not None:
          cust_id = row[0]  # Retrieve the cust_id from the query result
          cust_name =row[1]
          contact =row[2]
          messagebox.showinfo("Success", "You Successfully Login")
          LoginFrame.destroy()
          tableNo()  # Call tableNo function after successful login
      else:
          messagebox.showerror("Error", "Invalid Username or password")


def fetch_restaurant_info():
   conn = sqlite3.connect('db_thewok1.db')
   c = conn.cursor()
   c.execute('SELECT * FROM restaurant_information')
   data = c.fetchone()
   conn.close()
   return data

def create_marquee_text():
   restaurant_info = fetch_restaurant_info()
   if restaurant_info:
       restaurant_name = restaurant_info[1]
       operation_hour = restaurant_info[2]
       restaurant_location_db = restaurant_info[3]
       restaurant_contact_db = restaurant_info[4]
       marquee_text = (
           f"                              ** Welcome to {restaurant_name}**                              "
           f"                              ** Business Hours: {operation_hour} **                              "
           "                              ** Enjoy your meal and have a great day! **                               "
       )
   else:
       marquee_text = (
           "Error getting from database."
       )
   return marquee_text

def get_menu_imagepath():
   # Connect to the database (change the path to your database file)
   conn = sqlite3.connect('db_thewok1.db')
   cursor = conn.cursor()

   # Query to fetch all items from the menu table
   cursor.execute("SELECT item_image_path FROM items")
   rows = cursor.fetchall()

   # Initialize an empty string for the restaurant menu
   restaurantImagePathList = []

   # Loop through each row and format the information
   for row in rows:
       item_image_path = row[0]  # Extract the first element from the tuple
       restaurantImagePathList.append(item_image_path)

   # Close the database connection
   conn.close()

   return restaurantImagePathList

class HomeSlideshow:
   def __init__(self, home_frame):
       marquee_text = create_marquee_text()

       self.marquee = self.Marquee(home_frame, text=marquee_text, font=('Verdana', 15, 'bold'), borderwidth=1, relief="sunken", fps=60, speed=2)
       self.marquee.pack(side="top", fill="x", pady=20)

       self.restaurant_logo = PhotoImage(file=r"C:\Users\Vennis\Downloads\restaurant_logo_gif.gif")

       self.logo = Label(home_frame, image=self.restaurant_logo, width=350, height=350)
       self.logo.place(x=50, y=100)

       restaurant_info = fetch_restaurant_info()
       if restaurant_info:
           restaurant_name = restaurant_info[1]
           operation_hour = restaurant_info[2]
           restaurant_location_db = restaurant_info[3]
           restaurant_contact_db = restaurant_info[4]
       else:
           restaurant_name = "Error getting from database."
           operation_hour = "Error getting from database."
           restaurant_location_db = "Error getting from database."
           restaurant_contact_db = "Error getting from database."

       self.nameFrame = Frame(home_frame, width=350, height=60, bd=1)
       self.nameFrame.place(x=50, y=470)

       self.theWok = Label(self.nameFrame, text=restaurant_name, fg='brown', font=('helvetica', 22, 'bold'))
       self.theWok.place(x=175, y=30, anchor='center')

       self.nameFrame2 = Frame(home_frame, width=350, height=400, bd=1)
       self.nameFrame2.place(x=50, y=550)

       self.location = Label(self.nameFrame2, text='Location:', fg='brown', font=('verdana', 16, 'bold'))
       self.location.grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)

       self.address = Label(self.nameFrame2, text=restaurant_location_db, fg='salmon4', font=('helvetica', 16))
       self.address.grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)

       self.bushours = Label(self.nameFrame2, text='Business Hours:', fg='brown', font=('verdana', 16, 'bold'))
       self.bushours.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)

       self.details = Label(self.nameFrame2, text=operation_hour, fg='salmon4', font=('helvetica', 16), anchor='w', justify=tk.LEFT)
       self.details.grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)

       self.contact = Label(self.nameFrame2, text='Contact Us:', fg='brown', font=('verdana', 16, 'bold'))
       self.contact.grid(row=4, column=0, sticky=tk.W, padx=10, pady=5)

       self.phone_num = Label(self.nameFrame2, text=restaurant_contact_db, fg='salmon4', font=('helvetica', 16))
       self.phone_num.grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)

       itemimagepathlist = get_menu_imagepath()

       self.pictureID = 1
       self.maxPicture = len(itemimagepathlist)

       self.pictures = {}
       for idx, path in enumerate(itemimagepathlist, start=1):
           self.pictures[idx] = {'file': path}

       self.image_label = Label(home_frame, width=1280, height=720)
       self.image_label.place(x=500, y=100)

       initial_picture = self.pictures[1]
       self.image = self.load_and_resize_image(initial_picture['file'])
       self.image_label.config(image=self.image)
       self.image_label.image = self.image

       self.showPicture(home_frame)

   def load_and_resize_image(self, file_path):
       original_image = PhotoImage(file=file_path)
       return original_image.subsample(original_image.width() // 1280, original_image.height() // 720)

   def showPicture(self, home_frame):
       if self.pictureID in self.pictures:
           file_path = self.pictures[self.pictureID]['file']

           self.image = self.load_and_resize_image(file_path)

           self.image_label.config(image=self.image)
           self.image_label.image = self.image

           self.pictureID += 1
           if self.pictureID > self.maxPicture:
               self.pictureID = 1
           home_frame.after(2500, self.showPicture, home_frame)
       else:
           messagebox.showerror("Error", "Unknown pictureID!")

   class Marquee(Canvas):
       def __init__(self, parent, text, font=('Verdana', 20, 'bold'), margin=10, borderwidth=1, relief='flat', fps=60, speed=2, colors=None):
           super().__init__(parent, borderwidth=borderwidth, relief=relief)

           self.fps = fps
           self.speed = speed
           self.colors = colors if colors else ['black', 'brown', 'indian red', 'goldenrod']
           self.color_cycle = itertools.cycle(self.colors)

           self.text1_id = self.create_text(0, -1000, text=text, anchor="w", tags=("text1",), font=font, fill=next(self.color_cycle))
           self.text2_id = self.create_text(0, -1000, text=text, anchor="w", tags=("text2",), font=font, fill=next(self.color_cycle))

           (x0, y0, x1, y1) = self.bbox("text1")
           width = (x1 - x0) + (2 * margin) + (2 * borderwidth)
           height = (y1 - y0) + (2 * margin) + (2 * borderwidth)
           self.configure(width=width, height=height)

           self.text_width = x1 - x0
           self.canvas_width = self.winfo_reqwidth()

           self.coords("text1", 0, int(height / 2))
           self.coords("text2", self.text_width, int(height / 2))

           self.animate()
           self.change_color()

       def animate(self):
           self.move("text1", -self.speed, 0)
           self.move("text2", -self.speed, 0)

           (x0, y0, x1, y1) = self.bbox("text1")
           (x0_copy, y0_copy, x1_copy, y1_copy) = self.bbox("text2")

           if x1 < 0:
               self.coords("text1", x1_copy, y0)
           if x1_copy < 0:
               self.coords("text2", x1, y0_copy)

           self.after(int(1000 / self.fps), self.animate)

       def change_color(self):
           new_color = next(self.color_cycle)
           self.itemconfig("text1", fill=new_color)
           self.itemconfig("text2", fill=new_color)
           self.after(500, self.change_color)

def home_page():
   global home_frame, home_page
   home_frame = tk.Frame(main_frame)
   home_frame.place(relwidth=1, relheight=1)
   HomeSlideshow(home_frame)

def open_profile_window():
   global existing_username, existing_password, existing_username2, existing_password2

   c.execute('SELECT username FROM customer')
   existing_username = c.fetchone()
   existing_username2 = existing_username[0]

   c.execute('SELECT password FROM customer')
   existing_password = c.fetchone()
   existing_password2 = existing_password[0]

   bg_image = PhotoImage(file=r"C:\Users\Vennis\Downloads\foodbackground.png")  # Replace with your image file

   # Create a label to hold the background image
   bg_label = tk.Label(profile_frame, image=bg_image)
   bg_label.place(relwidth=1, relheight=1)

   # Store a reference to the background image to prevent garbage collection
   profile_frame.bg_image = bg_image

   # Create a frame inside the profile window
   frame1 = tk.Frame(profile_frame, height=500, width=700, bg='light yellow')
   frame1.place(relx=0.5, rely=0.5, anchor='center')

   # Existing Username Label and Entry
   old_username_label = tk.Label(frame1, text="Current Username:", font=('verdana', 16, 'bold'), bg='light yellow')
   old_username_label.place(x=80, y=50)
   old_username_entry = tk.Entry(frame1, font=('arial', 16, 'bold'))
   old_username_entry.place(x=400, y=50)

   # Existing Password Label and Entry
   old_password_label = tk.Label(frame1, text="Current Password:", font=('verdana', 16, 'bold'), bg='light yellow')
   old_password_label.place(x=80, y=100)
   old_password_entry = tk.Entry(frame1, show='*', font=('arial', 16, 'bold'))
   old_password_entry.place(x=400, y=100)

   # New Username Label and Entry
   new_username_label = tk.Label(frame1, text="New Username:", font=('verdana', 16, 'bold'), fg='brown', bg='light yellow')
   new_username_label.place(x=80, y=150)
   new_username_entry = tk.Entry(frame1, font=('arial', 16, 'bold'))
   new_username_entry.place(x=400, y=150)

   # New Password Label and Entry
   new_password_label = tk.Label(frame1, text="New Password:", font=('verdana', 16, 'bold'), fg='brown', bg='light yellow')
   new_password_label.place(x=80, y=200)
   new_password_entry = tk.Entry(frame1, show='*', font=('arial', 16, 'bold'))
   new_password_entry.place(x=400, y=200)

   # Confirm New Password Label and Entry
   confirm_password_label = tk.Label(frame1, text="Confirm New Password:", font=('verdana', 16, 'bold'), fg='brown', bg='light yellow')
   confirm_password_label.place(x=80, y=250)
   confirm_password_entry = tk.Entry(frame1, show='*', font=('arial', 16, 'bold'))
   confirm_password_entry.place(x=400, y=250)

   # Function to save new username and password
   def save_profile():
       global existing_username, existing_password
       old_username = old_username_entry.get()
       old_password = old_password_entry.get()
       new_username = new_username_entry.get()
       new_password = new_password_entry.get()
       confirm_password = confirm_password_entry.get()

       # Validate old username and password
       try:
           c.execute("SELECT * FROM `customer` WHERE `username` = ?", (old_username,))
           if c.fetchone() is not None:
               if old_username == existing_username2 and old_password == existing_password2:
                   # Check if new passwords match
                   if new_password == confirm_password:
                       c.execute('''
                                   UPDATE customer
                                   SET username = ?,
                                       password = ?
                                   WHERE username = ?
                               ''', (
                           new_username, new_password, old_username))
                       conn.commit()
                       messagebox.showinfo("Success", "Profile updated successfully!")
                       old_username_entry.delete(0,'end')
                       old_password_entry.delete(0,'end')
                       new_username_entry.delete(0,'end')
                       new_password_entry.delete(0,'end')
                       confirm_password_entry.delete(0,'end')
                       #profile_frame.destroy()  # Close the profile window
                   else:
                       messagebox.showerror("Error", "New passwords do not match!")
               else:
                   messagebox.showerror("Error", "Invalid current username or password!")
           else:
               messagebox.showerror("Error", "Invalid username!")
       except Exception as e:
           messagebox.showerror('Error',f'Error Message: {e}')





   # Save Button
   save_button = tk.Button(frame1, text="SAVE & UPDATE", command=save_profile, font=('verdana', 16, 'bold'), bg='brown', fg='white', activebackground='yellow')
   save_button.place(x=350, y=400, anchor='center')

def profile_page():
   global profile_frame

   profile_frame = tk.Frame(main_frame)
   profile_frame.place(relwidth=1, relheight=1)
   open_profile_window()

def initialising_FoodMenu():
   global food_frame, food_canvas, drinks_canvas, drinks_frame, item_id, add_food_order, drinks_scrollbar, food_scrollbar, trv_order_cart, entry_order_id, entry_table_no, entry_remarks, price_Entry
   container = Frame(menu_frame)
   container.place(x=0, y=0, width=1920, height=1080)
   container.configure(bg='light yellow')

   food_canvas = Canvas(container)
   food_canvas.place(x=575, y=615, width=1150, height=930, anchor='center')
   food_canvas.configure(bg='light blue')

   food_scrollbar = Scrollbar(container, orient=VERTICAL, command=food_canvas.yview)
   food_scrollbar.place(x=1132, y=150, height=930)
   food_canvas.configure(yscrollcommand=food_scrollbar.set)

   drinks_canvas = Canvas(container)
   drinks_canvas.place(x=0, y=150, width=1150, height=930)

   drinks_scrollbar = Scrollbar(container, orient=VERTICAL, command=drinks_canvas.yview)
   drinks_scrollbar.place(x=1132, y=150, height=930)
   drinks_canvas.configure(yscrollcommand=drinks_scrollbar.set)

   header_frame = Frame(container)
   header_frame.place(x=0, y=0, width=1920, height=150)

   food_button = Button(header_frame, text="FOOD", font=('Verdana', 15, 'bold'), bg='light yellow',
                        activebackground='white', command=select_food_button)
   food_button.place(x=10, y=100)

   drinks_button = Button(header_frame, text="DRINKS", font=('Verdana', 15, 'bold'), bg='light yellow',
                          activebackground='white', command=select_drinks_button)
   drinks_button.place(x=100, y=100)

   restaurant_name = Label(header_frame, text='FOOD & DRINKS MENU', font=('Impact', 40), fg='black')
   restaurant_name.place(relx=0.5, rely=0.5, anchor='center')

   food_frame = Frame(food_canvas)
   food_frame.config(relief='groove', bd=4)
   food_canvas.create_window((0, 0), window=food_frame, anchor="nw")

   drinks_frame = Frame(drinks_canvas)
   drinks_frame.config(relief='groove', bd=4)
   drinks_canvas.create_window((0, 0), window=drinks_frame, anchor="nw")

   # -------------------Order Cart [start]----------------------------------------------------------
   cart_frame = Frame(container)
   cart_frame.config(relief='groove', bd=4)
   cart_frame.place(x=1150, y=150, width=770, height=930)

   lbl_order_cart = Label(cart_frame, text="Order Cart", font=('Impact', 30), fg='brown')
   lbl_order_cart.place(relx=0.4, rely=0.01)

   lbl_order_id = Label(cart_frame, text="Order ID:", font=('Verdana', 15, 'bold'), fg='brown')
   lbl_order_id.place(x=50, y=80)

   entry_order_id = Entry(cart_frame, font=('Verdana', 15), width=5)
   entry_order_id.place(x=180, y=80)
   entry_order_id.config(state='normal')
   entry_order_id.delete(0, END)
   entry_order_id.insert(0, order_id_2)
   entry_order_id.config(state='readonly')

   # lbl_table_no = Label(cart_frame, text="Table No:", font=('Verdana', 15, 'bold'), fg='brown')
   # lbl_table_no.place(relx=0.1, rely=0.2)
   # lbl_table_no.place(x=50, y=120)

   # entry_table_no = Entry(cart_frame, font=('Verdana', 15), width=5)
   # entry_table_no.place(relx=0.3, rely=0.2)
   # entry_table_no.place(x=180, y=120)

   delete_btn = Button(cart_frame, text="Delete Item", font=('Verdana', 12, 'bold'),
                       bg='dark red', fg='light yellow', command=delete_selected_item)
   delete_btn.place(x=50, y=650)

   btn_confirm_order = Button(cart_frame, text="Confirm Order", font=('Verdana', 12, 'bold'), bg='dark blue',
                              fg='light yellow', command=confirm_order)
   btn_confirm_order.place(x=190, y=650)

   # -------------------trv_order_cart [start]------------------------------------------------------
   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Arial', 14, 'bold'))
   style.configure("Treeview", font=('Arial', 14))  # Change body font size
   style.configure("Treeview", rowheight=40)
   style.map('Treeview', background=[('selected', 'lightblue')])
   style.configure("Treeview", fieldbackground="light yellow")

   trv_order_cart = ttk.Treeview(cart_frame, columns=(1, 2, 3, 4, 5), show='headings', selectmode='browse')
   trv_order_cart.heading(1, text='No.')
   trv_order_cart.heading(2, text='Item')
   trv_order_cart.heading(3, text='Qty')
   trv_order_cart.heading(4, text='RM')
   trv_order_cart.heading(5, text='Remarks')

   trv_order_cart.place(x=50, y=130)

   # Adjust column widths
   trv_order_cart.column(1, width=85, anchor='center')
   trv_order_cart.column(2, width=160, anchor='center')
   trv_order_cart.column(3, width=85, anchor='center')
   trv_order_cart.column(4, width=85, anchor='center')
   trv_order_cart.column(5, width=210, anchor='center')


   total_Price = Label(cart_frame, text='Total Price:', fg='brown', font=('Verdana', 15, 'bold'))
   total_Price.place(x=50, y=600)

   price_Entry = Entry(cart_frame, borderwidth=1, font=("Arial", 15, 'bold'), width=10)
   price_Entry.place(x=190, y=600)


def fetch_food_drinks_items(item_category):
  print(f"Fetching {item_category} items...")  # Debug print
  conn = sqlite3.connect('db_thewok1.db')
  cursor = conn.cursor()
  cursor.execute("SELECT item_name, item_description, item_price, item_calories, item_image_path FROM items WHERE item_category=?", (item_category,))
  rows = cursor.fetchall()
  conn.close()
  print(f"Fetched {len(rows)} {item_category} items")  # Debug print
  return rows


def display_items(category):
  print(f"Displaying {category}")
  items = fetch_food_drinks_items(category)
  frame = food_frame if category == "Food" else drinks_frame
  canvas = food_canvas if category == "Food" else drinks_canvas


  frame.grid_columnconfigure(0, minsize=345)
  frame.grid_columnconfigure(1, minsize=515)
  frame.grid_columnconfigure(2, minsize=200)


  for widget in frame.winfo_children():
      widget.destroy()


  # Dictionary to store quantity variables for each item
  quantity_vars = {}


  def create_update_quantity(item_id, item_name):
      def update_quantity(delta):
          print(f"Updating Quantity for {item_name}...")
          new_quantity = quantity_vars[item_id].get() + delta
          if new_quantity >= 0:
              quantity_vars[item_id].set(new_quantity)
      return update_quantity


  if items:
      for i, item in enumerate(items):
          # Create a separate quantity variable for each item
          item_id = item[0]  # Assuming the first element of item is a unique identifier
          quantity_vars[item_id] = IntVar(value=0)

          food_image = PhotoImage(file=item[4])
          img_resized = food_image.subsample(food_image.width() // 350, food_image.height() // 197)
          food_image_label = Label(frame, image=img_resized, width=350, height=197)
          food_image_label.image = img_resized
          food_image_label.grid(row=i * 3, column=0, padx=20, pady=10, rowspan=3)

          # Create a sub-frame for name and description
          info_frame = Frame(frame)
          info_frame.grid(row=i*3, column=1, padx=20, pady=5, sticky='w')


          name_lbl = Label(info_frame, text=f'{item[0]} RM {item[2]}', font=('times new roman', 20), fg='brown',
                           wraplength=438)
          name_lbl.pack(anchor='w', padx=20)


          des = Label(info_frame, text=f'{item[1]}\n({item[3]} calories per serving)',
                      font=('arial', 14), fg='grey', wraplength=438, justify=LEFT)
          des.pack(anchor='w', padx=20)


          # Create a frame for buttons and quantity labels
          interaction_frame = Frame(frame)
          interaction_frame.grid(row=i*3, column=2, padx=0, pady=5, sticky='w')


          # Button frame
          button_frame = Frame(interaction_frame)
          button_frame.pack(anchor='w')


          update_quantity = create_update_quantity(item_id, item[0])


          quantity_subtract_btn = Button(button_frame, text="-", font=('times new roman', 15), bg='light yellow',
                                         command=lambda d=update_quantity: d(-1))
          quantity_subtract_btn.pack(side=LEFT, padx=2)


          cart_btn = Button(button_frame, text='Add to Order 🛒', font=('times new roman', 15), bg='brown',
                               fg='white', activebackground='yellow',
                               command=lambda order_id=entry_order_id, name=item[0], price=item[2],
                                              qty=quantity_vars[item[0]]:
                               add_food_order(order_id.get(), name, price, qty.get()))
          cart_btn.pack(side=LEFT, padx=2)


          quantity_add_btn = Button(button_frame, text="+", font=('times new roman', 15), bg='light yellow',
                                    command=lambda d=update_quantity: d(1))
          quantity_add_btn.pack(side=LEFT, padx=2)


          # Quantity Labels
          qty_frame = Frame(interaction_frame)
          qty_frame.pack(anchor='w', pady=(5, 0))


          lbl_qty1 = Label(qty_frame, text="Quantity:", font=('times new roman', 15))
          lbl_qty1.pack(side=LEFT, padx=2)


          lbl_qty2 = Label(qty_frame, textvariable=quantity_vars[item_id], font=('times new roman', 15))
          lbl_qty2.pack(side=LEFT, padx=2)


  else:
      no_data_label = Label(frame, text=f"No {category.lower()} items found", font=('Verdana', 12))
      no_data_label.grid(row=0, column=0, columnspan=2, padx=20, pady=50)


  canvas.update_idletasks()
  canvas.config(scrollregion=canvas.bbox("all"))


def display_food():
  display_items("Food")


def display_drinks():
  display_items("Drinks")


def select_food_button():
  drinks_canvas.place_forget()
  drinks_scrollbar.place_forget()
  food_canvas.place(x=575, y=615, width=1150, height=930, anchor='center')
  food_scrollbar.place(x=1132, y=150, height=930)
  display_food()


def select_drinks_button():
  food_canvas.place_forget()
  food_scrollbar.place_forget()
  drinks_canvas.place(x=0, y=150, width=1150, height=930)
  drinks_scrollbar.place(x=1132, y=150, height=930)
  display_drinks()


#-----------------------------------------------------------------------------------------------------------------------
#                                         ORDER CART FUNCTIONS
#-----------------------------------------------------------------------------------------------------------------------

def enter_remark_dialog():
   global remark_entry_value
   remark_entry_value = ""

   def confirm_remark():
       global remark_entry_value
       #nonlocal remark_entry_value
       remark_entry_value = remark_entry.get()
       remark_dialog.destroy()

   def cancel_remark():
       remark_dialog.destroy()

   remark_dialog = tk.Toplevel(root)
   remark_dialog.title("Enter Remark")

   lbl_remark = ttk.Label(remark_dialog, text="Please enter your remark:")
   lbl_remark.pack(padx=10, pady=10)

   remark = tk.StringVar()
   remark_entry = ttk.Entry(remark_dialog, textvariable=remark, width=30)
   remark_entry.pack(padx=10, pady=5)

   btn_confirm = ttk.Button(remark_dialog, text="Confirm", command=confirm_remark)
   btn_confirm.pack(side=tk.LEFT, padx=10, pady=10)

   btn_cancel = ttk.Button(remark_dialog, text="Cancel", command=cancel_remark)
   btn_cancel.pack(side=tk.RIGHT, padx=10, pady=10)

   remark_dialog.transient(root)
   remark_dialog.grab_set()
   root.wait_window(remark_dialog)

   return remark_entry_value

# Function to add food order with optional remark
def add_food_order(order_ID, item_name, price, quantity):
   if quantity <= 0:
       messagebox.showwarning("Invalid Quantity", "Please select a quantity greater than 0.")
       return

   if not order_ID:
       messagebox.showwarning("Missing Information", "Please enter Order ID.")
       return

   remarks = ""
   if messagebox.askyesno("Remark", "Do you have a remark for this food item?"):
       remarks = enter_remark_dialog()

   try:
       conn = sqlite3.connect('db_thewok1.db')
       cursor = conn.cursor()

       # Fetch the correct item_id from the items table
       cursor.execute("SELECT item_id FROM items WHERE item_name = ?", (item_name,))
       item_id_result = cursor.fetchone()
       if item_id_result is None:
           messagebox.showerror("Error", f"Item '{item_name}' not found in the database.")
           return
       item_id = item_id_result[0]

       # Check if the item already exists in the order_items table for the given order_ID and remarks
       cursor.execute('''
           SELECT quantity, remarks
           FROM order_items
           WHERE order_id = ? AND item_name = ? AND remarks = ?
       ''', (order_ID, item_name, remarks))
       existing_item = cursor.fetchone()

       if existing_item:
           # Item exists with the same remarks, update the quantity
           new_quantity = existing_item[0] + quantity
           new_price = price * new_quantity

           cursor.execute('''
               UPDATE order_items
               SET quantity = ?, price = ?
               WHERE order_id = ? AND item_name = ? AND remarks = ?
           ''', (new_quantity, new_price, order_ID, item_name, remarks))
       else:
           # Item does not exist with the same remarks, insert a new row
           cursor.execute('''
               INSERT INTO order_items (order_id, item_id, item_name, quantity, price, remarks)
               VALUES (?, ?, ?, ?, ?, ?)
           ''', (order_ID, item_id, item_name, quantity, price * quantity, remarks))


       conn.commit()

       # Refresh the order cart display
       refresh_order_cart(order_ID)

   except sqlite3.Error as e:
       messagebox.showerror("Database Error", f"An error occurred: {e}")
   finally:
       if conn:
           conn.close()


def update_remarks():
   selected_items = trv_order_cart.selection()
   if not selected_items:
       messagebox.showwarning("No Selection", "Please select an item to update remarks.")
       return

   selected_item = selected_items[0]
   item = trv_order_cart.item(selected_item)
   item_name = item["values"][1]

   order_remarks = entry_remarks.get().strip()

   # Update the Treeview
   new_values = list(item["values"])
   new_values[4] = order_remarks
   trv_order_cart.item(selected_item, values=tuple(new_values))

   # Update the database
   try:
       conn = sqlite3.connect('db_thewok1.db')
       cursor = conn.cursor()

       cursor.execute("""
       UPDATE order_items
       SET remarks = ?
       WHERE order_id = ? AND item_name = ?
       """, (order_remarks, entry_order_id.get(), item_name))

       conn.commit()
   except sqlite3.Error as e:
       messagebox.showerror("Database Error", f"An error occurred: {e}")
   finally:
       if conn:
           conn.close()

   # Clear the remarks entry widget
   entry_remarks.delete(0, END)

   # Refresh the order cart display to reflect the updated data
   refresh_order_cart(order_id_2)


def delete_selected_item():
   selected_item = trv_order_cart.selection()
   if not selected_item:
       messagebox.showwarning("No Selection", "Please select an item to delete.")
       return

   result = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this item?")
   if not result:
       return

   item = trv_order_cart.item(selected_item[0])
   item_name = item['values'][1]
   item_quantity = int(item['values'][2])
   item_price = float(item['values'][3])
   item_remarks = item['values'][4] if len(item['values']) > 4 else ""
   order_id = entry_order_id.get()

   try:
       conn = sqlite3.connect('db_thewok1.db')
       cursor = conn.cursor()

       # Delete the specific item from order_items
       cursor.execute('''
           DELETE FROM order_items
           WHERE order_id = ? AND item_name = ? AND quantity = ? AND price = ? AND remarks = ?
       ''', (order_id, item_name, item_quantity, item_price, item_remarks))

       conn.commit()

       # Check if the order is now empty
       cursor.execute('SELECT COUNT(*) FROM order_items WHERE order_id = ?', (order_id,))
       item_count = cursor.fetchone()[0]

       if item_count == 0:
           # If the order is empty, delete it from the orders table
           cursor.execute('DELETE FROM orders WHERE order_id = ?', (order_id,))
           conn.commit()
           messagebox.showinfo("Order Deleted", f"Order {order_id} has been deleted as it's now empty.")
           entry_order_id.delete(0, END)  # Clear the order ID entry

       refresh_order_cart(order_id)

   except sqlite3.Error as e:
       messagebox.showerror("Database Error", f"An error occurred: {e}")
   finally:
       if conn:
           conn.close()


def refresh_order_cart(order_id):
   global trv_order_cart, root

   # Check if root exists and is a Tk instance
   if 'root' not in globals() or not isinstance(root, tk.Tk):
       print("Root window is not defined or not a Tk instance. Skipping refresh.")
       return


   # Try to find the order_cart_frame, create it if it doesn't exist
   try:
       order_cart_frame = root.nametowidget('order_cart_frame')
   except KeyError:
       print("Order cart frame does not exist. Creating a new one.")
       order_cart_frame = ttk.Frame(root, name='order_cart_frame')
       order_cart_frame.pack(fill='both', expand=True)

   # Check if trv_order_cart exists, if not, create it
   if 'trv_order_cart' not in globals() or not isinstance(trv_order_cart, ttk.Treeview):
       trv_order_cart = ttk.Treeview(order_cart_frame, columns=('No', 'Item', 'Quantity', 'Price', 'Remarks'), show='headings')
       trv_order_cart.heading('No', text='No')
       trv_order_cart.heading('Item', text='Item')
       trv_order_cart.heading('Quantity', text='Quantity')
       trv_order_cart.heading('Price', text='Price')
       trv_order_cart.heading('Remarks', text='Remarks')
       trv_order_cart.pack(fill='both', expand=True)

   # Clear existing items in the treeview
   for item in trv_order_cart.get_children():
       trv_order_cart.delete(item)

   try:
       conn = sqlite3.connect('db_thewok1.db')
       cursor = conn.cursor()

       cursor.execute('''
           SELECT item_name, quantity, price, remarks
           FROM order_items
           WHERE order_id = ?
       ''', (order_id,))
       items = cursor.fetchall()

       if items:
           for i, item in enumerate(items, start=1):
               trv_order_cart.insert('', 'end', values=(i, *item))
       else:
           # If no items, insert a placeholder row
           trv_order_cart.insert('', 'end', values=('No items in cart', '', '', '', ''))

       # Uncomment the next line if you have defined update_total_price function
       # update_total_price()

   except sqlite3.Error as e:
       messagebox.showerror("Database Error", f"An error occurred while refreshing the cart: {e}")
   finally:
       if conn:
           conn.close()

   # Schedule the next refresh
   if root.winfo_exists():
       root.after(1000, lambda: refresh_order_cart(order_id))
   else:
       print("Root window no longer exists. Stopping refresh.")
def update_total_price():
   global price_Entry, total_price
   order_id = entry_order_id.get()
   print(f"Updating total price for order ID: {order_id}")

   total_price = 0.00  # Initialize total_price to 0.00

   if not order_id:
       total_price = update_total_price()
       if price_Entry:
           price_Entry.config(state='normal')
           price_Entry.delete(0, tk.END)
           price_Entry.insert(0, f"{total_price:.2f}")
           price_Entry.config(state='readonly')
       print("No order ID provided, setting price to 0.00")
       return total_price  # Return the total_price

   try:
       conn = sqlite3.connect('db_thewok1.db')
       cursor = conn.cursor()

       # Calculate total price from order_items table
       cursor.execute('SELECT SUM(price) FROM order_items WHERE order_id = ?', (order_id,))
       result = cursor.fetchone()
       print(f"SQL Query Result: {result}")  # Debug print to check the result

       if result is None or result[0] is None:
           print(f"No items found for order ID {order_id}")
           total_price = 0.00
       else:
           total_price = result[0]
           print(f"Total price calculated: {total_price}")

       if price_Entry:
           price_Entry.config(state='normal')
           price_Entry.delete(0, tk.END)
           price_Entry.config(state='readonly')
           print(f"Total price updated to {total_price:.2f}")

   except sqlite3.Error as e:
       messagebox.showerror("Database Error", f"An error occurred: {e}")
       print(f"Database Error: {e}")

   finally:
       if conn:
           conn.close()
           print("Database connection closed")

   return total_price

def confirm_order():
   global total_price
   total_price = update_total_price()
   if price_Entry:
       price_Entry.config(state='normal')
       price_Entry.delete(0, tk.END)
       price_Entry.insert(0, f"{total_price:.2f}")
       price_Entry.config(state='readonly')
   order_id = entry_order_id.get()
   if not order_id:
      messagebox.showwarning("Missing Information", "Please enter Order ID.")
      return


   try:
      conn = sqlite3.connect('db_thewok1.db')
      cursor = conn.cursor()


      cursor.execute("""
      UPDATE orders
      SET order_status = 'Confirmed'
      WHERE order_ID = ?
      """, (order_id,))


      conn.commit()
      messagebox.showinfo("Success", f"Order {order_id} has been confirmed.")
      order_list_page()


      # Clear the treeview and reset counters
      trv_order_cart.delete(*trv_order_cart.get_children())
      global no_counter
      no_counter = 0
      update_total_price()


   except sqlite3.Error as e:
      messagebox.showerror("Database Error", f"An error occurred: {e}")
   finally:
      if conn:
          conn.close()

def order_list_page():
   global order_list_frame1
   order_list_frame1 = tk.Frame(main_frame)
   order_list_frame1.place(relwidth=1, relheight=1)
   order_list()

def card_payment():
   #clear_previous_frames()
   global payby_label, mainframe, frame1, frame2, payby_label2
   order_list_frame.destroy()
   if payby_label2:
       payby_label2.destroy()
   if payby_label:
       payby_label.destroy()

   mainframe = Frame(order_list_frame1, height=1080, width=1920)
   mainframe.place(x=0, y=0)

   back_button = Button(mainframe, text='< Back', width=10, background='blue', fg='white', font=('verdana', 12),command=order_list)
   back_button.place(x=500, y=140)

   frame1 = Frame(mainframe, height=820, width=550, relief='groove', bd=2)
   frame1.place(x=960, y=540, anchor='center')

   label1 = Label(frame1, text='Fill in Payment Details', font=('verdana', 20, 'bold'), fg='black')
   label1.place(x=275, y=40, anchor='center')

   cost_label = Label(frame1, text='Total Cost:', font=('verdana', 18), fg='brown')
   cost_label.place(x=275, y=90, anchor='center')

   entry_total = Entry(frame1, font=('verdana', 18), fg='brown', width=20)
   entry_total.place(x=275, y=125, anchor='center')
   entry_total.config(state='normal')
   entry_total.delete(0, END)
   total_price = update_total_price()  # Call update_total_price and store the returned value
   entry_total.insert(0, f"{total_price:.2f}")
   entry_total.config(state='readonly')


   payby_label = Label(frame1, text='Pay by: Card', font=('verdana',15), fg='black')
   payby_label.place(x=275,y=170, anchor='center')

   frame2 = Frame(frame1, height=580, width=500, relief='groove', bd=2)
   frame2.place(x=25, y=200)

   name_label = Label(frame2, text='Name:',font=('verdana',18),fg='brown')
   name_label.place(x=45,y=50, anchor='w')

   name_entry = Entry(frame2, font=('verdana',18), fg='black', width=15)
   name_entry.place(x=225, y=35)

   cardNum_label = Label(frame2, text='Card No:', font=('verdana', 18), fg='brown')
   cardNum_label.place(x=45, y=120, anchor='w')

   cardNum_entry = Entry(frame2, font=('verdana', 18), fg='black', width=15)
   cardNum_entry.place(x=225, y=105)

   expired_label = Label(frame2, text='Expiry Date:', font=('verdana', 18), fg='brown')
   expired_label.place(x=45, y=190, anchor='w')

   expired_entry = Entry(frame2, font=('verdana', 18), fg='black', width=15)
   expired_entry.place(x=225, y=175)

   cvv_label = Label(frame2, text='CVV No:', font=('verdana', 18), fg='brown')
   cvv_label.place(x=45, y=260, anchor='w')

   cvv_entry = Entry(frame2, font=('verdana', 18), fg='black', width=15)
   cvv_entry.place(x=225, y=245)

   payment_btn = Button(frame2, text='Proceed Payment', font=('verdana',15), fg='black', bg='light yellow', activebackground='brown',
                        command=lambda: proceed_payment(name_entry.get(), cardNum_entry.get(), expired_entry.get(), cvv_entry.get()))
   payment_btn.place(x=250, y=480, anchor='center')


def tng_payment():
   global payby_label2, mainframe, frame2, payby_label, entry_total, order_list_frame1, order_list_frame

   order_list_frame.destroy()

   mainframe = Frame(order_list_frame1, height=1080, width=1920)
   mainframe.place(x=0, y=0)

   back_button = Button(mainframe, text='< Back', width=10, background='blue', fg='white', font=('verdana', 12), command=order_list)
   back_button.place(x=500, y=140)

   frame2 = Frame(mainframe, height=820, width=550, relief='groove', bd=2)
   frame2.place(x=960, y=540, anchor='center')

   label1 = Label(frame2, text='Fill in Payment Details', font=('verdana', 20, 'bold'), fg='black')
   label1.place(x=275, y=40, anchor='center')

   cost_label = Label(frame2, text='Total Cost:', font=('verdana', 18), fg='brown')
   cost_label.place(x=275, y=90, anchor='center')

   entry_total = Entry(frame2, font=('verdana', 18), fg='brown', width=20)
   entry_total.place(x=275, y=125, anchor='center')
   entry_total.config(state='normal')
   entry_total.delete(0, END)
   total_price = update_total_price()  # Call update_total_price and store the returned value
   entry_total.insert(0, f"{total_price:.2f}")
   entry_total.config(state='readonly')

   payby_label = Label(frame2, text='Pay by: Touch N Go', font=('verdana', 15), fg='black')
   payby_label.place(x=275, y=170, anchor='center')

   frame3 = Frame(frame2, height=580, width=500, relief='groove', bd=2)
   frame3.place(x=25, y=200)

   name_label = Label(frame3, text='Name:', font=('verdana', 18), fg='brown')
   name_label.place(x=45, y=50, anchor='w')

   name_entry = Entry(frame3, font=('verdana', 18), fg='black', width=15)
   name_entry.place(x=225, y=35)

   phoneNum_label = Label(frame3, text='Phone No:', font=('verdana', 18), fg='brown')
   phoneNum_label.place(x=45, y=120, anchor='w')

   phoneNum_entry = Entry(frame3, font=('verdana', 18), fg='black', width=15)
   phoneNum_entry.place(x=225, y=105)

   pass_label = Label(frame3, text='Security Pin:', font=('verdana', 18), fg='brown')
   pass_label.place(x=45, y=190, anchor='w')

   pass_entry = Entry(frame3, font=('verdana', 18), fg='black', width=15)
   pass_entry.place(x=225, y=175)

   payment_btn = Button(frame3, text='Proceed Payment', font=('verdana', 15), fg='black', bg='light yellow', activebackground='brown',
                        command=lambda: proceed_payment(name_entry.get(), phoneNum_entry.get(), pass_entry.get()))
   payment_btn.place(x=250, y=480, anchor='center')

   if payby_label:
       payby_label.destroy()
   if payby_label2:
       payby_label2.destroy()


def proceed_payment(*args):
   if not all(args):
       messagebox.showerror("Input Error", "Please fill in all fields")
   else:
       # Implement your payment logic here
       print("Proceeding with payment")
       mainframe.destroy()
       receipt()


# Function to fetch order data from the database
def fetch_order_data(order_id_2):
   # Replace with your database connection and query
   conn = sqlite3.connect('db_thewok1.db')
   cursor = conn.cursor()
   cursor.execute("SELECT item_id, item_name, quantity, price, remarks, order_id  FROM order_items WHERE order_id = ?", (order_id_2,))  # Adjust the query as needed
   rows = cursor.fetchall()
   conn.close()
   return rows

# Function to populate Treeviews with fetched data
def populate_treeviews(data):
   #for item in trv_order_cart.get_children():
       #trv_order_cart.delete(item)
   for item in trv_order_list.get_children():
       trv_order_list.delete(item)

   for row in data:
       trv_order_cart.insert("", "end", values=row)
       trv_order_list.insert("", "end", values=row)

# Function to create the order list frame and populate it
def order_list():
   global order_list_frame, trv_order_list, trv_order_cart, order_list_frame1, entry_total

   order_list_frame1.destroy()
   order_list_frame1 = Frame(main_frame)
   order_list_frame1.place(relwidth=1, relheight=1)

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Arial', 14, 'bold'))
   style.configure("Treeview", font=('Arial', 12))  # Change body font size
   style.configure("Treeview", rowheight=25)
   style.map('Treeview', background=[('selected', 'lightblue')])
   style.configure("Treeview", fieldbackground="light yellow")

   order_list_frame = Frame(order_list_frame1, relief=GROOVE, bd=1)
   order_list_frame.place(x=500, y=15, width=950, height=1000)
   order_list_frame.configure(bg='light yellow')

   trv_order_list = ttk.Treeview(order_list_frame, columns=(1, 2, 3, 4, 5, 6), show='headings', selectmode='browse', height=20)
   trv_order_list.heading(1, text='Item ID')
   trv_order_list.heading(2, text='Item')
   trv_order_list.heading(3, text='Qty')
   trv_order_list.heading(4, text='RM')
   trv_order_list.heading(5, text='Remarks')
   trv_order_list.heading(6, text='Status')
   trv_order_list.place(x=70, y=200)

   trv_order_list.column(1, width=80, anchor='center')
   trv_order_list.column(2, width=190, anchor='center')
   trv_order_list.column(3, width=80, anchor='center')
   trv_order_list.column(4, width=100, anchor='center')
   trv_order_list.column(5, width=210, anchor='center')
   trv_order_list.column(6, width=120, anchor='center')


   lbl_title = Label(order_list_frame, text="Order List", font=('Impact', 35), fg='brown', bg="light yellow")
   lbl_title.place(x=475, y=50, anchor='center')

   lbl_order_id = Label(order_list_frame, text="Order ID:", font=('Verdana', 18, 'bold'), fg='black', bg='light yellow')
   lbl_order_id.place(x=70, y=130)

   entry_order_id = Entry(order_list_frame, text="", font=('Verdana', 15), width=8)
   entry_order_id.place(x=210, y=135)
   entry_order_id.config(state='normal')
   entry_order_id.delete(0, END)
   entry_order_id.insert(0, order_id_2)
   entry_order_id.config(state='readonly')

   lbl_total = Label(order_list_frame, text="Total:", font=('Verdana', 15, 'bold'), fg='black', bg='light yellow')
   lbl_total.place(x=70, y=750)

   entry_total = Entry(order_list_frame, font=('Verdana', 15), width=8)
   entry_total.place(x=150, y=750)
   price_Entry= entry_total
   price_Entry.config(state='normal')
   price_Entry.delete(0, END)
   total_price = update_total_price()  # Call update_total_price and store the returned value
   price_Entry.insert(0, f"{total_price:.2f}")
   price_Entry.config(state='readonly')



   lbl_pay_by = Label(order_list_frame, text="Pay by:", font=('Verdana', 15, 'bold'), fg='black', bg='light yellow')
   lbl_pay_by.place(x=70, y=800)

   btn_tng = Button(order_list_frame, text="TnG", font=('Verdana', 15, 'bold'), bg='brown', fg='light yellow', width=10, command=tng_payment)
   btn_tng.place(x=70, y=850)

   btn_card = Button(order_list_frame, text="Debit/Credit", font=('Verdana', 15, 'bold'), bg='brown', fg='light yellow', width=15, command=card_payment)
   btn_card.place(x=250, y=850)

   data = fetch_order_data(order_id_2)
   populate_treeviews(data)

# Function to create the cart frame and populate it
def create_cart_frame(cart_frame):
   global trv_order_cart

   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Arial', 14, 'bold'))
   style.configure("Treeview", font=('Arial', 14))  # Change body font size
   style.configure("Treeview", rowheight=40)
   style.map('Treeview', background=[('selected', 'lightblue')])
   style.configure("Treeview", fieldbackground="light yellow")

   trv_order_cart = ttk.Treeview(cart_frame, columns=(1, 2, 3, 4, 5), show='headings', selectmode='browse')
   trv_order_cart.heading(1, text='No.')
   trv_order_cart.heading(2, text='Item')
   trv_order_cart.heading(3, text='Qty')
   trv_order_cart.heading(4, text='RM')
   trv_order_cart.heading(5, text='Remarks')
   trv_order_cart.place(x=50, y=130)

   # Adjust column widths
   trv_order_cart.column(1, width=85, anchor='center')
   trv_order_cart.column(2, width=160, anchor='center')
   trv_order_cart.column(3, width=85, anchor='center')
   trv_order_cart.column(4, width=85, anchor='center')
   trv_order_cart.column(5, width=210, anchor='center')


   order_id_2 = 1  # Replace with actual order_id_2
   order_list()

def setup_database():
   conn = sqlite3.connect('db_thewok1.db')
   cursor = conn.cursor()

   # Check if bill_number column exists, if not, add it
   cursor.execute("PRAGMA table_info(orders)")
   columns = [column[1] for column in cursor.fetchall()]
   if 'bill_number' not in columns:
       cursor.execute('ALTER TABLE orders ADD COLUMN bill_number TEXT')

       # Create a unique index for bill_number
       cursor.execute(
           'CREATE UNIQUE INDEX IF NOT EXISTS idx_bill_number ON orders (bill_number) WHERE bill_number IS NOT NULL')

   conn.commit()
   conn.close()


# Function to generate a unique bill number
def generate_bill_number():
   conn = sqlite3.connect('db_thewok1.db')
   cursor = conn.cursor()

   while True:
       cursor.execute("SELECT COUNT(*) FROM orders WHERE bill_number IS NOT NULL")
       count = cursor.fetchone()[0]
       new_bill_number = f"BILL-{count + 1:04d}"

       # Check if this bill number already exists
       cursor.execute("SELECT 1 FROM orders WHERE bill_number = ?", (new_bill_number,))
       if not cursor.fetchone():
           break

   conn.close()
   return new_bill_number


# Modified download_receipt function
def download_receipt():
   order_id = orderNo_Entry.get()
   if not order_id:
       messagebox.showerror("Error", "Please enter an Order ID")
       return

   conn = sqlite3.connect('orders.db')
   cursor = conn.cursor()

   # Check if order exists and get its details
   cursor.execute("SELECT * FROM orders WHERE order_id = ?", (order_id,))
   order = cursor.fetchone()
   if not order:
       messagebox.showerror("Error", f"No order found with ID {order_id}")
       conn.close()
       return

   # Assuming the structure: order_id, visit_id, total_price, order_status, bill_number
   order_id, visit_id, total_price, order_status, bill_number = order

   # Generate bill number if not exists
   if not bill_number:
       bill_number = generate_bill_number()
       cursor.execute("UPDATE orders SET bill_number = ? WHERE order_id = ?",
                      (bill_number, order_id))
       conn.commit()

   # Fetch order items
   cursor.execute("""
      SELECT oi.items_name, oi.quantity, oi.price
      FROM order_items oi
      WHERE oi.order_id = ?
  """, (order_id,))
   rows = cursor.fetchall()

   conn.close()

   if not rows:
       messagebox.showwarning("No Data", "No items found for this order.")
       return

   file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
   if not file_path:
       return

   pdf = FPDF()
   pdf.add_page()
   pdf.set_font("Helvetica", size=12)

   # Header
   pdf.set_font('Helvetica', 'B', 14)
   pdf.cell(0, 10, "The WOK Restaurant - Receipt", 0, 1, 'C')
   pdf.set_font('Helvetica', '', 12)
   pdf.cell(0, 10, f"Order ID: {order_id}", 0, 1, 'L')
   pdf.cell(0, 10, f"Bill Number: {bill_number}", 0, 1, 'L')
   pdf.cell(0, 10, f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'L')
   pdf.cell(0, 10, f"Order Status: {order_status}", 0, 1, 'L')
   pdf.ln(10)

   # Table Header
   pdf.set_font('Helvetica', 'B', 12)
   pdf.cell(10, 10, "No", 1, 0, 'C', True)
   pdf.cell(80, 10, "Item", 1, 0, 'C', True)
   pdf.cell(30, 10, "Price", 1, 0, 'C', True)
   pdf.cell(30, 10, "Quantity", 1, 0, 'C', True)
   pdf.cell(40, 10, "Total", 1, 1, 'C', True)

   # Table Content
   pdf.set_font('Helvetica', '', 12)
   total_price_calculated = 0
   for i, (item_name, quantity, price) in enumerate(rows, 1):
       item_total = price * quantity
       total_price_calculated += item_total

       pdf.cell(10, 10, str(i), 1, 0, 'C')
       pdf.cell(80, 10, item_name, 1, 0, 'L')
       pdf.cell(30, 10, f"RM{price:.2f}", 1, 0, 'R')
       pdf.cell(30, 10, str(quantity), 1, 0, 'C')
       pdf.cell(40, 10, f"RM{item_total:.2f}", 1, 1, 'R')

   # Totals
   pdf.set_font('Helvetica', 'B', 12)
   pdf.cell(150, 10, "Grand Total:", 1, 0, 'R', True)
   pdf.cell(40, 10, f"RM{total_price:.2f}", 1, 1, 'R', True)

   # Add a note if calculated total doesn't match stored total
   if abs(total_price - total_price_calculated) > 0.01:  # Allow for small floating-point discrepancies
       pdf.set_font('Helvetica', '', 10)
       pdf.cell(0, 10,
                "Note: The calculated total may differ from the stored total due to discounts or other adjustments.",
                0, 1, 'L')

   pdf.output(file_path)
   messagebox.showinfo("Success", "Receipt Downloaded!")
   os.startfile(file_path)


# -----------------------------------------------------------------------------------------------------------------------
# Receipt GUI
# -----------------------------------------------------------------------------------------------------------------------

def receipt():
   global orderNo_Entry
   RmainFrame = Frame(order_list_frame1, width=550, height=900, bd=1, relief=GROOVE, bg='light yellow')
   RmainFrame.place(x=700, y=50)

   infoFrame = Frame(RmainFrame, width=450, height=100)
   infoFrame.place(relx=0.5, rely=0.08, anchor=CENTER)  # Centering the infoFrame within mainFrame

   restaurantInfo = Label(infoFrame,
                          text='THE WOK RESTAURANT\n123, Penang Street, 11900, Penang, Malaysia.\n+6012- 345 6789',
                          font=('Verdana', 16, 'bold'), fg='brown', wraplength=450, justify=CENTER,
                          bg='light yellow')
   restaurantInfo.pack(fill="both", expand=True, padx=0, pady=0)

   lineBanner = Label(RmainFrame,
                      text='------------------------------------------------------------------------------------------------------',
                      fg='grey', bg='light yellow')
   lineBanner.place(x=15, y=130)

   receipt = Label(RmainFrame, text='Receipt', font=('Verdana', 14, 'bold'), fg='black', bg='light yellow')
   receipt.place(relx=0.5, rely=0.19, anchor=CENTER)

   orderNo = Label(RmainFrame, text='Order ID', font=('Verdana', 12, 'bold'), fg='brown', bg='light yellow')
   orderNo.place(x=15, y=200)

   orderNo_Entry = Entry(RmainFrame, borderwidth=1, font=('Verdana', 12, 'bold'), fg='brown')
   orderNo_Entry.place(x=120, y=200, height=20, width=100)


   dateTime = Label(RmainFrame, text='Date/ Time:', font=('Verdana', 12), fg='black', bg='light yellow')
   dateTime.place(x=15, y=230)
   dateTime_Entry = Entry(RmainFrame, borderwidth=1, font=('Verdana', 12), fg='black')
   dateTime_Entry.place(x=130, y=230, height=20, width=100)
   Time_Entry = Entry(RmainFrame, borderwidth=1, font=('Verdana', 12), fg='black')
   Time_Entry.place(x=430, y=230, height=20, width=100)

   # Treeview
   style = ttk.Style()
   style.configure("Treeview.Heading", font=('Verdana', 12, 'bold'))
   style.configure("Treeview", font=('Verdana', 12))  # Change body font size
   style.configure("Treeview", rowheight=40)
   style.map('Treeview', background=[('selected', 'lightblue')])
   style.configure("Treeview", fieldbackground="light yellow")

   # Create a Treeview widget
   tree = ttk.Treeview(RmainFrame, columns=(1, 2, 3, 4), show='headings')
   tree.heading(1, text='No')
   tree.heading(2, text='Item')
   tree.heading(3, text='Qty')
   tree.heading(4, text='RM')

   # Adjust column widths
   tree.column(1, width=70, anchor='center')
   tree.column(2, width=250)
   tree.column(3, width=70, anchor='center')
   tree.column(4, width=70, anchor='center')

   tree.place(x=15, y=280, width=520, height=400)


   total = Label(RmainFrame, text='Grand Total:', font=('Verdana', 14, 'bold'), fg='brown', bg='light yellow')
   total.place(x=15, y=720)
   entry_total = Entry(RmainFrame, font=('verdana', 18), fg='brown', width=20)
   entry_total.place(x=170, y=720, height=30, width=120)
   entry_total.config(state='normal')
   entry_total.delete(0, END)
   total_price = update_total_price()  # Call update_total_price and store the returned value
   entry_total.insert(0, f"{total_price:.2f}")
   entry_total.config(state='readonly')

   btn_pdf = Button(RmainFrame, text="Print PDF", font=('Verdana', 14, 'bold'), bg='brown', fg='light yellow',
                    command=download_receipt)
   btn_pdf.place(x=200, y=800)


def menu_page():
   global menu_frame
   menu_frame = tk.Frame(main_frame)
   menu_frame.place(relwidth=1, relheight=1)
   initialising_FoodMenu()
   select_food_button()

def Database():
   global conn, cursor
   conn = sqlite3.connect("db_thewok1.db")
   conn.execute("PRAGMA busy_timeout = 30000")  # wait for 30 seconds if the database is locked
   conn.execute("PRAGMA journal_mode = WAL")  # enable WAL mode
   cursor = conn.cursor()
   cursor.execute(
       "CREATE TABLE IF NOT EXISTS reservations(reservation_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
       "reservation_pax INTEGER NOT NULL, reservation_date TEXT NOT NULL, reservation_time TEXT NOT NULL, "
       "reservation_comments TEXT, cust_id INTEGER, FOREIGN KEY (cust_id) REFERENCES customer(cust_id))"
   )

   cursor.execute(
       "CREATE TABLE IF NOT EXISTS `customer` (cust_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, username TEXT, "
       "password TEXT, fullname TEXT, email TEXT, phone_no TEXT)")

   cursor.execute("""
          CREATE TABLE IF NOT EXISTS orders (
              order_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              cust_id INTEGER,
              food_id INTEGER,
              table_no INTEGER,
              FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
              FOREIGN KEY (food_id) REFERENCES food_items(food_id)
          )
      """)

   cursor.execute("""
          CREATE TABLE IF NOT EXISTS visiting (
          visit_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
          cust_id INTEGER,
          table_no INTEGER,
          FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
          )
      """)
   conn.commit()


def book_table():
   global empty
   #name = customer_name.get()
   pax = combobox_pax.get()
   date = entry_date.get()
   time = entry_time.get()
   comments = text_comments.get("1.0", "end-1c")  # Get all text from the text widget
   if comments == "" or comments == " ":
       comments = "None"

   if not pax or not date or not time or not comments:
       messagebox.showerror("Input Error", "Please fill in all fields")
   else:
       # Here you would include the logic to insert the reservation data into the database
       messagebox.showinfo("Success", "Table booked successfully!")
       empty =''
       new_id = get_reservation_id()
       conn.execute(
           "INSERT INTO reservations (reservation_id, reservation_name, reservation_contact, reservation_pax, reservation_date, reservation_time, reservation_comments, reservation_status) VALUES (?,?,?,?,?,?,?,?)",
           (new_id, cust_name, contact, pax, date, time, comments, empty))
       conn.commit()


def mainReservation():
   global entry_name, combobox_pax, entry_time, text_comments, entry_date

   reservation_bg_image = PhotoImage(file=r"C:\Users\Vennis\Downloads\reservation_bg.png")

   reservation_bg_label = tk.Label(reservationMain_frame, image=reservation_bg_image)
   reservation_bg_label.place(relwidth=1, relheight=1)

   reservation_frame = Frame(reservationMain_frame, bg='light yellow')
   reservation_frame.place(x=960, y=500, width=1100, height=650, anchor='center')
   reservationMain_frame.bg_image = reservation_bg_image

   lbl_the_wok = tk.Label(reservation_frame, text=f"{restaurant_name4}", font=('Verdana', 30, 'bold'), fg='brown', bg='light yellow')
   lbl_the_wok.place(x=550, y=60, anchor='center')

   lbl_book_your_spot = tk.Label(reservation_frame, text="Reserve Your Spot!", font=('Verdana', 20, 'bold'), bg='light yellow')
   lbl_book_your_spot.place(x=550, y=130, anchor='center')

   #lbl_name = tk.Label(reservation_frame, text='Name:', font=('Verdana', 15,'bold'), fg='black', bg='light yellow')
   #lbl_name.place(x=100, y=200)

   #entry_name = tk.Entry(reservation_frame, font=('Verdana', 15),fg='black')
   #entry_name.place(x=350, y=200, width=250)

   lbl_pax = tk.Label(reservation_frame, text='PAX:', font=('Verdana', 15,'bold'), fg='black', bg='light yellow')
   lbl_pax.place(x=100, y=200)

   pax_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 30]
   selected = IntVar(root)
   combobox_pax = ttk.Combobox(reservation_frame, font=('Verdana', 15), textvariable=selected, values=pax_no, width=6)
   combobox_pax.place(x=350, y=200)

   lbl_date = tk.Label(reservation_frame, text='Date (Eg: 1 Jan):', font=('Verdana', 15,'bold'),fg='black', bg='light yellow')
   lbl_date.place(x=100, y=250)

   entry_date = tk.Entry(reservation_frame, font=('Verdana', 15,'bold'),fg='blue')
   entry_date.place(x=350, y=250, width=300)

   lbl_time = tk.Label(reservation_frame, text='Arrival Time:', font=('Verdana', 15,'bold'), fg='black', bg='light yellow')
   lbl_time.place(x=100, y=300)

   entry_time = tk.Entry(reservation_frame, font=('Verdana', 15,'bold'),fg='blue')
   entry_time.place(x=350, y=300)

   lbl_comments = tk.Label(reservation_frame, text='Comments:', font=('Verdana', 15,'bold'), fg='black', bg='light yellow')
   lbl_comments.place(x=100, y=350)

   text_comments = tk.Text(reservation_frame, font=('Verdana', 15), height=3, width=45, fg='black')
   text_comments.place(x=350, y=350)

   book_button = tk.Button(reservation_frame, text="Book a Table", font=('Verdana', 15, 'bold'), command=book_table, bg='brown', fg='light yellow', width=15)
   book_button.place(x=550, y=550, anchor='center')


   Database()


def reservation_page():
   global reservationMain_frame
   reservationMain_frame = tk.Frame(main_frame)
   reservationMain_frame.place(relwidth=1, relheight=1)
   mainReservation()


def customer_review():
   def Database():
       global conn, cursor
       conn = sqlite3.connect("db_thewok1.db")
       conn.execute("PRAGMA busy_timeout = 30000")  # wait for 30 seconds if the database is locked
       conn.execute("PRAGMA journal_mode = WAL")  # enable WAL mode

       cursor = conn.cursor()
       cursor.execute(
           "CREATE TABLE IF NOT EXISTS reviews(review_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, customer_rating INTEGER NOT NULL, customer_review TEXT NOT NULL, cust_id INT, FOREIGN KEY (cust_id) REFERENCES customer(cust_id))"
       )
       conn.commit()

   def update_stars(event):
       rating = int(ratings_combobox.get().strip())
       for i in range(5):
           if i < rating:
               stars[i].config(fg='#EBA743')
           else:
               stars[i].config(fg='white')

   def submit_review():
       name = customer_name.get().strip()
       rating = ratings_combobox.get().strip()
       review = review_text.get("1.0", tk.END).strip()

       if name and rating and review:
           try:
               with sqlite3.connect("db_thewok1.db") as conn:
                   cursor = conn.cursor()
                   cursor.execute("SELECT cust_id FROM customer WHERE username = ?", (name,))
                   cust_id = cursor.fetchone()
                   if cust_id:
                       cust_id = cust_id[0]
                       # Insert review into the database
                       cursor.execute(
                           "INSERT INTO reviews(cust_id, customer_rating, customer_review) VALUES (?, ?, ?)",
                           (cust_id, rating, review))
                       conn.commit()
                       messagebox.showinfo("Success", "Thank you for the review!")

                       fetch_reviews()
                       display_review(current_review_index)

                       write_review_window.destroy()
                   else:
                       messagebox.showerror("Error", "Customer not found!")
           except sqlite3.Error as e:
               messagebox.showerror("Error", f"Error submitting review: {e}")
       else:
           messagebox.showerror("Error", "Please fill in all fields!")

   def fetch_reviews():
       global reviews
       try:
           with sqlite3.connect("db_thewok1.db") as conn:
               cursor = conn.cursor()
               # Fetch data from the database
               cursor.execute("""
                  SELECT c.username, r.customer_rating, r.customer_review
                  FROM reviews r
                  JOIN customer c ON r.cust_id = c.cust_id
              """)
               reviews = cursor.fetchall()
       except sqlite3.Error as e:
           messagebox.showerror("Error", f"Error fetching review data: {e}")

   def display_review(index):
       if not reviews:
           messagebox.showinfo("Info", "No reviews available.")
           return

       if index < 0 or index >= len(reviews):
           messagebox.showinfo("Info", "No more reviews.")
           return

       review = reviews[index]
       customer_label.config(text=f"Customer: {review[0]}")
       rating_label.config(text=f"Rating: {'★' * review[1]}")
       review_label.config(text=f"Review: {review[2]}")

   def next_review():
       global current_review_index
       current_review_index += 1
       if current_review_index >= len(reviews):
           current_review_index = 0  # Loop back to the first review
       display_review(current_review_index)

   def previous_review():
       global current_review_index
       current_review_index -= 1
       if current_review_index < 0:
           current_review_index = len(reviews) - 1  # Loop back to the last review
       display_review(current_review_index)

   def write_review_window():
       global ratings_combobox, review_text, stars, customer_name

       # Create new window for writing Food Review
       write_review_window = Toplevel(root)
       write_review_window.title("Write Review")
       write_review_window.configure(bg='light blue')
       write_review_window.geometry("1280x720")

       # -----------------WIDGETS FOR USER INPUT-----------------

       lbl_review = tk.Label(write_review_window, text="Your Review Matters!", font=('Verdana', 30, 'bold'),
                             fg='#A52A2A',bg='light blue')
       lbl_review.place(x=640, y=100, anchor='center')

       lbl_name = tk.Label(write_review_window, text="Name:", font=('Verdana', 15, 'bold'),bg='light blue')
       lbl_name.place(x=60, y=240)

       customer_name = tk.Entry(write_review_window, font=('Verdana', 15))
       customer_name.place(x=180, y=240)

       lbl_rating = tk.Label(write_review_window, text="Rating:", font=('Verdana', 15, 'bold'),bg='light blue')
       lbl_rating.place(x=60, y=310)

       ratings = [1, 2, 3, 4, 5]

       ratings_combobox = ttk.Combobox(write_review_window, font=('Verdana', 15), values=ratings, width=2)
       ratings_combobox.place(x=180, y=310)
       ratings_combobox.bind("<<ComboboxSelected>>", update_stars)

       stars = []
       for i in range(5):
           star = tk.Label(write_review_window, text="★", font=('Verdana', 20), fg='white',bg='light blue')
           star.place(x=240 + i * 40, y=300)
           stars.append(star)

       lbl_review = tk.Label(write_review_window, text="Review:", font=('Verdana', 15, 'bold'),bg='light blue')
       lbl_review.place(x=60, y=370)

       review_text = tk.Text(write_review_window, font=('Verdana', 15), height=5, width=75)
       review_text.place(x=180, y=370)

       button_submit = tk.Button(write_review_window, text="Submit Review", font=('Verdana', 15, 'bold'),
                                 command=submit_review, bg='#A52A2A', fg='#EEE3AD')
       button_submit.place(x=180, y=510)

   # Initialize database connection
   Database()

   review1_frame = Frame(review_frame, bg='#EEE3AD', bd=2, relief="groove")
   review1_frame.place(x=230, y=320, width=1500, height=400)

   customer_label = tk.Label(review1_frame, text="", font=('Verdana', 20, 'bold'), bg='#EEE3AD', wraplength=1200)
   customer_label.place(x=750, y=100, anchor=CENTER)

   rating_label = tk.Label(review1_frame, text="", font=('Verdana', 20), bg='#EEE3AD', wraplength=1200)
   rating_label.place(x=750, y=150, anchor=CENTER)

   review_label = tk.Label(review1_frame, text="", font=('Verdana', 18), wraplength=1200, justify=LEFT, bg='#EEE3AD')
   review_label.place(x=750, y=200, anchor=CENTER)

   # Buttons to navigate reviews
   back_button = tk.Button(review_frame, text="Back", font=('Verdana', 15, 'bold'), command=previous_review,
                           bg='#A52A2A', fg='#EEE3AD', width=10)
   back_button.place(x=230, y=730)

   next_button = tk.Button(review_frame, text="Next", font=('Verdana', 15, 'bold'), command=next_review, bg='#A52A2A',
                           fg='#EEE3AD', width=10)
   next_button.place(x=1580, y=730)

   # Fetch and display the reviews
   fetch_reviews()
   display_review(current_review_index)

   lbl_the_wok = tk.Label(review_frame, text=f"{restaurant_name4}", font=('Verdana', 30, 'bold'),
                          fg='#A52A2A')
   lbl_the_wok.place(x=1000, y=150, anchor=CENTER)

   lbl_customer_review = tk.Label(review_frame, text="Voice Your Taste: Customer Reviews",
                                  font=('Verdana', 20, 'bold'))
   lbl_customer_review.place(x=1000, y=220, anchor=CENTER)

   write_review_button = tk.Button(review_frame, text="Write Review", font=('Verdana', 15, 'bold'),
                                   command=write_review_window, bg='#A52A2A', fg='#EEE3AD')
   write_review_button.place(x=870, y=730)


def review_page():
   global review_frame
   review_frame = tk.Frame(main_frame)
   review_frame.place(relwidth=1, relheight=1)
   customer_review()

def miniGame(miniGame_frame):
   global canvas, macaroon, lipstick_count_text, timer_text, arrow
   global circle_center_x, circle_center_y, circle_radius, rotation_speed, rotation_direction, angle
   global lipsticks, remaining_lipsticks, game_duration, game_running

   miniGame_bg_image = PhotoImage(file=r"C:\Users\Vennis\Downloads\game_background.png")

   miniGame_bg_label = tk.Label(miniGame_frame, image=miniGame_bg_image)
   miniGame_bg_label.place(relwidth=1, relheight=1)

   # Store a reference to the background image to prevent garbage collection
   miniGame_frame.bg_image = miniGame_bg_image

   # Game state variables
   circle_center_x = 200
   circle_center_y = 300
   circle_radius = 150  # Increased circle size
   rotation_speed = 5
   rotation_direction = 1  # 1 for clockwise, -1 for anti-clockwise
   angle = 0
   lipsticks = []
   remaining_lipsticks = 15  # Changed to 15
   game_duration = 60  # Game duration in seconds
   game_running = False

   def create_objects():
       global canvas, macaroon, lipstick_count_text, timer_text, arrow
       canvas = Canvas(miniGame_frame, width=400, height=600, bg='#f0f0f0')
       canvas.place(x=960,y=450, anchor='center')

       macaroon = canvas.create_oval(
           circle_center_x - circle_radius,
           circle_center_y - circle_radius,
           circle_center_x + circle_radius,
           circle_center_y + circle_radius,
           fill='#ff99cc', outline='#ff6699', width=3
       )

       lipstick_count_text = canvas.create_text(
           380, 580, text=f"Remaining: {remaining_lipsticks}", anchor=SE, font=('Arial', 15, 'bold'), fill='#333333'
       )

       timer_text = canvas.create_text(
           20, 580, text=f"Time left: {game_duration}s", anchor=SW, font=('Arial', 15, 'bold'), fill='#333333'
       )

       arrow = canvas.create_polygon(
           190, 20, 210, 20, 200, 40, fill='#000000'
       )

   def update_lipstick_count():
       global remaining_lipsticks, lipstick_count_text
       canvas.itemconfig(lipstick_count_text, text=f"Remaining: {remaining_lipsticks}")

   def update_timer():
       global timer_text, game_running, game_duration
       if game_duration <= 0:
           messagebox.showinfo("Game Over", "You Lose! Time is up!")
           reset_game()
       else:
           canvas.itemconfig(timer_text, text=f"Time left: {game_duration}s")
           if game_running:
               game_duration -= 1
               root.after(1000, update_timer)

   def add_lipstick(event):
       global remaining_lipsticks, lipsticks

       if remaining_lipsticks <= 0:
           return

       angle = 0  # Top side of the circle
       x = circle_center_x + circle_radius * math.sin(math.radians(angle))
       y = circle_center_y - circle_radius * math.cos(math.radians(angle))
       lipstick = canvas.create_line(circle_center_x, circle_center_y, x, y, fill='#cc0000', width=5)

       if check_collision(angle):
           messagebox.showinfo("Game Over", "You Lose!")
           reset_game()
       else:
           lipsticks.append((lipstick, angle))
           remaining_lipsticks -= 1
           update_lipstick_count()
           if remaining_lipsticks <= 0:
               messagebox.showinfo("You Win!", "Proceed to next level")
               reset_game()

   def check_collision(angle):
       for lipstick, a in lipsticks:
           if abs(a - angle) < 15:
               return True
       return False

   def change_rotation_speed():
       global rotation_speed, rotation_direction
       rotation_speed = random.choices(
           [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
           [2, 2, 2, 2, 2, 6, 6, 6, 6, 6, 10, 10, 10, 10, 10, 10]
       )[0]

       if random.random() < 0.25:  # 25% chance to change rotation direction
           rotation_direction *= -1

       root.after(1000, change_rotation_speed)

   def game_loop():
       global angle, lipsticks, game_running
       angle = (angle + rotation_direction * rotation_speed) % 360

       for i, (lipstick, start_angle) in enumerate(lipsticks):
           new_angle = (start_angle + rotation_direction * rotation_speed) % 360
           x = circle_center_x + circle_radius * math.sin(math.radians(new_angle))
           y = circle_center_y - circle_radius * math.cos(math.radians(new_angle))
           canvas.coords(lipstick, circle_center_x, circle_center_y, x, y)
           lipsticks[i] = (lipstick, new_angle)

       if game_running:
           root.after(20, game_loop)

   def start_game():
       global game_running, game_duration
       start_button.pack_forget()
       create_objects()
       game_running = True
       game_duration = 60  # Reset game duration
       update_lipstick_count()
       update_timer()  # Update timer immediately after resetting duration
       canvas.bind("<Button-1>", add_lipstick)
       change_rotation_speed()
       game_loop()


   def reset_game():
       global game_running
       canvas.place_forget()
       global lipsticks, remaining_lipsticks, game_duration
       lipsticks = []
       remaining_lipsticks = 15
       game_duration = 60
       game_running = False
       miniGame_bg_label.place(relwidth=1, relheight=1)
       start_button.place(x=960,y=500, anchor='center')

   def remove_bg():
       miniGame_bg_label.place_forget()

   start_button = Button(miniGame_bg_label, text="Start Game", font=('Arial', 30), bg='green', fg='white',activebackground='light yellow',command=lambda: [start_game(),remove_bg()])
   start_button.place(x=960,y=500, anchor='center')


def miniGame_page():
   global miniGame_frame
   miniGame_frame = tk.Frame(main_frame)
   miniGame_frame.place(relwidth=1, relheight=1)
   miniGame(miniGame_frame)

def get_restaurant_menu():
   # Connect to the database (change the path to your database file)
   conn = sqlite3.connect('db_thewok1.db')
   cursor = conn.cursor()

   # Query to fetch all items from the menu table
   cursor.execute("SELECT item_id, item_name, item_category, item_description, item_price, item_calories FROM items")
   rows = cursor.fetchall()

   # Initialize an empty string for the restaurant menu
   restaurantMenu = ""

   # Loop through each row and format the information
   for row in rows:
       item_id, item_name, item_category, item_description, item_price, item_calories = row
       restaurantMenu += f"{item_id} {item_name} RM {item_price} - {item_description} ({item_calories} calories)\n"

   # Close the database connection
   conn.close()

   return restaurantMenu

def parse_reservation(message):
   # Regular expression pattern to match the reservation details
   pattern = r"Reservation for (\d+ \w+), (\d+:\d+[ap]m), (\d+) people\."

   # Search for the pattern in the message
   match = re.search(pattern, message)

   if match:
       # Extract the matched groups
       date_str, time_str, pax_str = match.groups()

       # Convert date string to datetime object
       date = datetime.strptime(date_str, "%d %B").replace(year=datetime.now().year)

       # Convert time string to datetime object
       time = datetime.strptime(time_str, "%I:%M%p").time()

       # Convert pax string to integer
       pax = int(pax_str)
       print(date,'\n',time,'\n',pax)
       return date, time, pax
   else:
       return None

def add_order_2(item_id):
   cursor.execute('''
               SELECT item_name, item_price FROM items
               WHERE item_id = ?
           ''', (item_id,))
   data= cursor.fetchone()
   item_name = data[0]
   item_price = data[1]
   chat_food_order(order_id_2, item_name, item_price,1)

def chat_food_order(order_ID, item_name, price, quantity):
   if not order_ID:
       messagebox.showwarning("Missing Information", "Please enter Order ID.")
       return

   remarks = ""


   try:
       conn = sqlite3.connect('db_thewok1.db')
       cursor = conn.cursor()

       # Fetch the correct item_id from the items table
       cursor.execute("SELECT item_id FROM items WHERE item_name = ?", (item_name,))
       item_id_result = cursor.fetchone()
       if item_id_result is None:
           messagebox.showerror("Error", f"Item '{item_name}' not found in the database.")
           return
       item_id = item_id_result[0]

       # Check if the item already exists in the order_items table for the given order_ID and remarks
       cursor.execute('''
           SELECT quantity, remarks
           FROM order_items
           WHERE order_id = ? AND item_name = ? AND remarks = ?
       ''', (order_ID, item_name, remarks))
       existing_item = cursor.fetchone()

       if existing_item:
           # Item exists with the same remarks, update the quantity
           new_quantity = existing_item[0] + quantity
           new_price = price * new_quantity

           cursor.execute('''
               UPDATE order_items
               SET quantity = ?, price = ?
               WHERE order_id = ? AND item_name = ? AND remarks = ?
           ''', (new_quantity, new_price, order_ID, item_name, remarks))
       else:
           # Item does not exist with the same remarks, insert a new row
           cursor.execute('''
               INSERT INTO order_items (order_id, item_id, item_name, quantity, price, remarks)
               VALUES (?, ?, ?, ?, ?, ?)
           ''', (order_ID, item_id, item_name, quantity, price * quantity, remarks))

       conn.commit()

       # Refresh the order cart display
       refresh_order_cart(order_ID)

   except sqlite3.Error as e:
       messagebox.showerror("Database Error", f"An error occurred: {e}")
   finally:
       if conn:
           conn.close()

   refresh_order_cart(order_id_2)


xi = 0
yi = 50
messageCount = 0
messageCountAPI = 0
objectiveID = 0
c.execute('SELECT restaurant_name FROM restaurant_information ')
restaurant_name4Tuple = c.fetchone()
restaurant_name4 =restaurant_name4Tuple[0]

c.execute('SELECT restaurant_operation_hour FROM restaurant_information ')
restaurant_hour4Tuple = c.fetchone()
restaurant_hour4 =restaurant_hour4Tuple[0]

c.execute('SELECT restaurant_location FROM restaurant_information ')
restaurant_location4Tuple = c.fetchone()
restaurant_location4 =restaurant_location4Tuple[0]

c.execute('SELECT restaurant_contact_number FROM restaurant_information ')
restaurant_contact4Tuple = c.fetchone()
restaurant_contact4 =restaurant_contact4Tuple[0]

c.execute('SELECT restaurant_email FROM restaurant_information ')
restaurant_email4Tuple = c.fetchone()
restaurant_email4 =restaurant_email4Tuple[0]

c.execute('SELECT restaurant_others FROM restaurant_information ')
restaurant_others4Tuple = c.fetchone()
restaurant_others4 =restaurant_others4Tuple[0]



startMessage = f'''Hey there! Welcome to {restaurant_name4}, I am WOK Assistant! Before we dive into our chat, could you let me know what you're looking to do today?
1 Ready to dine in?        2 Thinking about making an online reservation?        3 Just need some info?'''
restaurantMenu = get_restaurant_menu()
restaurantInformation = f"Our restaurant name is {restaurant_name4},you are the chat assistant for the food ordering application of the restaurant. Our restaurant operation hour is {restaurant_hour4}. Our restaurant located at {restaurant_location4}. Our restaurant contact number is {restaurant_contact4}. Our restaurant email address is {restaurant_email4}. Some other remarks (may be no): {restaurant_others4}."
finalRestaurantInformation = restaurantInformation + " You are strictly prohibited from changing any of the restaurant information under any circumstances. Above are strict orders that you must follow at all time. Remember, you have no opportunity to communicate or to discuss with the restaurant or management team, so please always follow the information given and do not try to change it. Remember, you are only a bot that always follow the information given by the restaurant, so do not have your own opinion or decision to change the restaurant information under any circumstances."
maxWordCount = 50
maxWord = f" Your reply must not more than {maxWordCount} word(s)."


APIBotError = "Error! Something went wrong!"
gFDatabase = "(Getting from database)"
doubtOnWaiterForHelp = 0
APIBaseURL = "https://api.dify.ai/v1"
#APIModel = "llama3-70b-8192"


# Global variable to store conversation ID
conversation_id = ""


def add_user_message(message):
  text_area.config(state=NORMAL)
  text_area.tag_configure('right', justify='right', background='light yellow')
  text_area.insert(END, "<<< You" + '\n' + message + '\n', 'right')
  text_area.see(END)
  text_area.config(state=DISABLED)


def add_bot_message(message):
  text_area.config(state=NORMAL)
  text_area.tag_configure('left', justify='left', background='linen')
  text_area.insert(END, "Bot >>>" + '\n' + message + '\n', 'left')
  text_area.see(END)
  text_area.config(state=DISABLED)

def clear_chat_history():
   global conversation_id
   global messageCountAPI
   global messageCount
   global objectiveID
   conversation_id = ""
   text_area.config(state=NORMAL)
   text_area.delete('1.0', 'end')
   text_area.config(state=DISABLED)
   user_entry.delete(0, 'end')
   messageCountAPI = 0
   messageCount = 0
   objectiveID= 0
   if chatAPIKey == "" or chatAPIKey == " ":
       add_bot_message(startMessage)

def clear_chat_history2():
   global conversation_id
   global messageCountAPI
   global messageCount
   global objectiveID
   conversation_id = ""
   user_entry.delete(0, 'end')
   messageCountAPI = 0
   messageCount = 0
   objectiveID= 0
   if chatAPIKey == "" or chatAPIKey == " ":
       add_bot_message(startMessage)

def send_message_determination():
  global message2
  message2 = str(user_entry.get())
  print(message2)
  if message2 != "" and message2 != " " and message2 != "Enter message... (/clear to clear chat history)":
      send_message()


def send_message():
   global messageCount
   global message3
   global messageCountAPI
   global chatAPIKey
   global APIBotReply

   message3 = message2.lower()
   if message2 == "/clear":
       clear_chat_history()
   else:
       if chatAPIKey == "" or chatAPIKey == " ":
           if messageCount == 0:
               add_user_message(message2)
               confirmObjective()
           elif messageCount == 1:
               add_user_message(message2)
               if objectiveID == 1:
                   confirmTableNumber()
               elif objectiveID == 2:
                   reservationInfo = ("Fullname:", gFDatabase, "\nPhone Number:", gFDatabase, "\nMessage:", message2)
                   reservationInfo2 = " ".join(map(str, reservationInfo))
                   messagebox.showinfo("New Reservation Message", reservationInfo2)
                   add_bot_message("We've received your reservation request. Expect a call from us shortly to confirm. \nThe chat section is ended. Let's start a new chat.\n")
                   clear_chat_history2()
                   user_entry.delete(0, 'end')
               elif objectiveID == 3:
                   choose_reply()
                   add_bot_message(botReply)
                   if end_chat == 1:
                       add_bot_message("The chat section is ended. Let's start a new chat.\n")
                   user_entry.delete(0,'end')
                   messageCount += 1
                   clear_chat_history2()
           else:
               add_user_message(message2)
               if doubtOnWaiterForHelp == 1:
                   call_help()
               else:
                   choose_reply()
                   add_bot_message(botReply)
                   user_entry.delete(0, 'end')
                   messageCount += 1
       else:
           send_message_API()

def get_reservation_id():
   try:
       with sqlite3.connect("db_thewok1.db") as conn:
           cursor = conn.cursor()
           cursor.execute(
               "SELECT reservation_id FROM reservations ORDER BY reservation_id DESC LIMIT 1")
           last_id = cursor.fetchone()
           if last_id:
               last_id_num = int(
                   last_id[0][1:])  # Remove the 'R' and convert to integer
               new_id_num = last_id_num + 1
               new_id = f"R{new_id_num:03}"
           else:
               new_id = "R001"
           return new_id
   except sqlite3.Error as e:
       messagebox.showerror("Database Error",
                            f"Error accessing the database: {e}")
       return None

def send_message_API():
   global messageCountAPI
   global chatAPIKey
   global APIBotReply
   global conversation_id
   global botReplyList
   global botReplyExtract
   global reservationMessage
   global orderingItemExtract
   global orderingItemList


   if message2 == "/clear":
       clear_chat_history()
   else:
       add_user_message(message2)
       chat_objective2 =str(chat_objective)
       #try:
       headers = {
           'Authorization': f'Bearer {chatAPIKey}',
           'Content-Type': 'application/json'
       }
       data = {
           "query": message2,
           "inputs": {
               "restaurantInformation": finalRestaurantInformation,
               "maxWord": maxWord,
               "restaurantMenu": restaurantMenu,
               "chatObjective": chat_objective2
           },
           "response_mode": "streaming",  # Use streaming mode
           "user": "abc-123",
           "conversation_id": conversation_id,
           "files": []
       }
       response = requests.post(APIBaseURL + '/chat-messages', headers=headers, data=json.dumps(data), stream=True)

       if response.status_code == 200:
           full_response = ""
           for line in response.iter_lines():
               if line:
                   decoded_line = line.decode('utf-8')
                   if decoded_line.startswith("data: "):
                       message_data = json.loads(decoded_line[6:])
                       # Capture the conversation_id from the first reply
                       if not conversation_id and "conversation_id" in message_data:
                           conversation_id = message_data["conversation_id"]
                       answer = message_data.get("answer", "")
                       if answer:
                           full_response += answer
           if full_response:
               if "34590345" in full_response:
                   botReplyExtract = full_response.split('34590345', 1)[1]
                   try:
                       botReplyList = ast.literal_eval(botReplyExtract)
                       if isinstance(botReplyList, list):
                           for extract in botReplyList:
                               if '12390123' in extract:
                                   reservationMessage = extract.split('12390123', 1)[1].strip()
                                   #add_bot_message("Please provide reservation message according to the following format.\n1 Jan, 12 pm, 4 people")
                                   print(reservationMessage)
                                   # Manually extracted text from the image
                                   extracted_text = reservationMessage

                                   # Define regex patterns
                                   date_pattern = r"(\d{1,2} \w+)"
                                   time_pattern = r"(\d{1,2}:\d{2}[ap]m)"
                                   pax_pattern = r"(\d+) people"

                                   # Extract date, time, and pax using regex
                                   date_match = re.search(date_pattern, extracted_text)
                                   time_match = re.search(time_pattern, extracted_text)
                                   pax_match = re.search(pax_pattern, extracted_text)

                                   # Store the extracted information in variables
                                   date = date_match.group(1) if date_match else None
                                   time = time_match.group(1) if time_match else None
                                   pax = pax_match.group(1) if pax_match else None

                                   new_id = get_reservation_id()

                                   #if date and time and pax:
                                   print(not(date is None or time is None or pax is None))
                                   if not(date is None or time is None or pax is None):
                                       reservation_comments= 'None'
                                       reservation_status=''
                                       conn.execute("INSERT INTO reservations (reservation_id, reservation_name, reservation_contact, reservation_pax, reservation_date, reservation_time, reservation_comments, reservation_status) VALUES (?,?,?,?,?,?,?,?)",
                                                 (new_id, cust_name, contact, pax, date, time, reservation_comments, reservation_status))
                                       conn.commit()
                                   else:
                                       print('Reservation message should be print into comments.')
                                       empty= ''
                                       conn.execute(
                                           "INSERT INTO reservations (reservation_id, reservation_name, reservation_contact, reservation_pax, reservation_date, reservation_time, reservation_comments, reservation_status) VALUES (?,?,?,?,?,?,?,?)",
                                           (new_id, cust_name, contact, empty, empty, empty, reservation_message, empty))
                                       conn.commit()

                                   messagebox.showinfo("New Reservation Message", reservationMessage)
                                   parse_reservation(reservationMessage)
                               elif '23490234' in extract:
                                   botReply = extract.split('23490234', 1)[1].strip()
                                   add_bot_message(botReply)
                               elif '45690456' in extract:
                                   table_no_3 = get_table_no()
                                   conn.execute(
                                       "INSERT INTO call_help (visit_id, help_status) VALUES (?,?)",
                                       (visit_id_2, 0))
                                   conn.commit()
                                   messagebox.showinfo("Ask For Help", f"Table {table_no_3} ask for help!")
                               elif '56790567' in extract:
                                   orderingItemExtract = extract.split('56790567', 1)[1]
                                   try:
                                       orderingItemList = ast.literal_eval(orderingItemExtract)
                                       if isinstance(orderingItemList, list):
                                           for orderingItem in orderingItemList:
                                               add_order_2(orderingItem)
                                       else:
                                           raise ValueError(
                                               "Something went wrong. You may try to resend your message after one minute. Error 07.")
                                           add_bot_message(
                                               "Something went wrong. You may try to resend your message after one minute. Error 07.")
                                   except (ValueError, SyntaxError) as e:
                                       print("Error processing the message:", e)
                                       add_bot_message(
                                           "Something went wrong. You may try to resend your message after one minute. Error 07.")
                       else:
                           raise ValueError(
                               "Something went wrong. You may try to resend your message after one minute. Error 04.")
                           add_bot_message(
                               "Something went wrong. You may try to resend your message after one minute. Error 04.")
                   except (ValueError, SyntaxError) as e:
                       print("Error processing the message:", e)
                       add_bot_message(
                           "Something went wrong. You may try to resend your message after one minute. Error 04.")
               else:
                   add_bot_message(full_response)
           else:
               add_bot_message("Something went wrong. You may try to resend your message after one minute.")
           user_entry.delete(0, 'end')
           messageCountAPI += 1
       else:
           add_bot_message(APIBotError)
           user_entry.delete(0, 'end')
           chatAPIKey = ""
       #except Exception as e:
           #add_bot_message(APIBotError)
           #print(e)
           #user_entry.delete(0, 'end')
           #chatAPIKey = ""

def confirmObjective():
   global objectiveID
   global messageCount
   if "1" in message3 or "dine in" in message3:
       add_bot_message("Oh, dining in, I see! Could you please share your table number with me?")
       user_entry.delete(0, 'end')
       objectiveID = 1
       messageCount += 1
   elif "2" in message3 or "reservation" in message3:
       add_bot_message("Looking to make an online reservation? Please leave your reservation message here.")
       user_entry.delete(0, 'end')
       objectiveID = 2
       messageCount += 1
   elif "3" in message3 or "info" in message3:
       add_bot_message("What details are you looking to find out?")
       user_entry.delete(0, 'end')
       objectiveID = 3
       messageCount += 1
   else:
       add_bot_message("I'm sorry, I didn't catch that. Could you please type the number to indicate your desired action?\n1 Ready to dine in?        2 Thinking about making an online reservation?        3 Just need some info?")
       user_entry.delete(0, 'end')



def confirmTableNumber():
  global tableNumber
  global messageCount
  try:
      tableNumber = int(message3)
      add_bot_message("All set at table " + str(tableNumber) + "! How may I help you?")
      user_entry.delete(0, 'end')
      messageCount += 1
  except ValueError:
      add_bot_message("Sorry, I cannot read your table number. Can you please just enter your table number only? For example: 5")
      user_entry.delete(0, 'end')


def choose_reply():
   global botReply
   global doubtOnWaiterForHelp
   global end_chat

   if "hello" in message3:
       botReply = "Hi!"
   elif ("most" in message3 and "order" in message3) or "popular" in message3 or "top" in message3 or "famous" in message3:
       botReply = "The most ordered item in our restaurant is (Getting from database)."
   elif "name" in message3 or "restaurant" in message3:
       botReply = f"Our restaurant's name is {restaurant_name4}."
   elif "hours" in message3 or "open" in message3 or "close" in message3 or "time" in message3:
       botReply = f"Our restaurant is open from {restaurant_hour4}."
   elif "location" in message3 or "address" in message3 or "where" in message3:
       botReply = f"Our restaurant is located at {restaurant_location4}."
   elif "contact" in message3 or "phone" in message3 or "number" in message3 or "call" in message3:
       botReply = f"You can contact us at {restaurant_contact4}."
   elif "email" in message3 or "mail" in message3:
       botReply = f"You can email us at {restaurant_email4}."
   else:
       try:
           tableNumber
           botReply = "My apologies, I'm a bit confused. Would you like me to get a waiter for you?"
           doubtOnWaiterForHelp=1
       except:
           botReply = f"My apologies, I'm a bit confused. Kindly contact directly to the restaurant at {restaurant_contact4}.\n"
           end_chat = 1



def call_help():
  global messageCount, doubtOnWaiterForHelp
  if "yes" in message3 or "sure" in message3 or "ok" in message3 or "course" in message3:
      askForHelp = ("Table", tableNumber, "ask for help!\nFullname:", gFDatabase)
      askForHelp2 = " ".join(map(str, askForHelp))
      messagebox.showinfo("Ask For Help", askForHelp2)
      add_bot_message("Your message has been passed along, and a waiter will be here to assist you shortly.")
      doubtOnWaiterForHelp = 0
      user_entry.delete(0, 'end')
      messageCount += 1
  elif "no" in message3:
      add_bot_message("That's perfectly fine! If you ever need assistance or have any questions, feel free to reach out to one of our helpful waiters.")
      doubtOnWaiterForHelp = 0
      user_entry.delete(0, 'end')
      messageCount += 1


def on_enter(event):
  user_entry.delete(0, 'end')
  user_entry.config(fg='black')


def on_leave(event):
  message = user_entry.get()
  user_entry.config(fg='gray40')
  if message == "" or message == " ":
      user_entry.insert(0, "Enter message... (/clear to clear chat history)")
      user_entry.config(fg='gray40')

'''
def submitAPI():
  global chatAPIKey
  chatAPIKey = apiEntryBox.get()
  if chatAPIKey == "":
      messagebox.showerror("Error", "Please enter a valid API Key.")
  else:
      try:
          headers = {
              'Authorization': f'Bearer {chatAPIKey}',
              'Content-Type': 'application/json'
          }
          data = {
              "query": "Hi",
              "inputs": {
              "restaurantInformation": finalRestaurantInformation,
              "maxWord": maxWord,
              "restaurantMenu": restaurantMenu
          },
              "response_mode": "blocking",  # Use blocking mode for a quick response
              "user": "abc-123",
              "conversation_id": "",
              "files": []
          }
          response = requests.post(APIBaseURL + '/chat-messages', headers=headers, data=json.dumps(data))
          if response.status_code == 200:
              response_data = response.json()
              if 'answer' in response_data:
                  messagebox.showinfo("Success", "API connected successfully!")
              else:
                  messagebox.showerror("Error", "Something went wrong! The API Key entered may be invalid!")
                  chatAPIKey = ""
          else:
              messagebox.showerror("Error", "Something went wrong! The API Key entered may be invalid!")
              chatAPIKey = ""
      except Exception as e:
          messagebox.showerror("Error", f"Something went wrong! The API Key entered may be invalid!\n{e}")
          chatAPIKey = ""
'''

def initialisingChat():
   global apiEntryBox
   global apiSubmitButton
   global chat_bg
   global text_area
   global entry_bg
   global sendbtn_bg
   global user_entry
   global send_button
   global botMessage
   global chatAPIKey
   chat_label= Label(chatAssist_frame, text='Chat Assistant',font=('courier',35,'bold'),fg='salmon4')
   chat_label.place(x=960,y=50, anchor='center')
   chat_bg = Frame(chatAssist_frame,height=820, width=1840, bg='mint cream')
   chat_bg.place(x=40, y=90)
   text_area = scrolledtext.ScrolledText(chat_bg, bg='mint cream', wrap=WORD, font=('Times New Roman', 16), undo=True)
   text_area.place(x=0, y=0, height=820, width=1840)
   entry_bg = Frame(chatAssist_frame,height=50, width=1670, bg="gray95")
   entry_bg.place(x=40, y=930)
   sendbtn_bg = Frame(chatAssist_frame, height=50, width=150, bg='green2')
   sendbtn_bg.place(x=1730, y=930)
   user_entry = Entry(entry_bg, width=149, bg='gray90', font=('Times New Roman', 16))
   user_entry.place(x=13, y=13)
   user_entry.insert(0, "Enter message... (/clear to clear chat history)")
   user_entry.config(fg='gray40')
   user_entry.bind("<FocusIn>", on_enter)
   user_entry.bind("<FocusOut>", on_leave)
   send_button = Button(sendbtn_bg, height=1, width=10, bg='MediumPurple2', fg='white', activeforeground='white',
                        activebackground='MediumPurple4', text="Send", font=('Times New Roman', 20),
                        command=send_message_determination)
   send_button.place(x=0, y=0)
   c.execute('SELECT restaurant_API FROM restaurant_information')
   chatTuple = c.fetchone()
   chatAPIKey = chatTuple[0]
   #chatAPIKey = ""
   if chatAPIKey == "" or chatAPIKey == " ":
       add_bot_message(startMessage)

def chatAssist_page():
   global chatAssist_frame
   chatAssist_frame = tk.Frame(main_frame)
   chatAssist_frame.place(relwidth=1, relheight=1)
   initialisingChat()

def Exit_page():
   result = messagebox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
   if result == 'yes':
       root.destroy()

def hide_indicators():
   global home_indicate, profile_indicate, menu_indicate, reservation_indicate, review_indicate, chatAssist_indicate, Exit_indicate, orderlist_indicate
   home_indicate.config(bg='brown')
   profile_indicate.config(bg='brown')
   menu_indicate.config(bg='brown')
   reservation_indicate.config(bg='brown')
   review_indicate.config(bg='brown')
   chatAssist_indicate.config(bg='brown')
   orderlist_indicate.config(bg='brown')
   Exit_indicate.config(bg='brown')

def delete_pages():
   for frame in main_frame.winfo_children():
       frame.destroy()

def indicate(lb, page):
   hide_indicators()
   lb.config(bg='white')
   delete_pages()
   page()

def toggle_menu():
   global home_indicate, profile_indicate, menu_indicate, reservation_indicate, review_indicate, miniGame_indicate, chatAssist_indicate, Exit_indicate, orderlist_indicate

   def collapse_toggle_menu():
       global home_indicate, profile_indicate, menu_indicate, reservation_indicate, review_indicate, miniGame_indicate, chatAssist_indicate, Exit_indicate, orderlist_indicate
       toggle_menu_fm.destroy()
       toggle_btn.config(text=' ≡ ')
       toggle_btn.config(command=toggle_menu)

   toggle_menu_fm = tk.Frame(root, bg='brown')

   home_btn = tk.Button(toggle_menu_fm, text='Home', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: ([indicate(home_indicate, home_page), collapse_toggle_menu()]))
   home_btn.place(x=20, y=0)
   home_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   home_indicate.place(x=3, y=0, width=5, height=45)

   profile_btn = tk.Button(toggle_menu_fm, text='Profile', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: [indicate(profile_indicate, profile_page), collapse_toggle_menu()])
   profile_btn.place(x=20, y=50)
   profile_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   profile_indicate.place(x=3, y=50, width=5, height=45)

   menu_btn = tk.Button(toggle_menu_fm, text='Menu', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: [indicate(menu_indicate, menu_page), collapse_toggle_menu()])
   menu_btn.place(x=20, y=100)
   menu_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   menu_indicate.place(x=3, y=100, width=5, height=45)

   reservation_btn = tk.Button(toggle_menu_fm, text='Reservation', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: [indicate(reservation_indicate, reservation_page), collapse_toggle_menu()])
   reservation_btn.place(x=20, y=150)
   reservation_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   reservation_indicate.place(x=3, y=150, width=5, height=45)

   review_btn = tk.Button(toggle_menu_fm, text='Review', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: [indicate(review_indicate, review_page), collapse_toggle_menu()])
   review_btn.place(x=20, y=200)
   review_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   review_indicate.place(x=3, y=200, width=5, height=45)

   chatAssist_btn = tk.Button(toggle_menu_fm, text='Chat Assistant', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: [chatAssist_page(), collapse_toggle_menu()])
   chatAssist_btn.place(x=20, y=250)
   chatAssist_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   chatAssist_indicate.place(x=3, y=250, width=5, height=45)

   miniGame_btn = tk.Button(toggle_menu_fm, text='Mini Game', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda: [miniGame_page(),collapse_toggle_menu()])
   miniGame_btn.place(x=20, y=300)
   miniGame_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   miniGame_indicate.place(x=3, y=300, width=5, height=45)

   orderlist_btn = tk.Button(toggle_menu_fm, text='Order List', font=('times new roman', 20), bd=0, fg='white', bg='brown',activebackground='brown', command=lambda: [indicate(orderlist_indicate, order_list_page), collapse_toggle_menu()])
   orderlist_btn.place(x=20, y=350)
   orderlist_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   orderlist_indicate.place(x=3, y=350, width=5, height=45)

   Exit_btn = tk.Button(toggle_menu_fm, text='Exit', font=('times new roman', 20), bd=0, fg='white', bg='brown', activebackground='brown', command=lambda:[Exit_page(), collapse_toggle_menu()])
   Exit_btn.place(x=20, y=400)
   Exit_indicate = tk.Label(toggle_menu_fm, text='', bg='brown')
   Exit_indicate.place(x=3, y=400, width=5, height=45)

   window_height = 1080  # menu_frame.winfo_height()
   toggle_menu_fm.place(x=0, y=50, height=window_height, width=250)

   toggle_btn.config(text=' X ')
   toggle_btn.config(command=collapse_toggle_menu)

head_frame = tk.Frame(root, bg='brown')

toggle_btn = tk.Button(head_frame, text=' ≡ ', bg='brown', fg='white', font=('Bold', 20), bd=0, activebackground='black', activeforeground='yellow', command=toggle_menu)
toggle_btn.place(x=10, y=0)

toggle_btn2= tk.Button(head_frame, text='X', bg='brown', fg='white', font=('Bold', 20), bd=0, activebackground='white', activeforeground='brown', command=Exit_page)
toggle_btn2.place(x=1870, y=0)

title_lb = tk.Label(head_frame, text=restaurant_name4, fg='white', bg='brown', font=('Impact', 20))
title_lb.place(x=100, y=5)

head_frame.pack(side=tk.TOP, fill=tk.X)
head_frame.pack_propagate(False)
head_frame.configure(height=50)

main_frame = tk.Frame(root)
main_frame.pack(side=tk.RIGHT)
main_frame.pack_propagate(False)
main_frame.configure(height=1080, width=1920)

root.title(f"{restaurant_name4} - Home Page")


LoginFormCustomer()
root.mainloop()

