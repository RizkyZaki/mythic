# import mysql.connector
# import numpy as np
# import matplotlib.pyplot as plt
# import cv2

# # Koneksi ke database
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     port='3306',
#     database="lahan_elsa"
# )

# def create_synthetic_image(size=100):
#     # Membuat citra sintetik yang lebih realistis
#     red_band = np.random.rand(size, size) * 0.5  # Nilai red band
#     nir_band = np.random.rand(size, size) * 0.5 + 0.5  # Nilai NIR band
#     return red_band, nir_band

# def calculate_ndvi(red_band, nir_band):
#     # Menghindari pembagian dengan nol
#     bottom = (nir_band + red_band)
#     bottom[bottom == 0] = 1

#     # Menghitung NDVI
#     ndvi = (nir_band - red_band) / bottom
#     return ndvi

# def tampilkan_data():
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT * FROM lahan")
#     myresult = mycursor.fetchall()
#     for x in myresult:
#         print(x)

# def tambah():
#     mycursor = mydb.cursor()

#     nama = str(input("Masukkan Nama Lahan: "))
#     deskripsi = str(input("Masukkan deskripsi: "))
#     informasi_detail = str(input("Masukkan Informasi Detail: "))
#     informasi_posisi = str(input("Masukkan Informasi Posisi: "))

#     # Membuat data citra sintetik untuk red dan NIR band
#     red_band, nir_band = create_synthetic_image()

#     # Menghitung NDVI
#     ndvi = calculate_ndvi(red_band, nir_band)
#     ndvi_mean = np.mean(ndvi)  # Simpan NDVI rata-rata ke database

#     sql = "INSERT INTO lahan (nama, deskripsi, informasi_detail, informasi_posisi, ndvi) VALUES (%s, %s, %s, %s, %s)"
#     val = (nama, deskripsi, informasi_detail, informasi_posisi, ndvi_mean)
#     mycursor.execute(sql, val)

#     mydb.commit()
#     print(mycursor.rowcount, "Data Masuk.")

# def visualisasi_ndvi():
#     id_data = int(input("Masukkan ID data untuk visualisasi NDVI: "))
    
#     mycursor = mydb.cursor()
#     sql = "SELECT nama, deskripsi, informasi_detail, informasi_posisi, ndvi FROM lahan WHERE id = %s"
#     val = (id_data,)
#     mycursor.execute(sql, val)
#     result = mycursor.fetchone()
    
#     if result:
#         print("Detail Data Lahan:")
#         print(f"Nama Lahan: {result[0]}")
#         print(f"Deskripsi: {result[1]}")
#         print(f"Informasi Detail: {result[2]}")
#         print(f"Informasi Posisi: {result[3]}")
#         ndvi_mean = result[4]

#         # Membuat data citra sintetik untuk red dan NIR band
#         red_band, nir_band = create_synthetic_image()

#         # Menghitung NDVI
#         ndvi = calculate_ndvi(red_band, nir_band)

#         # Visualisasi NDVI
#         plt.figure(figsize=(10, 6))
#         ndvi_plot = plt.imshow(ndvi, cmap='RdYlGn')
#         plt.colorbar(ndvi_plot, orientation='vertical', label='NDVI')
#         plt.title(f'NDVI Visualization for ID {id_data}')
#         plt.xlabel('X Coordinate')
#         plt.ylabel('Y Coordinate')
#         plt.show()

#         ndvi_image_normalized = cv2.normalize(ndvi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
#         cv2.imshow(f'NDVI Visualization for ID {id_data}', ndvi_image_normalized)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#     else:
#         print("Data dengan ID tersebut tidak ditemukan.")

# while True:
#     print("=====================================")
#     print("Menu :")
#     print("1. Tampil Data")
#     print("2. Tambah Data")
#     print("3. Visualisasi NDVI")
#     print("4. Keluar")
#     print("=====================================")
#     pilihan = int(input("Masukkan pilihan Anda: "))
#     if pilihan == 1:
#         tampilkan_data()
#     elif pilihan == 2:
#         tambah()
#     elif pilihan == 3:
#         visualisasi_ndvi()
#     elif pilihan == 4:
#         print("Keluar Dari Program")
#         break
#     else:
#         print("Pilihan tidak valid, silakan coba lagi.")
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Fungsi untuk menghitung NDVI
def calculate_ndvi(image):
    # Mengasumsikan band Red ada di channel 0 dan band NIR ada di channel 1
    red_band = image[:, :, 0].astype(float)
    nir_band = image[:, :, 1].astype(float)

    # Menghindari pembagian dengan nol
    bottom = (nir_band + red_band)
    bottom[bottom == 0] = 1

    # Menghitung NDVI
    ndvi = (nir_band - red_band) / bottom
    return ndvi

# Membaca gambar contoh (misalnya gambar harus memiliki 3 channel RGB atau 4 channel RGBA)
image = cv2.imread('sawit2.jpg')

# Mengkonversi gambar ke dalam format yang bisa digunakan (misalnya konversi ke RGB jika perlu)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Menghitung NDVI
ndvi = calculate_ndvi(image)

# Visualisasi NDVI
plt.figure(figsize=(10, 6))
ndvi_plot = plt.imshow(ndvi, cmap='RdYlGn')
plt.colorbar(ndvi_plot, orientation='vertical', label='NDVI')
plt.title('NDVI Visualization')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.show()
