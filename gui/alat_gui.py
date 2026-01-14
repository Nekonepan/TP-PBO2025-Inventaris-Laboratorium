import tkinter as tk
from tkinter import messagebox
from src.database.database import Database
from src.models.alat import Alat

class AlatGUI:
    def __init__(self):
        self.selected_id = None
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

        tk.Button(
            self.window,
            text="Update Alat",
            command=self.update_alat
        ).pack(pady=5)

        tk.Button(
            self.window,
            text="Hapus Alat",
            command=self.hapus_alat
        ).pack(pady=5)

        tk.Label(self.window, text="Daftar Alat").pack(pady=5)
        self.listbox = tk.Listbox(self.window, width=50)
        self.listbox.pack()

        self.listbox.bind("<<ListboxSelect>>", self.select_item)

        self.load_data()

    def select_item(self, event):
        try:
            index = self.listbox.curselection()[0]
            data = self.listbox.get(index).split(" | ")

            self.selected_id = data[0]

            self.nama.delete(0, tk.END)
            self.nama.insert(0, data[1])

            self.kondisi.delete(0, tk.END)
            self.kondisi.insert(0, data[2])

            self.status.delete(0, tk.END)
            self.status.insert(0, data[3])
        except:
            pass

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
        for row in data:
            teks = f"{row[0]} | {row[1]} | {row[2]} | {row[3]}"
            self.listbox.insert(tk.END, teks)

    def clear_form(self):
        self.selected_id = None
        self.nama.delete(0, tk.END)
        self.kondisi.delete(0, tk.END)
        self.status.delete(0, tk.END)
        self.status.insert(0, "Tersedia")


    def update_alat(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu")
            return

        self.alat_model.update_alat(
            self.selected_id,
            self.nama.get(),
            self.kondisi.get(),
            self.status.get()
        )
        messagebox.showinfo("Sukses", "Data berhasil diupdate")
        self.load_data()
        self.clear_form()


    def hapus_alat(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data terlebih dahulu")
            return

        self.alat_model.delete_alat(self.selected_id)
        messagebox.showinfo("Sukses", "Data berhasil dihapus")
        self.load_data()
        self.clear_form()
