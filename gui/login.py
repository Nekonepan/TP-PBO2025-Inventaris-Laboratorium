import tkinter as tk
from tkinter import messagebox
from src.database.database import Database
from src.session.session import Session
from gui.dashboard import DashboardGUI


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

        tk.Button(self.window, text="Login", command=self.login).pack(pady=10)

        self.window.mainloop()

    def login(self):
        username = self.username.get()
        password = self.password.get()

        self.db.cursor.execute(
            "SELECT * FROM user WHERE username=? AND password=?",
            (username, password)
        )
        user = self.db.cursor.fetchone()

        if user:
            Session.user_id = user[0]
            Session.username = user[1]
            Session.role = user[3]

            self.window.destroy()      # ✅ TUTUP LOGIN
            DashboardGUI()             # buka dashboard
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah")
