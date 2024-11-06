// Don't delete any comments below!!!
// Todo: Import Scanner
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Todo : Create ManajemenInventaris Object and Scanner
        ManajemenInventaris manajemenInventaris = new ManajemenInventaris();
        Scanner scanner = new Scanner(System.in);
        
        // Todo : Create Loop list menu
        int pilihan = 0;
        while (pilihan != 4) { // Selama pilihan tidak sama dengan 4 (Keluar)
            // Menampilkan menu
            System.out.println("\n===== Menu Manajemen Inventaris =====");
            System.out.println("1. Tambah Makanan Kering");
            System.out.println("2. Tambah Makanan Basah");
            System.out.println("3. Tampilkan Semua Makanan");
            System.out.println("4. Keluar");
            System.out.print("Pilih menu: ");
            pilihan = scanner.nextInt();
            
            // Proses pilihan menu
            switch (pilihan) {
                case 1:
                    manajemenInventaris.tambahMakananKering();
                    break;
                case 2:
                    manajemenInventaris.tambahMakananBasah();
                    break;
                case 3:
                    manajemenInventaris.tampilkanSemuaMakanan();
                    break;
                case 4:
                    System.out.println("Keluar dari program...");
                    break;
                default:
                    System.out.println("Pilihan tidak valid! Silakan pilih lagi.");
                    break;
            }
        }
        
        scanner.close(); // Menutup scanner
    }
}
