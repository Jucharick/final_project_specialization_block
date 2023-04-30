package Toy_shop_OOP.Toys;

import java.util.Random;

public abstract class Toy implements Toyinterface{
    protected int id; // protected видно только в пакете Toys
    protected String name;
    protected String color;
    protected double rate;

    protected static int counter = 0;

    public Toy(int id, String name, String color, double rate) {
        this.id = id;
        this.name = name;
        this.color = color;
        this.rate = rate;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    public double getRate() {
        return rate;
    }

    public void setRate(double rate) {
        this.rate = rate;
    }

    @Override
    public void getInfo() {
        System.out.printf("ID: %d  Name: %s  Color: %s Rate: %f  \n",
                          this.id, this.name, this.color, this.rate);
    }

    public String getStr() {
        return String.format("ID: %d  Name: %s  Color: %s Rate: %f  \n",
                          this.id, this.name, this.color, this.rate);
    }

    public static int getCountId() {
        counter = counter + 1;
        return counter;
    }

    public static String getRandomCalor() {
        Random rnd = new Random();
        int randovValue = rnd.nextInt(5);
        String color;
        switch (randovValue){
            case 1:
                color= "blue";
                break;
            case 2:
                color= "pink";
                break;
            case 3:
                color= "red";
                break;
            case 4:
                color= "yellow";
                break;
            case 5:
                color= "green";
                break;
            default:
                color= "grey";
        }
        return color;
    }
}