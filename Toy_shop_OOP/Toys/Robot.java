package Toy_shop_OOP.Toys;

public class Robot extends Toy{

    public Robot(double rate) {
        super(getCountId(), "Robot", getRandomCalor(), rate);
    }
    
    @Override
    public String getName() {
        return "Robot";
    }
}
