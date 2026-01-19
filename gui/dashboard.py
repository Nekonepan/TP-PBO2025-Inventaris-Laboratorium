import tkinter as tk
from tkinter import messagebox
from gui.alat_gui import AlatGUI

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

        tk.Button(
            self.window,
            text="Peminjaman Alat",
            width=20,
            command=self.peminjaman
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Logout",
            width=25,
            height=2,
            fg="white",
            bg="red", # Memberi warna berbeda untuk logout
            command=self.logout
        ).pack(pady=10)

        self.window.mainloop()

    def kelola_alat(self):
        AlatGUI()

    def kelola_kategori(self):
        messagebox.showinfo("Info", "Menu Kelola Kategori")

    def peminjaman(self):
        messagebox.showinfo("Info", "Menu Peminjaman")

    def logout(self):
        konfirmasi = messagebox.askyesno("Logout", "Apakah Anda yakin ingin keluar?")
        if konfirmasi:
            self.window.destroy()