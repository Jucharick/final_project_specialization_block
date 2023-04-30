package Toy_shop_OOP.Toys;

public class Doll extends Toy{

    public Doll(double rate) {
        super(getCountId(), "Doll", getRandomCalor(), rate);
    }
    
    @Override
    public String getName() {
        return "Doll";
    }
}
