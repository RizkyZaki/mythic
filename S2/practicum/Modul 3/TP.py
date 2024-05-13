import pandas as pd

df = pd.read_csv('raw-data/DataPendahuluan.csv')

df['Tingkat_Penyelesaian_Pendidikan'] = df['Tingkat_Penyelesaian_Pendidikan'].astype(float)
df['Tingkat_Setengah_Pengangguran'] = df['Tingkat_Setengah_Pengangguran'].astype(float)

def menu_pendidikan_tertinggi():
    highest_education = df.nlargest(5, 'Tingkat_Penyelesaian_Pendidikan')[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']]
    print("5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi:")
    print(highest_education)

def menu_pengangguran_tertinggi():
    highest_unemployment = df.nlargest(5, 'Tingkat_Setengah_Pengangguran')[['Provinsi', 'Tingkat_Setengah_Pengangguran']]
    print("5 Kota dengan Tingkat Pengangguran Tertinggi:")
    print(highest_unemployment)

def menu_pendidikan_terendah():
    lowest_education = df.nsmallest(5, 'Tingkat_Penyelesaian_Pendidikan')[['Provinsi', 'Tingkat_Penyelesaian_Pendidikan']]
    print("5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah:")
    print(lowest_education)

def menu_pengangguran_terendah():
    lowest_unemployment = df.nsmallest(5, 'Tingkat_Setengah_Pengangguran')[['Provinsi', 'Tingkat_Setengah_Pengangguran']]
    print("5 Kota dengan Tingkat Pengangguran Terendah:")
    print(lowest_unemployment)

def menu_tampilkan_dataframe():
    print("Seluruh Data Frame:")
    print(df.to_string(index=True))




# Menu
while True:
    print("\nMenu:")
    print("1. 5 Kota dengan Tingkat Penyelesaian Pendidikan Tertinggi")
    print("2. 5 Kota dengan Tingkat Pengangguran Tertinggi")
    print("3. 5 Kota dengan Tingkat Penyelesaian Pendidikan Terendah")
    print("4. 5 Kota dengan Tingkat Pengangguran Terendah")
    print("5. Tampilkan Seluruh DataFrame")
    print("0. Keluar dari Aplikasi")
    
    menu = input("Pilih menu: ")
    
    if menu == '1':
        menu_pendidikan_tertinggi()
    elif menu == '2':
        menu_pengangguran_tertinggi()
    elif menu == '3':
        menu_pendidikan_terendah()
    elif menu == '4':
        menu_pengangguran_terendah()
    elif menu == '5':
        menu_tampilkan_dataframe()
    elif menu == '0':
        print("Keluar dari Aplikasi.")
        break
    else:
        print("Menu tidak valid. Silakan pilih menu yang sesuai.")
