import java.util.ArrayList;
import java.util.Scanner;

// Class Buku mewakili sebuah buku dengan atribut judul, penulis, dan tahun terbit
class Buku {
    String judul;
    String penulis;
    int tahunTerbit;

    // Constructor untuk inisialisasi buku
    public Buku(String judul, String penulis, int tahunTerbit) {
        this.judul = judul;
        this.penulis = penulis;
        this.tahunTerbit = tahunTerbit;
    }

    // Method untuk menampilkan informasi buku
    public void tampilkanInfo() {
        System.out.println("Judul: " + this.judul);
        System.out.println("Penulis: " + this.penulis);
        System.out.println("Tahun Terbit: " + this.tahunTerbit);
    }
}

// Class Perpustakaan untuk mengelola koleksi buku
class Perpustakaan {
    ArrayList<Buku> koleksiBuku = new ArrayList<>();

    // Method untuk menambah buku ke perpustakaan
    public void tambahBuku(Buku buku) {
        koleksiBuku.add(buku);
        System.out.println("Buku berhasil ditambahkan!");
    }

    // Method untuk menampilkan semua buku di perpustakaan
    public void tampilkanSemuaBuku() {
        if (koleksiBuku.isEmpty()) {
            System.out.println("Tidak ada buku dalam perpustakaan.");
        } else {
            for (int i = 0; i < koleksiBuku.size(); i++) {
                System.out.println("\nBuku " + (i + 1));
                koleksiBuku.get(i).tampilkanInfo();
            }
        }
    }

    // Method untuk mencari buku berdasarkan judul
    public void cariBuku(String judul) {
        boolean ditemukan = false;
        for (Buku buku : koleksiBuku) {
            if (buku.judul.equalsIgnoreCase(judul)) {
                System.out.println("Buku ditemukan!");
                buku.tampilkanInfo();
                ditemukan = true;
                break;
            }
        }
        if (!ditemukan) {
            System.out.println("Buku tidak ditemukan.");
        }
    }

    // Method untuk menghitung total buku dalam perpustakaan
    public void hitungTotalBuku() {
        System.out.println("Total buku di perpustakaan: " + koleksiBuku.size());
    }

    // Method untuk menghapus buku berdasarkan judul
    public void hapusBuku(String judul) {
        boolean dihapus = false;
        for (int i = 0; i < koleksiBuku.size(); i++) {
            if (koleksiBuku.get(i).judul.equalsIgnoreCase(judul)) {
                koleksiBuku.remove(i);
                System.out.println("Buku berhasil dihapus.");
                dihapus = true;
                break;
            }
        }
        if (!dihapus) {
            System.out.println("Buku tidak ditemukan untuk dihapus.");
        }
    }
}

// Main class untuk menjalankan program
public class zaki_library   {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Perpustakaan perpustakaan = new Perpustakaan();
        boolean running = true;

        while (running) {
            System.out.println("\n=== Sistem Perpustakaan ===");
            System.out.println("1. Tambah Buku");
            System.out.println("2. Tampilkan Semua Buku");
            System.out.println("3. Cari Buku");
            System.out.println("4. Hapus Buku");
            System.out.println("5. Hitung Total Buku");
            System.out.println("6. Keluar");
            System.out.print("Pilih menu: ");
            int pilihan = scanner.nextInt();
            scanner.nextLine(); // Membaca newline yang tersisa

            switch (pilihan) {
                case 1:
                    System.out.print("Masukkan Judul Buku: ");
                    String judul = scanner.nextLine();
                    System.out.print("Masukkan Penulis Buku: ");
                    String penulis = scanner.nextLine();
                    System.out.print("Masukkan Tahun Terbit: ");
                    int tahunTerbit = scanner.nextInt();
                    scanner.nextLine(); // Membersihkan buffer
                    Buku bukuBaru = new Buku(judul, penulis, tahunTerbit);
                    perpustakaan.tambahBuku(bukuBaru);
                    break;
                case 2:
                    perpustakaan.tampilkanSemuaBuku();
                    break;
                case 3:
                    System.out.print("Masukkan judul buku yang dicari: ");
                    String judulCari = scanner.nextLine();
                    perpustakaan.cariBuku(judulCari);
                    break;
                case 4:
                    System.out.print("Masukkan judul buku yang ingin dihapus: ");
                    String judulHapus = scanner.nextLine();
                    perpustakaan.hapusBuku(judulHapus);
                    break;
                case 5:
                    perpustakaan.hitungTotalBuku();
                    break;
                case 6:
                    running = false;
                    System.out.println("Program selesai.");
                    break;
                default:
                    System.out.println("Pilihan tidak valid.");
                    break;
            }
        }
        scanner.close();
    }
}
