mnu = ["lele", "ayam","ikan","esteh"]
harga = [10000, 14000, 12500, 5000]
pembeli = [2,4,3,3] 

def menu():
    print("Menu Warung Makan Alpro")
    print("1. Lele - Rp. 10,000")
    print("2. Ayam - Rp. 14,000")
    print("3. Tahu - Rp. 12,500")
    print("4. esteh - Rp. 12,500")
menu()

def pembayaran(mnnu, harga, jumlah):
    subtotal = harga * jumlah
    print(f"{mnnu}: {jumlah} x {harga} = {subtotal}")
    return subtotal

ttlpndptan = 0

print("Rekap Pembayaran:")
for i in range(len(mnu)):
    subtotal = pembayaran(mnu[i], harga[i], pembeli[i])
    ttlpndptan += subtotal
    
print(f"Total pembayaran hari ini adalah: {ttlpndptan}")