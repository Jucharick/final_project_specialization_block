package Toy_shop_OOP.Toys;

public class Lego extends Toy{

    public Lego(int id, String name, String color, float rate) {
        super(id, name, color, rate);
    }

    @Override
    public String getName() {
        return "Lego";
    }
}
