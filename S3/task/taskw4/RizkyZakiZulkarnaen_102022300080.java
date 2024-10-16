package taskw4;

public class RizkyZakiZulkarnaen_102022300080 {

    public static void main(String[] args) {

        // Contoh 1: Hasil Ujian dengan if-else
        System.out.println("Contoh 1: Hasil Ujian dengan if-else");
        int nilai1 = 8;
        int nilai2 = 7;
        int nilai3 = 5;
        float rata_rata = (float) (nilai1 + nilai2 + nilai3) / 3;

        if (rata_rata < 5) {
            System.out.println("Tidak Lulus");
        } else if (rata_rata >= 5 && rata_rata < 6) {
            System.out.println("Harus ikut ujian perbaikan");
        } else {
            System.out.println("Lulus");
        }
        System.out.println("Nilai Rata-rata = " + rata_rata + "\n");

        // Contoh 2: Hasil Ujian dengan switch-case
        System.out.println("Contoh 2: Hasil Ujian dengan switch-case");
        switch ((int) rata_rata) {
            case 0:
            case 1:
            case 2:
            case 3:
            case 4:
                System.out.println("Tidak Lulus");
                break;
            case 5:
                System.out.println("Ikut ujian perbaikan");
                break;
            default:
                System.out.println("Lulus");
                break;
        }
        System.out.println("Nilai Rata-rata = " + rata_rata + "\n");

        // Contoh 3: Penggunaan while loop
        System.out.println("Contoh 3: while loop");
        int num1 = 0;
        int num2 = 23;
        int num3 = num1 + num2;
        while (num3 > num1) {
            num2 -= 3;
            num1 += 2;
            num3 = num1 + num2;
            System.out.println("num1=" + num1 + ", num3=" + num3);
        }
        System.out.println();

        // Contoh 4: while true loop dengan break
        System.out.println("Contoh 4: while true loop dengan break");
        int variable = 20;
        while (true) {
            System.out.println("Nilai variable= " + variable);
            --variable;
            if (variable < 10) {
                break;
            }
        }
        System.out.println();

        // Contoh 5: for loop dengan pengurangan variabel
        System.out.println("Contoh 5: for loop");
        for (variable = 20; variable >= 10; variable--) {
            System.out.println("Nilai variable = " + variable);
        }
        System.out.println();

        // Contoh 6: for loop dengan dua variabel
        System.out.println("Contoh 6: for loop dengan dua variabel");
        for (int variable1 = 20, variable2 = 0; variable1 >= 10 && variable2 <= 5; variable1--, variable2++) {
            System.out.println("Nilai variable1= " + variable1);
            System.out.println("Nilai variable2= " + variable2);
        }
        System.out.println();

        // Contoh 7: for loop tanpa kondisi awal atau akhir
        System.out.println("Contoh 7: for loop tanpa kondisi");
        variable = 20;
        for (; ; ) {
            System.out.println("Nilai variable = " + variable);
            variable--;
            if (variable < 10) break;
        }
        System.out.println();

        // Contoh 8: do-while loop
        System.out.println("Contoh 8: do-while loop");
        variable = 20;
        do {
            System.out.println("Nilai variable = " + variable);
            variable--;
        } while (variable > 20);
        System.out.println();

        // Contoh 9: Nested loop dengan while dan for
        System.out.println("Contoh 9: Nested loop");
        int j = 0;
        for (int i = 0; i < 5; i++) {
            while (j < 5) {
                System.out.print(" @ ");
                j++;
            }
            j = 0;
            System.out.print("\n");
        }
        System.out.println();

        // Contoh 10: Continue statement
        System.out.println("Contoh 10: Continue statement");
        for (int i = 0; i < 10; i++) {
            System.out.print(i + " ");
            if (i % 2 == 0) continue;
            System.out.println(" ");
        }
        System.out.println();

        // Contoh 11: Continue with Label
        System.out.println("Contoh 11: Continue with Label");
        outer:
        for (int i = 0; i < 10; i++) {
            for (int k = 0; k < 10; k++) {
                if (k > i) {
                    System.out.println();
                    continue outer;
                }
                System.out.print(" " + (i * k));
            }
        }
        System.out.println("\n");
    }
}
