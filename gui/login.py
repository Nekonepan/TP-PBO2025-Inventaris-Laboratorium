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
        
        # --- KUNCI FULLSCREEN ---
        # Ini akan membuat jendela otomatis maksimal (zoomed) saat dibuka
        self.window.state("zoomed") 
        
        self.window.configure(bg="#D1E9F6") 

        # --- CONTAINER UTAMA ---
        self.main_frame = tk.Frame(self.window, bg="white", bd=0)
        # Menggunakan place agar kartu login tetap di tengah layar meskipun fullscreen
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=400)

        # --- SISI KIRI (Form Login) ---
        self.left_frame = tk.Frame(self.main_frame, bg="#4A90E2", width=450, height=400)
        self.left_frame.pack(side="left", fill="both", expand=True)

        tk.Label(self.left_frame, text="LOGIN", font=("Helvetica", 24, "bold"), 
                 bg="#4A90E2", fg="white").pack(pady=(50, 20))

        # Username
        tk.Label(self.left_frame, text="USER NAME", font=("Helvetica", 8, "bold"), 
                 bg="#4A90E2", fg="white").pack(anchor="w", padx=50)
        self.username = tk.Entry(self.left_frame, font=("Helvetica", 12), bd=0, highlightthickness=1)
        self.username.pack(fill="x", padx=50, pady=(5, 15), ipady=5)

        # Password
        tk.Label(self.left_frame, text="PASSWORD", font=("Helvetica", 8, "bold"), 
                 bg="#4A90E2", fg="white").pack(anchor="w", padx=50)
        self.password = tk.Entry(self.left_frame, font=("Helvetica", 12), show="*", bd=0, highlightthickness=1)
        self.password.pack(fill="x", padx=50, pady=(5, 30), ipady=5)

        # Tombol Login
        self.btn_login = tk.Button(self.left_frame, text="SIGN UP", command=self.login,
                                   bg="white", fg="#4A90E2", font=("Helvetica", 10, "bold"),
                                   bd=0, cursor="hand2", width=20)
        self.btn_login.pack(pady=10, ipady=5)

        # tk.Label(self.left_frame, text="Don't have an account?", font=("Helvetica", 8), 
        #          bg="#4A90E2", fg="white").pack()

        # --- SISI KANAN (Logo) ---
        self.right_frame = tk.Frame(self.main_frame, bg="white", width=250, height=400)
        self.right_frame.pack(side="right", fill="both")

        tk.Label(self.right_frame, text="🔒", font=("Helvetica", 60), 
                 bg="white", fg="#A0E9FF").pack(expand=True)
        
        # tk.Label(self.right_frame, text="Dole.com", font=("Helvetica", 8), 
        #          bg="white", fg="lightgrey").pack(pady=10)

        self.window.mainloop()

    def login(self):
        # Tambahkan .strip() untuk menghindari spasi tak sengaja
        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:
            messagebox.showwarning("Input Kosong", "Silahkan isi username dan password")
            return

        try:
            self.db.cursor.execute(
                "SELECT * FROM user WHERE username=? AND password=?",
                (username, password)
            )
            user = self.db.cursor.fetchone()

            if user:
                Session.user_id = user[0]
                Session.username = user[1]
                Session.role = user[3]
                self.window.destroy()
                DashboardGUI()
            else:
                messagebox.showerror("Login Gagal", "Username atau password salah")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan database: {e}")

if __name__ == "__main__":
    LoginGUI()