package Toy_shop_OOP;

import Toy_shop_OOP.Toys.*;
import java.util.ArrayList;
import java.util.Random;

public class Program {

    public static final int SIZE = 10;

    public static void main(String[] args) {
        
        init();
                
    }

    private static void init() {
        ArrayList<Toy> shopFirst = new ArrayList<>();
        ArrayList<Toy> shopSecond = new ArrayList<>();
        ArrayList<Toy> shopThird = new ArrayList<>();

        for (int i = 1; i < SIZE + 1; i++) {
            switch (new Random().nextInt(3)) {
                case 0:
                    shopFirst.add(new Doll());
                    break;
                case 1:
                    shopFirst.add(new Lego());
                    break;
                case 2:
                    shopFirst.add(new Robot());
                    break;
            }

            switch (new Random().nextInt(3)) {
                case 0:
                    shopSecond.add(new Doll());
                    break;
                case 1:
                    shopSecond.add(new Lego());
                    break;
                case 2:
                    shopSecond.add(new Robot());
                    break;
            }

            switch (new Random().nextInt(3)) {
                case 0:
                    shopThird.add(new Doll());
                    break;
                case 1:
                    shopThird.add(new Lego());
                    break;
                case 2:
                    shopThird.add(new Robot());
                    break;
            }
        }

        System.out.println("Shop First");
            for (Toy T: shopFirst) {
                T.getInfo();
        }
        System.out.println("Shop Second");
            for (Toy T: shopSecond) {
                T.getInfo();
        }
        System.out.println("Shop Third");
            for (Toy T: shopThird) {
                T.getInfo();
        }
    }
}
