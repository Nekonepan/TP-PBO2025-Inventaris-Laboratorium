class Alat:
    def __init__(self, db):
        self.db = db

    def tambah_alat(self, nama, kondisi, status, kategori_id):
        query = """
        INSERT INTO alat (nama_alat, kondisi, status, kategori_id)
        VALUES (?, ?, ?, ?)
        """
        self.db.cursor.execute(query, (nama, kondisi, status, kategori_id))
        self.db.conn.commit()

    def get_all_alat(self):
        query = "SELECT alat_id, nama_alat, kondisi, status FROM alat"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
