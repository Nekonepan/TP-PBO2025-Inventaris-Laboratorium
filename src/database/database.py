import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("src/database/inventaris.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def get_all_kategori(self):
        query = "SELECT kategori_id, nama_kategori FROM kategori"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()


    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS kategori (
            kategori_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_kategori TEXT,
            deskripsi TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS alat (
            alat_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_alat TEXT,
            kondisi TEXT,
            status TEXT,
            kategori_id INTEGER
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS peminjaman (
            pinjam_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tanggal_pinjam TEXT,
            tanggal_kembali TEXT,
            status_pinjam TEXT,
            alat_id INTEGER,
            user_id INTEGER
        )
        """)

        self.conn.commit()
