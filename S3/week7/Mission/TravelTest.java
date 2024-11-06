

import java.util.Scanner;

public class TravelTest {
    public static void main(String[] args) {
        Travel[] travels = {
            new Travel("TRV001", "Munchen", "GermanAirways", Travel.INDIVIDUAL, 10),
            new Travel("TRV002", "Prague", "AirFrance", Travel.INDIVIDUAL, 20),
            new Travel("TRV003", "LA", "DeltaAirlines", Travel.PACKAGE, 12),
            new Travel("TRV004", "Osaka", "KoreanAir", Travel.INDIVIDUAL, 15),
            new Travel("TRV005", "Shanghai", "ChinaSouthern", Travel.PACKAGE, 10)
        };

        Scanner scanner = new Scanner(System.in);
        while (true) {
            printMenu();
            int choice = scanner.nextInt();

            switch (choice) {
                case 1 -> printAllPackages(travels);
                case 2 -> searchIndividual(travels);
                case 3 -> searchPackage(travels);
                case 4 -> updateMaxPeople(travels, scanner);
                case 5 -> updateResvPeople(travels, scanner);
                case 9 -> {
                    System.out.println("Keluar!!");
                    scanner.close();
                    return;
                }
                default -> System.out.println("Silahkan masukkan ulang!!");
            }
        }
    }

    private static void printMenu() {
        System.out.println("======= < Menu > =======");
        System.out.println("1. Lihat semua paket perjalanan");
        System.out.println("2. Pencarian paket individu");
        System.out.println("3. Pencarian paket perjalanan");
        System.out.println("4. Perubahan jumlah maksimal peserta");
        System.out.println("5. Perubahan jumlah peserta dalam reservasi");
        System.out.println("9. Keluar");
        System.out.println("========================");
        System.out.print("Pilih Menu: ");
    }

    private static void printAllPackages(Travel[] travels) {
        printHeader();
        for (Travel travel : travels) {
            travel.printTravelInfo();
        }
        printSeparator();
    }

    private static void searchIndividual(Travel[] travels) {
        printHeader();
        for (Travel travel : travels) {
            if (travel.getTravelType() == Travel.INDIVIDUAL) {
                travel.printTravelInfo();
            }
        }
        printSeparator();
    }

    private static void searchPackage(Travel[] travels) {
        printHeader();
        for (Travel travel : travels) {
            if (travel.getTravelType() == Travel.PACKAGE) {
                travel.printTravelInfo();
            }
        }
        printSeparator();
    }

    private static void updateMaxPeople(Travel[] travels, Scanner scanner) {
        System.out.print(">> Masukkan code travel: ");
        String code = scanner.next();
        System.out.print(">> Masukkan jumlah maksimum orang dalam reservasi untuk diubah: ");
        int maxPeople = scanner.nextInt();

        if (maxPeople < 0) {
            System.out.println("[Error] Jumlah maksimal peserta tidak boleh lebih kecil dari 0.");
            return;
        }

        boolean found = false;
        for (Travel travel : travels) {
            if (travel.getTravelCode().equalsIgnoreCase(code)) {
                travel.setMaxPeople(maxPeople);
                found = true;
                System.out.println(">> Jumlah maksimum orang dalam reservasi sudah diubah menjadi " + maxPeople + " orang.");
                break;
            }
        }

        if (!found) {
            System.out.println("[Error] Tidak ditemukan paket yang cocok dengan code travel [" + code + "].");
        }
    }

    private static void updateResvPeople(Travel[] travels, Scanner scanner) {
        System.out.print(">> Masukkan code travel: ");
        String code = scanner.next();
        System.out.print(">> Masukkan jumlah peserta dalam reservasi untuk diubah: ");
        int resvPeople = scanner.nextInt();

        if (resvPeople < 0) {
            System.out.println("[Error] Jumlah peserta dalam reservasi tidak boleh lebih kecil dari 0.");
            return;
        }

        boolean found = false;
        for (Travel travel : travels) {
            if (travel.getTravelCode().equalsIgnoreCase(code)) {
                travel.setResvPeople(resvPeople);
                found = true;
                System.out.println(">> Jumlah peserta dalam reservasi sudah diubah menjadi " + resvPeople + " orang.");
                break;
            }
        }

        if (!found) {
            System.out.println("[Error] Tidak ditemukan paket yang cocok dengan code travel [" + code + "].");
        }
    }

    private static void printHeader() {
        System.out.printf("%-12s %-12s %-15s %-10s %-15s %-15s %-10s%n", "Code Travel", "Nama Kota", "Airline", "Jenis Paket", "Jml Peserta max", "Jml Peserta saat ini", "Status");
        System.out.println("---------------------------------------------------------------------------------------------------------");
    }

    private static void printSeparator() {
        System.out.println("---------------------------------------------------------------------------------------------------------");
  }
}