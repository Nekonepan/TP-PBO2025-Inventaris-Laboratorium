import tkinter as tk
from tkinter import messagebox
from src.database.database import Database
from src.utils.session import Session
from .dashboard import DashboardGUI
from src.session.session import Session


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

        query = """
        SELECT user_id, username, role
        FROM user
        WHERE username=? AND password=?
        """
        self.db.cursor.execute(query, (username, password))
        user = self.db.cursor.fetchone()

        if user:
            # SIMPAN SESSION
            Session.user_id = user[0]
            Session.username = user[1]
            Session.role = user[2]

            self.window.destroy()
            DashboardGUI()
        else:
            messagebox.showerror("Error", "Username atau password salah")
