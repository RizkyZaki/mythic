import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV
df = pd.read_csv('raw-data/data-penjualan-avanza.csv', delimiter=';')

# Menampilkan data
print(df)

# Mencari keuntungan tertinggi dan tahunnya
keuntungan_tertinggi = df['Keuntungan'].max()
indeks_keuntungan_tertinggi = df['Keuntungan'].idxmax()
tahun_keuntungan_tertinggi = df.loc[indeks_keuntungan_tertinggi, "Tahun"]

# Menampilkan keuntungan tertinggi dan tahunnya
print("Keuntungan tertinggi:", keuntungan_tertinggi)
print("Tahun keuntungan tertinggi:", tahun_keuntungan_tertinggi)

plt.figure(figsize=(8, 6))
plt.title("Grafik Keuntungan PT. AVANZA dari tahun ke tahun")
plt.xlabel("Tahun")
plt.ylabel("Keuntungan")
plt.bar(df['Tahun'], df ['Keuntungan'], color='green')
plt.grid(True)
plt.show()
plt.title("Grafik penjualan PT. AVANZA dari tahun ke tahun")
plt.xlabel("Tahun")
plt.ylabel("penjualan")
plt.bar(df['Tahun'], df['Penjualan'], color='blue')
plt.grid(True)
plt.show()