import tkinter as tk
from tkinter import messagebox
# Import database & session tetap sama seperti kode aslimu
from src.database.database import Database
from src.session.session import Session
from gui.dashboard import DashboardGUI

class LoginGUI:
    def __init__(self):
        self.db = Database()
        self.window = tk.Tk()
        self.window.title("Login Inventaris Laboratorium")
        self.window.geometry("800x500") # Ukuran fix agar proporsional
        self.window.configure(bg="#D1E9F6") # Warna dasar biru muda

        # --- CONTAINER UTAMA ---
        # Membuat frame tengah agar mirip kartu di gambar
        self.main_frame = tk.Frame(self.window, bg="white", bd=0)
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=400)

        # --- SISI KIRI (Fom Login dengan Gradasi Biru) ---
        # Catatan: Di tkinter, warna gradasi paling mudah dibuat dengan Label warna solid 
        # atau gambar. Di sini kita gunakan warna biru yang mirip.
        self.left_frame = tk.Frame(self.main_frame, bg="#4A90E2", width=450, height=400)
        self.left_frame.pack(side="left", fill="both", expand=True)

        tk.Label(self.left_frame, text="LOGIN", font=("Helvetica", 24, "bold"), 
                 bg="#4A90E2", fg="white").pack(pady=(50, 20))

        # Username
        tk.Label(self.left_frame, text="USER NAME", font=("Helvetica", 8), 
                 bg="#4A90E2", fg="white").pack(anchor="w", padx=50)
        self.username = tk.Entry(self.left_frame, font=("Helvetica", 12), bd=0, highlightthickness=1)
        self.username.pack(fill="x", padx=50, pady=(0, 15), ipady=5)

        # Password
        tk.Label(self.left_frame, text="PASSWORD", font=("Helvetica", 8), 
                 bg="#4A90E2", fg="white").pack(anchor="w", padx=50)
        self.password = tk.Entry(self.left_frame, font=("Helvetica", 12), show="*", bd=0, highlightthickness=1)
        self.password.pack(fill="x", padx=50, pady=(0, 30), ipady=5)

        # Tombol Sign Up (Login)
        self.btn_login = tk.Button(self.left_frame, text="SIGN UP", command=self.login,
                                   bg="white", fg="#4A90E2", font=("Helvetica", 10, "bold"),
                                   bd=0, cursor="hand2", width=20)
        self.btn_login.pack(pady=10, ipady=5)

        tk.Label(self.left_frame, text="Don't have an account?", font=("Helvetica", 8), 
                 bg="#4A90E2", fg="white").pack()

        # --- SISI KANAN (Putih / Logo) ---
        self.right_frame = tk.Frame(self.main_frame, bg="white", width=250, height=400)
        self.right_frame.pack(side="right", fill="both")

        # Placeholder untuk Logo Gembok (Bisa diganti dengan ImageTk)
        tk.Label(self.right_frame, text="🔒", font=("Helvetica", 60), 
                 bg="white", fg="#A0E9FF").pack(expand=True)
        
        tk.Label(self.right_frame, text="Dole.com", font=("Helvetica", 8), 
                 bg="white", fg="lightgrey").pack(pady=10)

        self.window.mainloop()

    def login(self):
        # Logika login tetap sama persis dengan kodemu sebelumnya
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
            self.window.destroy()
            DashboardGUI()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah")