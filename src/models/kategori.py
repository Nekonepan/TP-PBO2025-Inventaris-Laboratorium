class Kategori:
    def __init__(self, db):
        self.db = db

    def tambah_kategori(self, nama):
        query = "INSERT INTO kategori (nama_kategori) VALUES (?)"
        self.db.cursor.execute(query, (nama,))
        self.db.conn.commit()

    def get_all_kategori(self):
        query = "SELECT kategori_id, nama_kategori FROM kategori"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    def update_kategori(self, kategori_id, nama):
        query = """
        UPDATE kategori
        SET nama_kategori=?
        WHERE kategori_id=?
        """
        self.db.cursor.execute(query, (nama, kategori_id))
        self.db.conn.commit()

    def delete_kategori(self, kategori_id):
        query = "DELETE FROM kategori WHERE kategori_id=?"
        self.db.cursor.execute(query, (kategori_id,))
        self.db.conn.commit()
