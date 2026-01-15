import tkinter as tk
from tkinter import messagebox
from datetime import date
from src.database.database import Database
from src.models.peminjaman import Peminjaman
from src.models.alat import Alat


class PeminjamanGUI:
    def __init__(self):
        self.db = Database()
        self.peminjaman_model = Peminjaman(self.db)
        self.alat_model = Alat(self.db)

        self.window = tk.Toplevel()
        self.window.title("Peminjaman Alat")

        tk.Label(self.window, text="Nama Peminjam").pack()
        self.nama = tk.Entry(self.window)
        self.nama.pack()

        tk.Label(self.window, text="Pilih Alat (Tersedia)").pack()
        self.listbox = tk.Listbox(self.window, width=50)
        self.listbox.pack()

        tk.Button(
            self.window,
            text="Pinjam Alat",
            command=self.pinjam
        ).pack(pady=5)

        tk.Label(self.window, text="Peminjaman Aktif").pack(pady=10)
        self.listbox_pinjam = tk.Listbox(self.window, width=60)
        self.listbox_pinjam.pack()

        tk.Button(
            self.window,
            text="Kembalikan Alat",
            command=self.kembalikan
        ).pack(pady=5)

        self.load_alat()
        self.load_peminjaman()

    def load_alat(self):
        self.listbox.delete(0, tk.END)
        query = "SELECT alat_id, nama_alat FROM alat WHERE status='Tersedia'"
        self.db.cursor.execute(query)
        for row in self.db.cursor.fetchall():
            self.listbox.insert(tk.END, f"{row[0]} | {row[1]}")

    def load_peminjaman(self):
        self.listbox_pinjam.delete(0, tk.END)
        data = self.peminjaman_model.get_peminjaman_aktif()
        for row in data:
            # pinjam_id | nama_alat | username | tanggal | alat_id
            teks = f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}"
            self.listbox_pinjam.insert(tk.END, teks)


    def pinjam(self):
        if not self.nama.get() or not self.listbox.curselection():
            messagebox.showwarning("Peringatan", "Lengkapi data")
            return

        data = self.listbox.get(self.listbox.curselection()[0]).split(" | ")
        alat_id = data[0]

        user_id = 1  # sementara (admin)

        self.peminjaman_model.pinjam_alat(
            alat_id,
            user_id,
            date.today().isoformat()
        )

        messagebox.showinfo("Sukses", "Alat berhasil dipinjam")
        self.load_alat()
        self.load_peminjaman()

    def kembalikan(self):
        if not self.listbox_pinjam.curselection():
            messagebox.showwarning("Peringatan", "Pilih data")
            return
    
        data = self.listbox_pinjam.get(
            self.listbox_pinjam.curselection()[0]
        ).split(" | ")
    
        pinjam_id = data[0]
        alat_id = data[4]
    
        self.peminjaman_model.kembalikan_alat(
            pinjam_id,
            alat_id,
            date.today().isoformat()
        )
    
        messagebox.showinfo("Sukses", "Alat dikembalikan")
        self.load_alat()
        self.load_peminjaman()

