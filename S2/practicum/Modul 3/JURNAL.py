import pandas as pd


def muat_data():
    # Hint: Isi dengan fungsi untuk memuat data dari file CSV (fungsi untuk membaca data csv?)
    df = pd.read_csv("Jurnal.csv")
    return df

def tampilkan_data_frame(data):
    # Hint: Isi dengan fungsi untuk menampilkan seluruh dataframe (print data dari csvnya?)
    print(data.to_string())


def tampilkan_gambaran_umum(data):
    # Hint: Isi dengan fungsi untuk menampilkan informasi umum tentang data (print ringkasan statistik deskriptif dari data?)
    print(data.info())
    print(data.describe())

def sepuluh_provinsi_teratas(data):
    # Hint: Isi dengan fungsi untuk menampilkan sepuluh provinsi teratas pada tahun 2023  (pakai sort value)
    data2023 = data.sort_values("2023", ascending=False)
    print(data2023.head(10))

def provinsi_dengan_peningkatan_terbesar(data):
    # Hint: Isi dengan fungsi untuk menemukan provinsi dengan peningkatan terbesar dari 2021 ke 2023 (pakai data.loc)
    data['Peningkatan'] = data['2023'] - data['2021']
  
    provinsi_tertinggi = data.loc[data['Peningkatan'].idxmax()]
    
    print(f"Provinsi dengan peningkatan terbesar dari 2021 ke 2023: {provinsi_tertinggi['Provinsi']} ({provinsi_tertinggi['Peningkatan']})")
   

def analisis_korelasi(data):
    # Hint: Isi dengan fungsi untuk menganalisis korelasi antara tahun (fungsi buat mencari korelasi?)
    korelasi = data[['2021', '2022', '2023']].corr()
    
    print("Matrix Korelasi:")
    print(korelasi)

def kinerja_provinsi_tertentu(data, nama_provinsi):
    # Hint: Isi dengan fungsi untuk menampilkan kinerja provinsi tertentu (pakai data.loc dan kondisi jika data tidak ada)
    data_provinsi = data[data['Provinsi'] == nama_provinsi]
    
    if len(data_provinsi) == 0:
        print("Data untuk provinsi", nama_provinsi, "tidak ditemukan.")
    else:
        print("Data untuk provinsi", nama_provinsi, ":")
        print(data_provinsi)

def utama():
    data = muat_data()
    while True:
        print("=====================================")
        print("Menu Analisis Data:")
        # Hint: Tambahkan pilihan menu sesuai deskripsi soal
        print('1. Tampilkan  seluruh data frame')
        print('2. Tampilkan gambaran umum data')
        print('3. Tampilkan 10 provinsi terbaik Tahun 2023')
        print('4. Tampilkan provinsi dengan peningkatan terbesar Tahun 2021-2023')
        print('5. Analisis korelasi antar tahun')
        print('6. Tampilkan performa provinsi tertentu')
        print('7. Keluar')
        print("=====================================")
        pilihan = int(input("Masukkan pilihan Anda: "))
        # Hint: Tambahkan if else untuk setiap pilihan menu sesuai deskripsi soal
        if(pilihan == 1):
          data = muat_data()
          tampilkan_data_frame(data)
        elif(pilihan == 2):
          data = muat_data()
          tampilkan_gambaran_umum(data)
        elif(pilihan == 3):
          data = muat_data()
          sepuluh_provinsi_teratas(data)
        elif(pilihan == 4):
          data = muat_data()
          provinsi_dengan_peningkatan_terbesar(data)
        elif(pilihan == 5):
          data = muat_data()
          analisis_korelasi(data)
        elif(pilihan == 6):
          prov = str(input("Masukkan Nama Provinsi:"))
          data = muat_data()
          kinerja_provinsi_tertentu(data,prov)
        elif(pilihan == 7):
          print("Keluar Dari Program")
          break

if __name__ == "__main__":
    utama()
