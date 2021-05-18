#!C:\Users\Sara\AppData\Local\Programs\Python\Python39\python.exe
from PIL import Image, ImageTk
from tkinter import *
import mysql.connector

print("Content-Type: text/html\n")
print("Inserted Records!")

conn = mysql.connector.connect(
    host="localhost", port="3306", user="root", database="test1")
cursor = conn.cursor()
selectquery = "select * from example"
cursor.execute(selectquery)
records = cursor.fetchall()
print("Number of rows in given table ", cursor.rowcount)

for row in records:
    print("Username ", row[0])
    print("Password ", row[1])
    print()

cursor.close()
conn.close()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")

        self.bg = ImageTk.PhotoImage(file="bg1.jpg")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        #self.left = ImageTk.PhotoImage(file = "left.png")
        #left = Label(self.root, image = self.left).place(x = 80, y = 100, relwidth = 400, relheight = 500)

        frame1 = Frame(self.root, bg="white")
        frame1.place(x=300, y=70, width=700, height=350)

        title = Label(frame1, text="REGISTER HERE", font=(
            "Comicsans", 22, "bold"), bg="white", fg="blue").place(x=50, y=30)

        self.var_name = StringVar()
        name = Label(frame1, text="Enter Full Name", font=(
            "Comicsans", 17, "bold"), bg="white", fg="green").place(x=50, y=100)
        txt_name = Entry(frame1, font=("Comicsans", 17),
                         bg="light gray").place(x=50, y=130, width=250)

        pwd = Label(frame1, text="Enter Password", font=(
            "Comicsans", 17, "bold"), bg="white", fg="green").place(x=370, y=100)
        pass_pwd = Entry(frame1, font=("Comicsans", 17), bg="light gray",
                         textvariable=self.var_name).place(x=370, y=130, width=250)

        confirm_pwd = Label(frame1, text="Confirm Password", font=(
            "Comicsans", 17, "bold"), bg="white", fg="green").place(x=50, y=170)
        pass_confirm = Entry(frame1, font=("Comicsans", 17),
                             bg="light gray").place(x=50, y=200, width=250)

        btn_register = Button(frame1, text="Register and Play --->", cursor="hand2", command=self.registerData,
                              font=("Comicsans", 17, "bold"), bg="white", fg="purple").place(x=210, y=280)

        # btn_login = Button(self.root, text="Sign In", cursor="hand2", font=(
        # "Comicsans", 17, "bold"), bg="white", fg="black").place(x=620, y=550)

    def registerData(self):
        print(self.var_name.get())

    # def nextPage():
        # root.destroy()
        #import page2

    # def prevPage():
        # root.destroy()
        #import page3


root = Tk()
obj = Register(root)
root.mainloop()
