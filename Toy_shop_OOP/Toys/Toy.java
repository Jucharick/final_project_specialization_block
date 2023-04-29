package Toy_shop_OOP.Toys;

public abstract class Toy implements Toyinterface{
    protected int id; // protected видно только в пакете Toys
    protected String name;
    protected String color;
    protected float rate;

    public Toy(int id, String name, String color, float rate) {
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

    public float getRate() {
        return rate;
    }

    @Override 
    public void step() {
        System.out.println("Шаг");
    }

    @Override
    public void getInfo() {
        System.out.printf("ID: %d  Name: %s  Color: %s Rate: %f  \n",
                          this.id, this.name, this.color, this.rate);
    }
}