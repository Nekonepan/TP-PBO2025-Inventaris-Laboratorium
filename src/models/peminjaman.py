class Peminjaman:
    def __init__(self, db):
        self.db = db

    def pinjam_alat(self, alat_id, nama_peminjam, tanggal_pinjam):
        query = """
        INSERT INTO peminjaman (alat_id, nama_peminjam, tanggal_pinjam, status)
        VALUES (?, ?, ?, 'Dipinjam')
        """
        self.db.cursor.execute(query, (alat_id, nama_peminjam, tanggal_pinjam))
        self.db.conn.commit()

        # update status alat
        self.db.cursor.execute(
            "UPDATE alat SET status='Dipinjam' WHERE alat_id=?",
            (alat_id,)
        )
        self.db.conn.commit()

    def kembalikan_alat(self, peminjaman_id, alat_id, tanggal_kembali):
        query = """
        UPDATE peminjaman
        SET tanggal_kembali=?, status='Dikembalikan'
        WHERE peminjaman_id=?
        """
        self.db.cursor.execute(query, (tanggal_kembali, peminjaman_id))
        self.db.conn.commit()

        # update status alat
        self.db.cursor.execute(
            "UPDATE alat SET status='Tersedia' WHERE alat_id=?",
            (alat_id,)
        )
        self.db.conn.commit()

    def get_peminjaman_aktif(self):
        query = """
        SELECT p.peminjaman_id, a.nama_alat, p.nama_peminjam, p.tanggal_pinjam, a.alat_id
        FROM peminjaman p
        JOIN alat a ON p.alat_id = a.alat_id
        WHERE p.status='Dipinjam'
        """
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
