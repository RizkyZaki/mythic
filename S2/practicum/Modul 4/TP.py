from prettytable import PrettyTable
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('inventars_buku.db')
cursor = conn.cursor()
def create_table(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='buku'")
    result = cursor.fetchone()
    if result:
        print("Tabel sudah ada.")
    else:
        cursor.execute("""CREATE TABLE buku (
                          id_buku INTEGER PRIMARY KEY,
                          judul TEXT NOT NULL,
                          penulis TEXT NOT NULL,
                          tahun_terbit INTEGER,
                          genre TEXT,
                          stok INTEGER NOT NULL
                          )""")
        print("Tabel berhasil dibuat.")

def insert_book(cursor):
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun_terbit = input("Masukkan tahun terbit: ")
    genre = input("Masukkan genre buku: ")
    stok = input("Masukkan jumlah stok: ")

    cursor.execute("INSERT INTO buku (judul, penulis, tahun_terbit, genre, stok) VALUES (?, ?, ?, ?, ?)",
                   (judul, penulis, tahun_terbit, genre, stok))
    conn.commit()
    print("Data buku berhasil dimasukkan.")

def display_books(cursor):
    cursor.execute("SELECT * FROM buku")
    rows = cursor.fetchall()
    if rows:
        table = PrettyTable()
        table.field_names = ["ID Buku", "Judul", "Penulis", "Tahun Terbit", "Genre", "Stok"]
        for row in rows:
            table.add_row(row)
        print(table)
    else:
        print("Tidak ada data buku.")

def delete_book(cursor):
    id_buku = input("Masukkan ID buku yang akan dihapus: ")
    cursor.execute("SELECT * FROM buku WHERE id_buku = ?", (id_buku,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM buku WHERE id_buku = ?", (id_buku,))
        conn.commit()
        print("Buku berhasil dihapus.")
    else:
        print("ID buku tidak ditemukan.")

def display_data(cursor):
    cursor.execute("SELECT genre, COUNT(*) as count FROM buku GROUP BY genre")
    rows = cursor.fetchall()
    if rows:
        genres = [row[0] for row in rows]
        counts = [row[1] for row in rows]

        plt.figure(figsize=(10, 6))
        plt.bar(genres, counts, color='skyblue')
        plt.xlabel('Genre')
        plt.ylabel('Jumlah Buku')
        plt.title('Jumlah Buku per Genre')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
    else:
        print("Tidak ada data buku.")

while True:
    print("=====================================")
    print("Menu :")
    print('1. Buat Tabel')
    print('2. Masukkan Buku')
    print('3. Tampilkan Buku')
    print('4. Hapus Buku')
    print('5. Tampilkan Data')
    print('6. Keluar')
    print("=====================================")
    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 1:
        create_table(cursor)
    elif pilihan == 2:
        insert_book(cursor)
    elif pilihan == 3:
        display_books(cursor)
    elif pilihan == 4:
        delete_book(cursor)
    elif pilihan == 5:
        display_data(cursor)
    elif pilihan == 6:
        print("Terima Kasih Program berakhir.")
        break

cursor.close()
conn.close()
