#import library sqlite 3 dan maplotlib
import sqlite3
import matplotlib.pyplot as plt
from prettytable import PrettyTable

#buatlah database yang dapat diakses secara keseluruhan

#Buatlah fungsi untuk membuat tabel
def buattabel(): 
    conn = sqlite3.connect('database_obat.db')
    curs = conn.cursor()
    curs.execute("""
                  CREATE TABLE IF NOT EXISTS table_obat(
                    id_obat INTEGER NOT NULL PRIMARY KEY,
                    nama VARCHAR(100) NOT NULL,
                    harga INTEGER(100) NOT NULL,
                    stok INTEGER(11) NOT NULL,
                    jenis_obat VARCHAR(100) NOT NULL
                    )
                """)
    print("Table Berhasil Dibuat")
    conn.commit()
    conn.close()

# #Buatlah fungsi untuk menambahkan obat
def tambah_obat(id_obat, nama, harga, stok, jenis_obat):
    conn = sqlite3.connect('database_obat.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO table_obat(id_obat,nama,harga,stok,jenis_obat) VALUES (?,?,?,?,?)",(id_obat, nama, harga, stok, jenis_obat))
    print("Data berhasil Dibuat")
    conn.commit()
    conn.close()
    
# #Buatlah fungsi untuk hapus obat berdasarkan id obat
def hapus_obat(id_obat):
    conn = sqlite3.connect('database_obat.db')
    curs = conn.cursor()
    curs.execute("DELETE FROM table_obat WHERE id_obat=?",(id_obat,))
    print("data berhasil Dihapus")
    conn.commit()
    conn.close()
    
# #Buatlah fungsi untuk mencari obat berdasarkan id
def cari_obat(id_obat : int):
    conn = sqlite3.connect('database_obat.db')
    curs = conn.cursor()
    curs.execute(f"""
                  SELECT * FROM table_obat
                  WHERE id_obat LIKE "{id_obat}%" 
                """)
    rows = curs.fetchall()
    if rows:
        table = PrettyTable()
        table.field_names = ["ID Obat", "Nama", "Harga", "Stok", "Jenis Obat"]
        for row in rows:
            table.add_row(row)
        print(table)
    else:
        print(f"ID Obat {id_obat} Tidak Ditemukan.")
    
    conn.commit()
    conn.close()

# #Buatlah fungsi untuk menampilkan seluruh obat yang ada pada tabel
def tampilkan_obat():
    conn = sqlite3.connect('database_obat.db')
    curs = conn.cursor()
    curs.execute("SELECT * FROM table_obat")
    rows = curs.fetchall()
    if rows:
        table = PrettyTable()
        table.field_names = ["ID Obat", "Nama", "Harga", "Stok", "Jenis Obat"]
        for row in rows:
            table.add_row(row)
        print(table)
    else:
        print("Data Kosong.")
    
    conn.commit()
    conn.close()
        
# #Buatlah fungsi untuk visualisasi data dalam bentuk bar chart
def vis_data():
    conn = sqlite3.connect('database_obat.db')
    curs = conn.cursor()
    curs.execute("""
                  SELECT nama, stok FROM table_obat
                """)
    rows = curs.fetchall()
    obat = [row[0] for row in rows]
    stok = [row[1] for row in rows]
    plt.figure(figsize=(10, 6))
    plt.bar(obat,stok, color='skyblue')
    plt.xlabel('Stok Obat')
    plt.title('Stok Keseluruhan Obat')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    conn.commit()
    conn.close()
    

#buatlah perulangan untuk menampilkan pilihan menu dan menjalankan program
while True:
    #Tampilkan menu
    print("""
          Selamat Datang Di APOTEK DASPRO!!
          Pilihan Menu :
          1. Membuat Tabel
          2. Menambahkan Obat
          3. Menghapus Obat
          4. Mencari Obat
          5. Menampilkan Data
          6. Visualisasi Data
          7. Keluar
          """)
    pilihan = int(input("Masukan pilihan menu: "))
    if pilihan == 1:
        buattabel()
    elif pilihan == 2:
        id_obat = int(input("Masukkan ID obat : "))
        nama = str(input("Masukkan Nama obat : "))
        harga = int(input("Masukkan Harga obat : "))
        stok = int(input("Masukkan Stok obat : "))
        jenis_obat = str(input("Masukkan Jenis obat : "))
        tambah_obat(id_obat, nama, harga, stok, jenis_obat)
    elif pilihan == 3:
        id_obat = int(input("Masukkan id obat Yang Akan Dihapus: "))
        hapus_obat(id_obat)
    elif pilihan == 4:
        id_obat = int(input("Masukkan ID Obat Yang Akan Dicari: "))
        cari_obat(id_obat)
    elif pilihan == 5:
        tampilkan_obat()
    elif pilihan == 6:
        vis_data()
    elif pilihan == 7:
        print("Terimakasih Telah Menggunakan layanan APOTIK DASPRO")
        break
    else :
        pass