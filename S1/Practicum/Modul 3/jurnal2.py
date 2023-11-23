print("===== TRANSAKSI PENJUALAN =====")

val_product = int(input("Jumlah Produk : "))
total_price = 0
for i in range(1, val_product+1):
  price = int(input(f"Harga Barang {i} : "))
  total_price += price

print(f"Total Pembayaran : {total_price}")