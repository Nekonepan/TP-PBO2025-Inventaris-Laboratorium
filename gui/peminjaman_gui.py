import tkinter as tk
from tkinter import messagebox, ttk
from datetime import date
from src.database.database import Database
from src.models.peminjaman import Peminjaman
from src.models.alat import Alat
from src.session.session import Session # Menggunakan user_id dari session asli

class PeminjamanGUI:
    def __init__(self):
        self.db = Database()
        self.peminjaman_model = Peminjaman(self.db)
        self.alat_model = Alat(self.db)

        # === Window ===
        self.window = tk.Toplevel()
        self.window.title("Sistem Peminjaman Alat")
        
        # self.window.state("zoomed")
        try:
            self.window.state("zoomed")  # Windows
        except:
            self.window.attributes("-zoomed", True)  # Linux
            
        self.window.configure(bg="#F0F7FA")

        # --- HEADER ---
        header = tk.Frame(self.window, bg="#4A90E2", height=80)
        header.pack(fill="x")
        tk.Label(header, text="TRANSAKSI PEMINJAMAN ALAT", font=("Helvetica", 18, "bold"), 
                 bg="#4A90E2", fg="white").pack(pady=20)

        # --- CONTAINER UTAMA ---
        main_container = tk.Frame(self.window, bg="#F0F7FA")
        main_container.pack(fill="both", expand=True, padx=40, pady=20)

        # --- KOLOM KIRI (FORM PEMINJAMAN BARU) ---
        self.left_frame = tk.LabelFrame(main_container, text=" Form Pinjam Alat ", font=("Helvetica", 10, "bold"),
                                        bg="white", padx=20, pady=20, fg="#4A90E2", bd=2)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

        tk.Label(self.left_frame, text="Nama Peminjam:", bg="white", font=("Helvetica", 9)).pack(anchor="w")
        self.nama = tk.Entry(self.left_frame, font=("Helvetica", 11), bd=1, relief="solid")
        self.nama.pack(fill="x", pady=(5, 15), ipady=5)
        # Otomatis isi nama dari session jika ada
        if Session.username:
            self.nama.insert(0, Session.username)

        tk.Label(self.left_frame, text="Pilih Alat yang Tersedia:", bg="white", font=("Helvetica", 9)).pack(anchor="w")
        
        # Tabel Alat Tersedia
        columns_alat = ("id", "nama")
        self.tree_alat = ttk.Treeview(self.left_frame, columns=columns_alat, show="headings", height=10)
        self.tree_alat.heading("id", text="ID")
        self.tree_alat.heading("nama", text="Nama Alat")
        self.tree_alat.column("id", width=50, anchor="center")
        self.tree_alat.pack(fill="both", expand=True, pady=10)

        tk.Button(self.left_frame, text="➕ PROSES PINJAM", command=self.pinjam,
                  bg="#4A90E2", fg="white", font=("Helvetica", 10, "bold"), bd=0, cursor="hand2").pack(fill="x", ipady=10)

        # --- KOLOM KANAN (DAFTAR PINJAMAN AKTIF) ---
        self.right_frame = tk.LabelFrame(main_container, text=" Peminjaman Aktif (Belum Kembali) ", font=("Helvetica", 10, "bold"),
                                         bg="white", padx=20, pady=20, fg="#4A90E2", bd=2)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

        # Tabel Peminjaman Aktif
        columns_pinjam = ("id", "alat", "peminjam", "tgl", "alat_id")
        self.tree_pinjam = ttk.Treeview(self.right_frame, columns=columns_pinjam, show="headings", height=10)
        self.tree_pinjam.heading("id", text="ID Pinjam")
        self.tree_pinjam.heading("alat", text="Alat")
        self.tree_pinjam.heading("peminjam", text="Peminjam")
        self.tree_pinjam.heading("tgl", text="Tanggal")
        self.tree_pinjam.heading("alat_id", text="ID Alat")
        
        # Sembunyikan kolom ID Alat (hanya untuk sistem)
        self.tree_pinjam.column("id", width=70, anchor="center")
        self.tree_pinjam.column("alat_id", width=0, stretch=tk.NO) 
        
        self.tree_pinjam.pack(fill="both", expand=True, pady=(0, 10))

        tk.Button(self.right_frame, text="↩️ KEMBALIKAN ALAT", command=self.kembalikan,
                  bg="#5CB85C", fg="white", font=("Helvetica", 10, "bold"), bd=0, cursor="hand2").pack(fill="x", ipady=10)

        # Load Initial Data
        self.load_alat()
        self.load_peminjaman()

    def load_alat(self):
        for i in self.tree_alat.get_children(): self.tree_alat.delete(i)
        query = "SELECT alat_id, nama_alat FROM alat WHERE status='Tersedia'"
        self.db.cursor.execute(query)
        for row in self.db.cursor.fetchall():
            self.tree_alat.insert("", tk.END, values=row)

    def load_peminjaman(self):
        for i in self.tree_pinjam.get_children(): self.tree_pinjam.delete(i)
        data = self.peminjaman_model.get_peminjaman_aktif()
        for row in data:
            # row: (pinjam_id, nama_alat, username, tanggal, alat_id)
            self.tree_pinjam.insert("", tk.END, values=row)

    def pinjam(self):
        selected = self.tree_alat.focus()
        if not self.nama.get() or not selected:
            messagebox.showwarning("Peringatan", "Silahkan isi nama dan pilih alat dari tabel!")
            return

        alat_id = self.tree_alat.item(selected, 'values')[0]
        user_id = Session.user_id if Session.user_id else 1 # Ambil dari session asli

        self.peminjaman_model.pinjam_alat(alat_id, user_id, date.today().isoformat())
        messagebox.showinfo("Sukses", "Alat berhasil dipinjam!")
        self.load_alat()
        self.load_peminjaman()

    def kembalikan(self):
        selected = self.tree_pinjam.focus()
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih data peminjaman yang ingin dikembalikan!")
            return

        values = self.tree_pinjam.item(selected, 'values')
        pinjam_id = values[0]
        alat_id = values[4] # Diambil dari kolom alat_id yang disembunyikan

        self.peminjaman_model.kembalikan_alat(pinjam_id, alat_id, date.today().isoformat())
        messagebox.showinfo("Sukses", "Alat telah dikembalikan ke laboratorium.")
        self.load_alat()
        self.load_peminjaman()