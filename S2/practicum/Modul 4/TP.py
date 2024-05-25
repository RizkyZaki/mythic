from prettytable import PrettyTable
import matplotlib.pyplot as plt
import sqlite3


def buat_tabel(cursor):
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

def buat_buku(cursor):
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahun_terbit = input("Masukkan tahun terbit: ")
    genre = input("Masukkan genre buku: ")
    stok = input("Masukkan jumlah stok: ")

    cursor.execute("INSERT INTO buku (judul, penulis, tahun_terbit, genre, stok) VALUES (?, ?, ?, ?, ?)",
                   (judul, penulis, tahun_terbit, genre, stok))
    conn.commit()
    print("Data buku berhasil dimasukkan.")

def tampilkan_buku(cursor):
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

def hapus_buku(cursor):
    id_buku = input("Masukkan ID buku yang akan dihapus: ")
    cursor.execute("SELECT * FROM buku WHERE id_buku = ?", (id_buku,))
    row = cursor.fetchone()
    if row:
        cursor.execute("DELETE FROM buku WHERE id_buku = ?", (id_buku,))
        conn.commit()
        print("Buku berhasil dihapus.")
    else:
        print("ID buku tidak ditemukan.")

def visualisasi(cursor):
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

conn = sqlite3.connect('inventaris_buku.db')
cursor = conn.cursor()
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
        buat_tabel(cursor)
    elif pilihan == 2:
        buat_buku(cursor)
    elif pilihan == 3:
        tampilkan_buku(cursor)
    elif pilihan == 4:
        hapus_buku(cursor)
    elif pilihan == 5:
        visualisasi(cursor)
    elif pilihan == 6:
        print("Terima Kasih Program berakhir.")
        break

cursor.close()
conn.close()
