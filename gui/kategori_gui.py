import tkinter as tk
from tkinter import messagebox, ttk
from src.database.database import Database
from src.models.kategori import Kategori

class KategoriGUI:
    def __init__(self):
        # === Model ===
        self.db = Database()
        self.kategori_model = Kategori(self.db)
        self.selected_id = None

        # === Window ===
        self.window = tk.Toplevel()
        self.window.title("Kelola Kategori")
        self.window.state("zoomed")
        self.window.configure(bg="#F0F7FA") # Warna latar biru muda senada

        # --- HEADER ---
        header = tk.Frame(self.window, bg="#4A90E2", height=80)
        header.pack(fill="x")
        tk.Label(header, text="PENGELOLAAN KATEGORI ALAT", font=("Helvetica", 18, "bold"), 
                 bg="#4A90E2", fg="white").pack(pady=20)

        # --- CONTAINER UTAMA ---
        main_container = tk.Frame(self.window, bg="#F0F7FA")
        main_container.pack(fill="both", expand=True, padx=40, pady=20)

        # --- KOLOM KIRI (FORM INPUT) ---
        self.form_frame = tk.LabelFrame(main_container, text=" Input Kategori ", font=("Helvetica", 10, "bold"),
                                        bg="white", padx=25, pady=25, fg="#4A90E2", bd=2)
        self.form_frame.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(self.form_frame, text="Nama Kategori:", bg="white", font=("Helvetica", 10)).pack(anchor="w")
        self.nama = tk.Entry(self.form_frame, font=("Helvetica", 12), bd=1, relief="solid")
        self.nama.pack(fill="x", pady=(10, 30), ipady=8)

        # --- TOMBOL AKSI ---
        btn_style = {"font": ("Helvetica", 10, "bold"), "bd": 0, "cursor": "hand2"}

        tk.Button(self.form_frame, text="💾 SIMPAN KATEGORI", command=self.simpan_kategori,
                  bg="#4A90E2", fg="white", **btn_style).pack(fill="x", pady=5, ipady=10)

        tk.Button(self.form_frame, text="🔄 UPDATE KATEGORI", command=self.update_kategori,
                  bg="#5CB85C", fg="white", **btn_style).pack(fill="x", pady=5, ipady=10)

        tk.Button(self.form_frame, text="🗑️ HAPUS KATEGORI", command=self.hapus_kategori,
                  bg="#D9534F", fg="white", **btn_style).pack(fill="x", pady=5, ipady=10)

        # --- KOLOM KANAN (TABEL DATA) ---
        self.table_frame = tk.Frame(main_container, bg="white")
        self.table_frame.pack(side="right", fill="both", expand=True)

        # Menggunakan Treeview agar sejajar dan rapi
        columns = ("id", "nama")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        
        self.tree.heading("id", text="ID")
        self.tree.heading("nama", text="Nama Kategori")

        self.tree.column("id", width=100, anchor="center")
        self.tree.column("nama", width=400, anchor="w")

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

        self.load_data()

    def load_data(self):
        # Bersihkan tabel sebelum load ulang
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        data = self.kategori_model.get_all_kategori()
        for row in data:
            self.tree.insert("", tk.END, values=row)

    def select_item(self, event):
        selected = self.tree.focus()
        if not selected: return
        
        values = self.tree.item(selected, 'values')
        self.selected_id = values[0]
        
        self.nama.delete(0, tk.END)
        self.nama.insert(0, values[1])

    def simpan_kategori(self):
        nama_val = self.nama.get().strip()
        if not nama_val:
            messagebox.showwarning("Peringatan", "Nama kategori tidak boleh kosong!")
            return

        self.kategori_model.tambah_kategori(nama_val)
        messagebox.showinfo("Sukses", "Kategori berhasil ditambahkan")
        self.load_data()
        self.clear_form()

    def update_kategori(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih kategori di tabel lebih dulu")
            return

        self.kategori_model.update_kategori(self.selected_id, self.nama.get())
        messagebox.showinfo("Sukses", "Kategori berhasil diperbarui")
        self.load_data()
        self.clear_form()

    def hapus_kategori(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih kategori di tabel lebih dulu")
            return

        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus kategori ini?"):
            self.kategori_model.delete_kategori(self.selected_id)
            messagebox.showinfo("Sukses", "Kategori berhasil dihapus")
            self.load_data()
            self.clear_form()

    def clear_form(self):
        self.selected_id = None
        self.nama.delete(0, tk.END)