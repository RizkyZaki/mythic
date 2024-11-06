package com.lgcns.mission.book;

public class SecondBook extends Book {
    private String seller;
    private double discountRate;

    public SecondBook(String title, String author, double price, int stockQuantity, String seller, double discountRate) {
        super(title, author, price, stockQuantity);
        this.seller = seller;
        this.discountRate = discountRate;
    }

    public double getDiscountedPrice() {
        return getPrice() * (1 - discountRate);
    }

    @Override
    public String toString() {
        return String.format("SecondBook [Title: %s, Author: %s, Price (Discounted): %s, Seller: %s, Stock: %d]",
                             getTitle(), getAuthor(), MissionUtil.moneyFormat(getDiscountedPrice()), seller, getStockQuantity());
    }
}
