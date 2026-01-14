import tkinter as tk
from tkinter import messagebox
from src.database.database import Database
from src.models.alat import Alat

class AlatGUI:
    def __init__(self):
        self.db = Database()
        self.alat_model = Alat(self.db)

        self.window = tk.Toplevel()
        self.window.title("Kelola Alat Laboratorium")
        self.window.geometry("400x400")

        tk.Label(self.window, text="Nama Alat").pack()
        self.nama = tk.Entry(self.window)
        self.nama.pack()

        tk.Label(self.window, text="Kondisi").pack()
        self.kondisi = tk.Entry(self.window)
        self.kondisi.pack()

        tk.Label(self.window, text="Status").pack()
        self.status = tk.Entry(self.window)
        self.status.insert(0, "Tersedia")
        self.status.pack()

        tk.Button(
            self.window,
            text="Simpan Alat",
            command=self.simpan_alat
        ).pack(pady=10)

        tk.Label(self.window, text="Daftar Alat").pack(pady=5)
        self.listbox = tk.Listbox(self.window, width=50)
        self.listbox.pack()

        self.load_data()

    def simpan_alat(self):
        nama = self.nama.get()
        kondisi = self.kondisi.get()
        status = self.status.get()

        if nama == "" or kondisi == "":
            messagebox.showwarning("Peringatan", "Data tidak boleh kosong")
            return

        self.alat_model.tambah_alat(nama, kondisi, status, 1)
        messagebox.showinfo("Sukses", "Data alat berhasil disimpan")
        self.clear_form()
        self.load_data()

    def load_data(self):
        self.listbox.delete(0, tk.END)
        data = self.alat_model.get_all_alat()
        for alat in data:
            self.listbox.insert(
                tk.END,
                f"{alat[0]} | {alat[1]} | {alat[2]} | {alat[3]}"
            )

    def clear_form(self):
        self.nama.delete(0, tk.END)
        self.kondisi.delete(0, tk.END)
        self.status.delete(0, tk.END)
        self.status.insert(0, "Tersedia")
