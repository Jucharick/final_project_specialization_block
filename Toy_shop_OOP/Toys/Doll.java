package Toy_shop_OOP.Toys;

public class Doll extends Toy{

    public Doll(int id, String name, String color, float rate) {
        super(id, name, color, rate);
    }
    
    @Override
    public String getName() {
        return "Doll";
    }
}
