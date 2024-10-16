class civitascademic {
    private String nama;
    private String nik;
    private String status;
    private String jenisKelamin;

    public civitascademic(String nama, String nik, String status, String jenisKelamin) {
        this.nama = nama;
        this.nik = nik;
        this.status = status;
        this.jenisKelamin = jenisKelamin;
    }

    public int hitungTunjangan() {
        if (status.equals("menikah")) {
            if (jenisKelamin.equals("Laki-laki")) {
                return 25000;
            } else if (jenisKelamin.equals("Perempuan")) {
                return 20000;
            }
        }
        return 15000;
    }

    public int hitungPendapatan() {
        int pendapatanPokok = jenisKelamin.equals("Laki-laki") ? 6000 : 5000;
        return hitungTunjangan() + pendapatanPokok;
    }

    public void tampilkanInfo() {
        System.out.println("Civitas Akademik");
        System.out.println("Nama: " + nama);
        System.out.println("NIK: " + nik);
        System.out.println("Jenis Kelamin: " + jenisKelamin);
        System.out.println("Pendapatan: " + hitungPendapatan());
    }

    public static void main(String[] args) {
        civitascademic civitas = new civitascademic("Tarian", "1234450593021", "menikah", "Perempuan");
        civitas.tampilkanInfo();
    }
}
