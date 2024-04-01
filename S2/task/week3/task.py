# Buat dictionary untuk menyimpan informasi kendaraan
kendaraan = {
    "D1122": {
        "merk": "Honda",
        "jenis": "sedan",
        "tahun_pembuatan": 2020,
        "pemilik": "Andi"
    },
    "D1714": {
        "merk": "Toyota",
        "jenis": "truck",
        "tahun_pembuatan": 2018,
        "pemilik": "Budi"
    },
    "D118F": {
        "merk": "BMW",
        "jenis": "sedan",
        "tahun_pembuatan": 2017,
        "pemilik": "Asep"
    },
    "D9971": {
        "merk": "Mercedez",
        "jenis": "sedan",
        "tahun_pembuatan": 2019,
        "pemilik": "Kevin"
    },
}

# Tampilkan informasi kendaraan dalam satu baris
for plat_nomor, info in kendaraan.items():
    print(f"Plat Nomor: {plat_nomor}, Merk: {info['merk']}, Jenis: {info['jenis']}, Tahun Pembuatan: {info['tahun_pembuatan']}, Pemilik: {info['pemilik']}")
