import tkinter as tk
from tkinter import messagebox
from gui.alat_gui import AlatGUI
from gui.kategori_gui import KategoriGUI
from gui.peminjaman_gui import PeminjamanGUI
from src.session.session import Session

class DashboardGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Dashboard Inventaris Laboratorium")
        self.window.state("zoomed")
        self.window.configure(bg="#D1E9F6")

        # --- SIDEBAR ---
        self.sidebar = tk.Frame(self.window, bg="#4A90E2", width=280)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Header Sidebar
        tk.Label(self.sidebar, text="MENU UTAMA", font=("Helvetica", 14, "bold"), 
                 bg="#4A90E2", fg="white").pack(pady=(50, 40))

        # --- MENU BUTTONS ---
        # Kita buat fungsi pembantu agar posisi emoji dan teks terkunci secara grid
        if Session.role == "admin":
            self.add_menu_item("-", "Kelola Alat", self.kelola_alat)
            self.add_menu_item("-", "Kelola Kategori", self.kelola_kategori)
        
        self.add_menu_item("-", "Peminjaman", self.peminjaman_alat)

        # Tombol Logout
        logout_btn = tk.Button(self.sidebar, text="LOGOUT", command=self.logout, 
                              bg="#FF6B6B", fg="white", font=("Helvetica", 10, "bold"),
                              bd=0, cursor="hand2")
        logout_btn.pack(side="bottom", fill="x", pady=20, ipady=12)

        # --- MAIN AREA ---
        self.main_content = tk.Frame(self.window, bg="white")
        self.main_content.pack(side="right", fill="both", expand=True, padx=20, pady=20)

        welcome_text = f"SELAMAT DATANG, {Session.username.upper()}"
        tk.Label(self.main_content, text=welcome_text, font=("Helvetica", 20, "bold"), 
                 bg="white", fg="#4A90E2").place(relx=0.5, rely=0.5, anchor="center")

        self.window.mainloop()

    def add_menu_item(self, icon, text, command):
        """Fungsi ini membuat container tombol agar emoji dan teks lurus sempurna"""
        # Frame pembungkus tombol agar bisa diklik seluruh area
        btn_frame = tk.Frame(self.sidebar, bg="#4A90E2", cursor="hand2")
        btn_frame.pack(fill="x", pady=2)

        # Bind event klik pada frame agar berfungsi seperti tombol
        btn_frame.bind("<Button-1>", lambda e: command())

        # Label Icon (Kolom 0) - Lebar dikunci agar teks di kolom 1 sejajar
        lbl_icon = tk.Label(btn_frame, text=icon, font=("Helvetica", 14), 
                           bg="#4A90E2", fg="white", width=4)
        lbl_icon.grid(row=0, column=0, padx=(30, 0), pady=10)
        lbl_icon.bind("<Button-1>", lambda e: command())

        # Label Text (Kolom 1) - Rata kiri (anchor='w')
        lbl_text = tk.Label(btn_frame, text=text, font=("Helvetica", 11, "bold"), 
                           bg="#4A90E2", fg="white", anchor="w")
        lbl_text.grid(row=0, column=1, sticky="w")
        lbl_text.bind("<Button-1>", lambda e: command())

        # Efek Hover (Opsional agar lebih enak dilihat)
        def on_enter(e): btn_frame.config(bg="#357ABD"), lbl_icon.config(bg="#357ABD"), lbl_text.config(bg="#357ABD")
        def on_leave(e): btn_frame.config(bg="#4A90E2"), lbl_icon.config(bg="#4A90E2"), lbl_text.config(bg="#4A90E2")
        
        btn_frame.bind("<Enter>", on_enter)
        btn_frame.bind("<Leave>", on_leave)

    def kelola_alat(self): AlatGUI()
    def kelola_kategori(self): KategoriGUI()
    def peminjaman_alat(self): PeminjamanGUI()
    def logout(self):
        if messagebox.askyesno("Logout", "Yakin ingin keluar?"):
            self.window.destroy()