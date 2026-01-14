class Alat:
    def __init__(self, nama, kondisi, status, kategori_id):
        self.nama = nama
        self.kondisi = kondisi
        self.status = status
        self.kategori_id = kategori_id

    def tambah_alat(self, db):
        query = """
        INSERT INTO alat (nama_alat, kondisi, status, kategori_id)
        VALUES (?, ?, ?, ?)
        """
        db.cursor.execute(query, (self.nama, self.kondisi, self.status, self.kategori_id))
        db.conn.commit()
