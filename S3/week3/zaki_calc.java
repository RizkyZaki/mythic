import java.util.Scanner;

class Student {
    private final String name;
    private final String nim;
    private double scoreTubes, scoreQuiz, scoreTugas, scoreUTS, scoreUAS;

    public Student(String name, String nim) {
        this.name = name;
        this.nim = nim;
    }

    public void inputScore() {
        Scanner input = new Scanner(System.in);
        System.out.print("Masukkan nilai Tubes: ");
        scoreTubes = input.nextDouble();
        System.out.print("Masukkan nilai Quiz: ");
        scoreQuiz = input.nextDouble();
        System.out.print("Masukkan nilai Tugas: ");
        scoreTugas = input.nextDouble();
        System.out.print("Masukkan nilai UTS: ");
        scoreUTS = input.nextDouble();
        System.out.print("Masukkan nilai UAS: ");
        scoreUAS = input.nextDouble();
    }

    public double calculateScore() {
        return (0.30 * scoreTubes) + (0.10 * scoreQuiz) + (0.10 * scoreTugas) +
                (0.25 * scoreUTS) + (0.25 * scoreUAS);
    }

    public void displayResult() {
        System.out.println("\nNama  : " + name);
        System.out.println("NIM   : " + nim);
        System.out.printf("Nilai Matakuliah Pemrograman Berorientasi Objek: %.2f\n", calculateScore());
    }
}

public class zaki_calc {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Masukkan Nama: ");
        String name = input.nextLine();
        System.out.print("Masukkan NIM: ");
        String nim = input.nextLine();

        Student student = new Student(name, nim);

        student.inputScore();

        student.displayResult();
    }
}
