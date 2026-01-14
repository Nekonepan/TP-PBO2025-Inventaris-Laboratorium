import tkinter as tk
from ..src.database import Database

class LoginGUI:
    def __init__(self):
        self.db = Database()
        self.window = tk.Tk()
        self.window.title("Login Inventaris Laboratorium")

        tk.Label(self.window, text="Username").pack()
        self.username = tk.Entry(self.window)
        self.username.pack()

        tk.Label(self.window, text="Password").pack()
        self.password = tk.Entry(self.window, show="*")
        self.password.pack()

        tk.Button(self.window, text="Login", command=self.login).pack()
        self.window.mainloop()

    def login(self):
        print("Login ditekan")
