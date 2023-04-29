package Toy_shop_OOP.Toys;

public class Lego extends Toy{

    public Lego() {
        super(getCountId(), "Lego", getRandomCalor(), 0.3);
    }

    @Override
    public String getName() {
        return "Lego";
    }
}
