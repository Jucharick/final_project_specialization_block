package Toy_shop_OOP.Toys;

public class Lego extends Toy{

    public Lego(double rate) {
        super(getCountId(), "Lego", getRandomCalor(), rate);
    }

    @Override
    public String getName() {
        return "Lego";
    }
}
