class Peminjaman:
    def __init__(self, db):
        self.db = db

    def pinjam_alat(self, alat_id, user_id, tanggal_pinjam):
        query = """
        INSERT INTO peminjaman (alat_id, user_id, tanggal_pinjam, status_pinjam)
        VALUES (?, ?, ?, 'Dipinjam')
        """
        self.db.cursor.execute(query, (alat_id, user_id, tanggal_pinjam))
        self.db.conn.commit()

        # update status alat
        self.db.cursor.execute(
            "UPDATE alat SET status='Dipinjam' WHERE alat_id=?",
            (alat_id,)
        )
        self.db.conn.commit()

    def kembalikan_alat(self, pinjam_id, alat_id, tanggal_kembali):
        query = """
        UPDATE peminjaman
        SET tanggal_kembali=?, status_pinjam='Dikembalikan'
        WHERE pinjam_id=?
        """
        self.db.cursor.execute(query, (tanggal_kembali, pinjam_id))
        self.db.conn.commit()

        # update status alat
        self.db.cursor.execute(
            "UPDATE alat SET status='Tersedia' WHERE alat_id=?",
            (alat_id,)
        )
        self.db.conn.commit()

    def get_peminjaman_aktif(self):
        query = """
        SELECT p.pinjam_id,
               a.nama_alat,
               u.username,
               p.tanggal_pinjam,
               a.alat_id
        FROM peminjaman p
        JOIN alat a ON p.alat_id = a.alat_id
        JOIN user u ON p.user_id = u.user_id
        WHERE p.status_pinjam = 'Dipinjam'
        """
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
