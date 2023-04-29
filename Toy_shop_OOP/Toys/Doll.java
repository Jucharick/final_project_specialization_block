package Toy_shop_OOP.Toys;

public class Doll extends Toy{

    public Doll() {
        super(getCountId(), "Doll", getRandomCalor(), 0.2);
    }
    
    @Override
    public String getName() {
        return "Doll";
    }
}
