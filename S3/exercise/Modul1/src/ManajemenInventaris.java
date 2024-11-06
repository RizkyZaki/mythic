// Don't delete any comments below!!!
// Todo : Import ArrayList and Scanner
import java.util.ArrayList;
import java.util.Scanner;

public class ManajemenInventaris {
    // Todo : Create ArrayList of MakananKering (daftarMakananKering) and MakananBasah (daftarMakananBasah) to store items
    private ArrayList<MakananKering> daftarMakananKering = new ArrayList<>();
    private ArrayList<MakananBasah> daftarMakananBasah = new ArrayList<>();
    private Scanner scanner = new Scanner(System.in);

    public void tambahMakananKering() {
        // Todo : Create input for Nama Makanan, Jumlah Makanan, Harga Makanan, and Brand Makanan
        System.out.println("Masukkan Nama Makanan: ");
        String nama = scanner.next();
        System.out.println("Masukkan Jumlah Makanan: ");
        int jumlah = scanner.nextInt();
        System.out.println("Masukkan Harga Makanan: ");
        double harga = scanner.nextDouble();
        System.out.println("Masukkan Brand Makanan: ");
        String brand = scanner.next();

        // Todo : Create a new object for MakananKering
        MakananKering makananKering = new MakananKering(nama, jumlah, harga, brand);
        makananKering.setNama(nama);
        makananKering.setJumlah(jumlah);
        makananKering.setHarga(harga);
        makananKering.setBrand(brand);

        // Menambahkan makanan kering ke dalam daftar
        daftarMakananKering.add(makananKering);

        // Todo : Create Print Notification "Makanan kering berhasil ditambahkan"
        System.out.println("Makanan kering berhasil ditambahkan!");
    }

    public void tambahMakananBasah() {
        // Todo : Create input for Nama Makanan, Jumlah Makanan, Harga Makanan, and Bahan Makanan
        System.out.println("Masukkan Nama Makanan: ");
        String nama = scanner.next();
        System.out.println("Masukkan Jumlah Makanan: ");
        int jumlah = scanner.nextInt();
        System.out.println("Masukkan Harga Makanan: ");
        double harga = scanner.nextDouble();
        System.out.println("Masukkan Bahan Makanan: ");
        String bahan = scanner.next();

        // Todo : Create a new object for MakananBasah
        MakananBasah makananBasah = new MakananBasah(nama, jumlah, harga, bahan);
        makananBasah.setNama(nama);
        makananBasah.setJumlah(jumlah);
        makananBasah.setHarga(harga);
        makananBasah.setBahan(bahan);

        // Menambahkan makanan basah ke dalam daftar
        daftarMakananBasah.add(makananBasah);

        // Todo : Create Print Notification "Makanan Basah berhasil ditambahkan"
        System.out.println("Makanan basah berhasil ditambahkan!");
    }

    public void tampilkanSemuaMakanan() {
        // Todo : Check if both lists are empty and print "Tidak ada makanan disini" if true
        if (daftarMakananKering.isEmpty() && daftarMakananBasah.isEmpty()) {
            System.out.println("Tidak ada makanan disini");
        } else {
            // Todo : Create print notification for Makanan Kering
            if (!daftarMakananKering.isEmpty()) {
                System.out.println("Daftar Makanan Kering:");
                for (MakananKering mk : daftarMakananKering) {
                    mk.tampilkanData(); // menampilkan detail makanan kering
                }
            }

            // Todo : Create print notification for Makanan Basah
            if (!daftarMakananBasah.isEmpty()) {
                System.out.println("Daftar Makanan Basah:");
                for (MakananBasah mb : daftarMakananBasah) {
                    mb.tampilkanData(); // menampilkan detail makanan basah
                }
            }
        }
    }
}
