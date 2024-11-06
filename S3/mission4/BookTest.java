package com.lgcns.mission.book;

public class BookTest {
    public static void main(String[] args) {
        Book[] books = {
            new Book("Java Basics", "Author A", 150000, 10),
            new SecondBook("Advanced Java", "Author B", 200000, 5, "Seller X", 0.1)
        };

        Customer[] customers = {
            new Customer("John Doe"),
            new Customer("Jane Smith")
        };

        // Cetak daftar buku awal
        System.out.println("Initial Book List:");
        for (Book book : books) {
            System.out.println(book);
        }

        // Transaksi pembelian
        System.out.println("\nTransactions:");
        customers[0].buyBook(books[0]);
        customers[1].buyBook((SecondBook) books[1]);

        // Cetak ulang daftar buku setelah transaksi
        System.out.println("\nUpdated Book List:");
        for (Book book : books) {
            System.out.println(book);
        }

        // Cetak daftar pelanggan beserta total transaksi mereka
        System.out.println("\nCustomer Purchases:");
        for (Customer customer : customers) {
            System.out.println(customer);
        }
    }
}
