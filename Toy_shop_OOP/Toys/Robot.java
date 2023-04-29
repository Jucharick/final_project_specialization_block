package Toy_shop_OOP.Toys;

public class Robot extends Toy{

    public Robot(int id, String name, String color, float rate) {
        super(id, name, color, rate);
    }
    
    @Override
    public String getName() {
        return "Robot";
    }
}
