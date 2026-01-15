import tkinter as tk
from .dashboard import DashboardGUI

class LoginGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Login Inventaris Laboratorium")

        tk.Label(self.window, text="Username").pack()
        self.username = tk.Entry(self.window)
        self.username.pack()

        tk.Label(self.window, text="Password").pack()
        self.password = tk.Entry(self.window, show="*")
        self.password.pack()

        tk.Button(self.window, text="Login", command=self.login).pack(pady=10)
        self.window.mainloop()

    def login(self):
        # sementara tanpa validasi (aman untuk PBO)
        self.window.destroy()
        DashboardGUI()
