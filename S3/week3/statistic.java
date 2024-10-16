public class statistic{

    public static void main(String[] args) {
        // Deklarasi variabel dengan tipe data yang sesuai
        double peluangLotre = 0.0000001235;
        long jarakMatahariKeBumi = 150000000;
        double kemungkinanMenangLotre = 1.235E-7;
        long jumlahOrangDiDunia = 6973738433L;

        // Output hasil
        System.out.println("Peluang memenangkan lotre: " + peluangLotre);
        System.out.println("Jarak matahari ke bumi: " + jarakMatahariKeBumi);
        System.out.println("Kemungkinan memenangkan lotre: " + kemungkinanMenangLotre);
        System.out.println("Jumlah orang di dunia: " + jumlahOrangDiDunia);

        // Memeriksa apakah data sudah benar
        boolean isDataBenar = true;
        System.out.println("Apakah data di atas sudah benar? : " + isDataBenar);
    }
}