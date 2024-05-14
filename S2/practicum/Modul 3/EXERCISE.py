import pandas as pd

# Membaca data dari file CSV
df = pd.read_csv('Top 50 Football Player.csv')

# Menambahkan kolom rata-rata
df['Average'] = (df['Speed'] + df['Stamina'] + df['Attack'] + df['Defense']) / 4

# Mengurutkan data berdasarkan rata-rata tertinggi
sorted_df = df.sort_values("Average", ascending=False)

# Memfilter data berdasarkan umur antara 23 dan 28 tahun
filtered_df = sorted_df[(sorted_df["Umur"] >= 23) & (sorted_df["Umur"] <= 28)]

# Mengambil 11 data teratas
data = filtered_df.head(11)

# Menghitung total harga
total_harga = df["Harga ($)"].sum() 

# Mencari nilai tertinggi dari setiap kolom ability beserta nama pemain
max_speed_player = df.loc[df["Speed"].idxmax(), "Nama"]
max_stamina_player = df.loc[df["Stamina"].idxmax(), "Nama"]
max_attack_player = df.loc[df["Attack"].idxmax(), "Nama"]
max_defense_player = df.loc[df["Defense"].idxmax(), "Nama"]

# Menampilkan data
print(data)
print(f"Total Harga ${float(total_harga)}")
print(f"Speed Tertinggi = {max_speed_player} ({df['Speed'].max()})")
print(f"Stamina Tertinggi = {max_stamina_player} ({df['Stamina'].max()})")
print(f"Attack Tertinggi = {max_attack_player} ({df['Attack'].max()})")
print(f"Defense Tertinggi = {max_defense_player} ({df['Defense'].max()})")
