package Toy_shop_OOP.Toys;

public class Robot extends Toy{

    public Robot() {
        super(getCountId(), "Robot", getRandomCalor(), 0.5);
    }
    
    @Override
    public String getName() {
        return "Robot";
    }
}
