import java.util.Scanner;

public class zaki_rectangle {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan panjang persegi panjang: ");
        double panjang = scanner.nextDouble();

        System.out.print("Masukkan lebar persegi panjang: ");
        double lebar = scanner.nextDouble();

        double luas = panjang * lebar;

        System.out.println("Luas persegi panjang adalah: " + luas);
    }
}
