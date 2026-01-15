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
        self.window.geometry("300x300")

        tk.Label(
            self.window,
            text="Dashboard Inventaris Laboratorium",
            font=("Arial", 12, "bold")
        ).pack(pady=10)

        # ===== MENU BERDASARKAN ROLE =====
        if Session.role == "admin":
            tk.Button(
                self.window,
                text="Kelola Alat",
                width=20,
                command=self.kelola_alat
            ).pack(pady=5)

            tk.Button(
                self.window,
                text="Kelola Kategori",
                width=20,
                command=self.kelola_kategori
            ).pack(pady=5)

        # semua role boleh pinjam
        tk.Button(
            self.window,
            text="Peminjaman Alat",
            width=20,
            command=self.peminjaman_alat
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Logout",
            width=20,
            command=self.logout
        ).pack(pady=10)

        self.window.mainloop()

    def kelola_alat(self):
        AlatGUI()

    def kelola_kategori(self):
        KategoriGUI()

    def peminjaman_alat(self):
        PeminjamanGUI()

    def logout(self):
        konfirmasi = messagebox.askyesno("Logout", "Apakah Anda yakin ingin keluar?")
        if konfirmasi:
            self.window.destroy()
