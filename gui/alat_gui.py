import tkinter as tk
from tkinter import messagebox, ttk
from src.database.database import Database
from src.models.alat import Alat
from src.models.kategori import Kategori

class AlatGUI:
    def __init__(self):
        # === Model ===
        self.selected_id = None
        self.db = Database()
        self.alat_model = Alat(self.db)
        self.kategori_model = Kategori(self.db)

        # === Window ===
        self.window = tk.Toplevel()
        self.window.title("Kelola Alat Laboratorium")
        
        # self.window.state("zoomed")
        try:
            self.window.state("zoomed")  # Windows
        except:
            self.window.attributes("-zoomed", True)  # Linux
            
        self.window.configure(bg="#F0F7FA") # Warna latar biru sangat muda

        # --- HEADER ---
        header = tk.Frame(self.window, bg="#4A90E2", height=80)
        header.pack(fill="x")
        tk.Label(header, text="PENGELOLAAN ALAT LABORATORIUM", font=("Helvetica", 18, "bold"), 
                 bg="#4A90E2", fg="white").pack(pady=20)

        # --- CONTAINER UTAMA (Dua Kolom) ---
        main_container = tk.Frame(self.window, bg="#F0F7FA")
        main_container.pack(fill="both", expand=True, padx=40, pady=20)

        # --- KOLOM KIRI (FORM INPUT) ---
        self.form_frame = tk.LabelFrame(main_container, text=" Input Data Alat ", font=("Helvetica", 10, "bold"),
                                        bg="white", padx=20, pady=20, fg="#4A90E2", bd=2)
        self.form_frame.pack(side="left", fill="y", padx=(0, 20))

        # Fungsi pembantu untuk membuat label & entry rapi
        self.buat_label_entry("Nama Alat:", "nama")
        self.buat_label_entry("Kondisi:", "kondisi")
        self.buat_label_entry("Status:", "status", default="Tersedia")

        tk.Label(self.form_frame, text="Kategori:", bg="white", font=("Helvetica", 9)).pack(anchor="w", pady=(10, 0))
        self.kategori_combo = ttk.Combobox(self.form_frame, state="readonly", font=("Helvetica", 11))
        self.kategori_combo.pack(fill="x", pady=(5, 20))
        self.load_kategori()

        # --- TOMBOL-TOMBOL ---
        self.btn_simpan = tk.Button(self.form_frame, text="💾 SIMPAN DATA", command=self.simpan_alat,
                                    bg="#4A90E2", fg="white", font=("Helvetica", 10, "bold"), bd=0, cursor="hand2")
        self.btn_simpan.pack(fill="x", pady=5, ipady=8)

        self.btn_update = tk.Button(self.form_frame, text="🔄 UPDATE DATA", command=self.update_alat,
                                    bg="#5CB85C", fg="white", font=("Helvetica", 10, "bold"), bd=0, cursor="hand2")
        self.btn_update.pack(fill="x", pady=5, ipady=8)

        self.btn_hapus = tk.Button(self.form_frame, text="🗑️ HAPUS DATA", command=self.hapus_alat,
                                   bg="#D9534F", fg="white", font=("Helvetica", 10, "bold"), bd=0, cursor="hand2")
        self.btn_hapus.pack(fill="x", pady=5, ipady=8)

        # --- KOLOM KANAN (TABEL DATA) ---
        self.table_frame = tk.Frame(main_container, bg="white")
        self.table_frame.pack(side="right", fill="both", expand=True)

        # Menggunakan Treeview agar lebih rapi dari Listbox
        columns = ("id", "nama", "kondisi", "status", "kategori")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings")
        
        # Atur Header Tabel
        self.tree.heading("id", text="ID")
        self.tree.heading("nama", text="Nama Alat")
        self.tree.heading("kondisi", text="Kondisi")
        self.tree.heading("status", text="Status")
        self.tree.heading("kategori", text="Kategori")

        # Atur Lebar Kolom
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("nama", width=150)
        self.tree.column("kondisi", width=100)
        self.tree.column("status", width=100)
        self.tree.column("kategori", width=150)

        self.tree.pack(fill="both", expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.select_item)

        self.load_data()

    def buat_label_entry(self, label_text, attr_name, default=""):
        tk.Label(self.form_frame, text=label_text, bg="white", font=("Helvetica", 9)).pack(anchor="w", pady=(10, 0))
        entry = tk.Entry(self.form_frame, font=("Helvetica", 11), bd=1, relief="solid")
        entry.pack(fill="x", pady=5, ipady=5)
        if default: entry.insert(0, default)
        setattr(self, attr_name, entry)

    def load_data(self):
        # Bersihkan tabel sebelum load
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        for row in self.alat_model.get_all_alat():
            # row: (id, nama, kondisi, status, nama_kategori)
            self.tree.insert("", tk.END, values=row)

    def select_item(self, event):
        selected = self.tree.focus()
        if not selected: return
        
        values = self.tree.item(selected, 'values')
        self.selected_id = values[0]

        # Isi kembali ke form
        self.nama.delete(0, tk.END)
        self.nama.insert(0, values[1])

        self.kondisi.delete(0, tk.END)
        self.kondisi.insert(0, values[2])

        self.status.delete(0, tk.END)
        self.status.insert(0, values[3])

    def simpan_alat(self):
        kategori_index = self.kategori_combo.current()
        if kategori_index == -1:
            messagebox.showwarning("Peringatan", "Pilih kategori!")
            return

        kategori_id = self.kategori_data[kategori_index][0]
        self.alat_model.tambah_alat(self.nama.get(), self.kondisi.get(), self.status.get(), kategori_id)
        messagebox.showinfo("Sukses", "Alat berhasil disimpan")
        self.load_data()
        self.clear_form()

    def update_alat(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel!")
            return
        self.alat_model.update_alat(self.selected_id, self.nama.get(), self.kondisi.get(), self.status.get())
        messagebox.showinfo("Sukses", "Data berhasil diperbarui")
        self.load_data()
        self.clear_form()

    def hapus_alat(self):
        if not self.selected_id:
            messagebox.showwarning("Peringatan", "Pilih data di tabel!")
            return
        if messagebox.askyesno("Konfirmasi", "Hapus data ini?"):
            self.alat_model.delete_alat(self.selected_id)
            self.load_data()
            self.clear_form()

    def load_kategori(self):
        self.kategori_data = self.kategori_model.get_all_kategori()
        self.kategori_combo['values'] = [k[1] for k in self.kategori_data]

    def clear_form(self):
        self.selected_id = None
        self.nama.delete(0, tk.END)
        self.kondisi.delete(0, tk.END)
        self.status.delete(0, tk.END)
        self.status.insert(0, "Tersedia")
        self.kategori_combo.set('')