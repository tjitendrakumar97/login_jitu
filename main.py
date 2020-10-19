# import PySimpleGUI as sg
from tkinter import *
from tkinter import messagebox


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login/Sign Up")
        self.root.geometry("1500x900+0+0")
        title = Label(self.root, text="Login system", font=("times new roman", 40, "bold"), bg="blue")
        title.place(x=0, y=0, relwidth=1)
        self.uname = StringVar()
        self.password = StringVar()
        self.sgn_uname = StringVar()
        self.sgn_password = StringVar()
        self.sgn_password_re = StringVar()

        login_frame = Frame(self.root, bg="blue")
        login_frame.place(x=100, y=300)

        lbuser = Label(login_frame, text="Username", compound=LEFT, font=("times new roman", 20, "bold")).grid(row=2,
                                                                                                               column=0,
                                                                                                               padx=20,
                                                                                                               pady=10)
        txtuser = Entry(login_frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15)).grid(row=2, column=1,
                                                                                                       padx=20)
        lbpass = Label(login_frame, text="Password", compound=LEFT, font=("times new roman", 20, "bold")).grid(row=3,
                                                                                                               column=0,
                                                                                                               padx=20,
                                                                                                               pady=10)
        txtpass = Entry(login_frame, bd=5, textvariable=self.password, relief=GROOVE, font=("", 15)).grid(row=3,
                                                                                                          column=1,
                                                                                                          padx=20)

        btn_login = Button(login_frame, text="Login", width=12, command=self.login,
                           font=("times new roman", 14, "bold"),
                           fg="green").grid(row=4, column=0, pady=10)
        head_log = Label(login_frame, text="Login", compound=CENTER, font=("times new roman", 20, "bold")).grid(row=1,
                                                                                                                column=0
                                                                                                                ,
                                                                                                                padx=20,
                                                                                                                pady=10)
        signup_frame = Frame(self.root, bg="blue")
        signup_frame.place(x=720, y=300)

        sgnuser = Label(signup_frame, text="Username", compound=LEFT, font=("times new roman", 20, "bold")).grid(row=2,
                                                                                                                 column=0
                                                                                                                 ,
                                                                                                                 padx=20
                                                                                                                 ,
                                                                                                                 pady=10)
        txtsgnuser = Entry(signup_frame, bd=5, textvariable=self.sgn_uname, relief=GROOVE, font=("", 15)).grid(row=2,
                                                                                                               column=1,
                                                                                                               padx=20)
        sgnpass = Label(signup_frame, text="Password", compound=LEFT, font=("times new roman", 20, "bold")).grid(row=3,
                                                                                                                 column=0,
                                                                                                                 padx=20,
                                                                                                                 pady=10)
        txtsgnpass = Entry(signup_frame, bd=5, textvariable=self.sgn_password, relief=GROOVE, font=("", 15)).grid(row=3,
                                                                                                                  column=1,
                                                                                                                  padx=20)
        sgnpass_re = Label(signup_frame, text="Re enter Password", compound=LEFT,
                           font=("times new roman", 20, "bold")).grid(row=4,
                                                                      column=0,
                                                                      padx=20,
                                                                      pady=10)
        txtsgnpass_re = Entry(signup_frame, bd=5, textvariable=self.sgn_password_re, relief=GROOVE, font=("", 15)).grid(
            row=4,
            column=1,
            padx=20)

        btn_sgn = Button(signup_frame, text="Signup", width=12, command=self.signup,
                         font=("times new roman", 14, "bold"),
                         fg="green").grid(row=5, column=0, pady=10)
        head_sgn = Label(signup_frame, text="Signup", compound=CENTER, font=("times new roman", 20, "bold")).grid(row=1,
                                                                                                                  column=0
                                                                                                                  ,
                                                                                                                  padx=20,
                                                                                                                  pady=10)

    def login(self):
        if self.uname.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        elif self.uname.get() == "jitu" and self.password.get() == "12345":
            messagebox.showinfo("Successful", f"Welcome {self.uname.get()}")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def signup(self):
        if self.sgn_uname.get() == "" or self.sgn_password.get() == "" or self.sgn_password_re.get() == "":
            messagebox.showerror("Error", "All fields are required!")
        elif self.sgn_password.get() != self.sgn_password_re.get():
            messagebox.showerror("Error", "Mismatch in password!")
        else:
            messagebox.showinfo("Successful", f"Signup Successful for {self.sgn_uname.get()}")


root = Tk()
obj = Login(root)
root.mainloop()
