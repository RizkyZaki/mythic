package com.lgcns.mission.book;

public class Customer {
    private String name;
    private double totalPrice;

    public Customer(String name) {
        this.name = name;
        this.totalPrice = 0.0;
    }

    public void buyBook(Book book) {
        if (book.getStockQuantity() > 0) {
            book.setStockQuantity(book.getStockQuantity() - 1);
            totalPrice += book.getPrice();
        }
    }

    public void buyBook(SecondBook book) {
        if (book.getStockQuantity() > 0) {
            book.setStockQuantity(book.getStockQuantity() - 1);
            totalPrice += book.getDiscountedPrice();
        }
    }

    @Override
    public String toString() {
        return String.format("Customer [Name: %s, Total Spent: %s]", name, MissionUtil.moneyFormat(totalPrice));
    }
}
