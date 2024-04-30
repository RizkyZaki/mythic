import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("raw-data/penjualan_mobil_avanza.csv", sep=';')

print(df)

avg = df["Penjualan"].mean()
print("Penjualan rata-rata:", avg)

penjualan_tertinggi = df["Penjualan"].max()
print("Penjualan Tertinggi: ", penjualan_tertinggi)

penjualan_terendah = df["Penjualan"].min()
print("Penjualan Terendah: ", penjualan_terendah)

# Plot
plt.plot(df.index, df["Penjualan"], label="Penjualan")
plt.plot(df.index, [penjualan_terendah] * len(df), label="Penjualan Terendah", linestyle="--")
plt.plot(df.index, [penjualan_tertinggi] * len(df), label="Penjualan Tertinggi", linestyle="--")
plt.xlabel("Index")
plt.ylabel("Penjualan")
plt.title("Grafik Penjualan")
plt.legend()
plt.show()