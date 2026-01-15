import tkinter as tk
from tkinter import messagebox
from src.database.database import Database
from src.models.kategori import Kategori


class KategoriGUI:
    def __init__(self):
        self.db = Database()
        self.kategori_model = Kategori(self.db)
        self.selected_id = None

        self.window = tk.Toplevel()
        self.window.title("Kelola Kategori")

        tk.Label(self.window, text="Nama Kategori").pack()
        self.nama = tk.Entry(self.window)
        self.nama.pack()

        tk.Button(
            self.window,
            text="Simpan Kategori",
            command=self.simpan_kategori
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Update Kategori",
            command=self.update_kategori
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Hapus Kategori",
            command=self.hapus_kategori
        ).pack(pady=5)

        tk.Label(self.window, text="Daftar Kategori").pack(pady=10)
        self.listbox = tk.Listbox(self.window, width=40)
        self.listbox.pack()

        self.listbox.bind("<<ListboxSelect>>", self.select_item)

        self.load_data()

    def load_data(self):
        self.listbox.delete(0, tk.END)
        data = self.kategori_model.get_all_kategori()
        for row in data:
            teks = f"{row[0]} | {row[1]}"
            self.listbox.insert(tk.END, teks)

    def select_item(self, event):
        try:
            index = self.listbox.curselection()[0]
            data = self.listbox.get(index).split(" | ")

            self.selected_id = data[0]
            self.nama.delete(0, tk.END)
            self.nama.insert(0, data[1])
        except:
            pass

    def simpan_kategori(self):
        if not self.nama.get():
            messagebox.showwarning("Peringatan", "Nama kategori kosong")
            return

        self.kategori_model.tambah_kategori(self.nama.get())
        messagebox.showinfo("Sukses", "Kategori ditambahkan")
        self.load_data()
        self.clear_form()

    def update_kategori(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih kategori terlebih dahulu")
            return

        self.kategori_model.update_kategori(
            self.selected_id,
            self.nama.get()
        )
        messagebox.showinfo("Sukses", "Kategori diupdate")
        self.load_data()
        self.clear_form()

    def hapus_kategori(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih kategori terlebih dahulu")
            return

        self.kategori_model.delete_kategori(self.selected_id)
        messagebox.showinfo("Sukses", "Kategori dihapus")
        self.load_data()
        self.clear_form()

    def clear_form(self):
        self.selected_id = None
        self.nama.delete(0, tk.END)
