package com.lgcns.mission.book;

public class Book {
    private String title;
    private String author;
    private double price;
    private int stockQuantity;

    public Book(String title, String author, double price, int stockQuantity) {
        this.title = title;
        this.author = author;
        this.price = price;
        this.stockQuantity = stockQuantity;
    }

    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public double getPrice() { return price; }
    public int getStockQuantity() { return stockQuantity; }

    public void setStockQuantity(int stockQuantity) { this.stockQuantity = stockQuantity; }

    @Override
    public String toString() {
        return String.format("Book [Title: %s, Author: %s, Price: %s, Stock: %d]", 
                             title, author, MissionUtil.moneyFormat(price), stockQuantity);
    }
}
