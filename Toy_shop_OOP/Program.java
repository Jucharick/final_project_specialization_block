package Toy_shop_OOP;

import Toy_shop_OOP.Toys.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.lang.Math;
import java.io.FileWriter;
import java.io.IOException;

public class Program {

    public static int SIZE = 5;
    public static double rateDoll = 0.2;
    public static double rateLego = 0.3;
    public static double rateRobot = 0.5;

    public static ArrayList<Toy> shopToys = new ArrayList<>();
    public static Queue<Toy> playToys = new LinkedList<>();

    public static Toy prizeToy = null;
    
    public static void main(String[] args) {  

        get();

    }

    private static void userView(){
        Scanner reader = new Scanner(System.in);
        System.out.print("Введите количество игрушек: \n");
        SIZE= reader.nextInt();
        
        reader.nextLine();
        System.out.print("Вы хотите изменить частоту выпадения игрушек (y/n)? \n");
        String userAnswer = reader.nextLine().toLowerCase();
        
        if (userAnswer.equals("y") || userAnswer.equals("yes") || userAnswer.equals("Да")) {
            System.out.print("частота для трех игрушек должна равняться 1 \n");
            Double input;
            System.out.print("частота для Doll (от 0 до 1 через запятую): \n");
            try {
                input= reader.nextDouble();
                if (input < 1) {
                    rateDoll = input;
                }
                else {
                    System.out.print("Число должнно быть меньше 1 \n");
                }
            }
            catch (Exception err){
                System.out.print("Некорректное значение \n");
                reader.nextLine();
            }

            System.out.print("частота для Lego (от 0 до 1 через запятую): \n");
            try {
                input= reader.nextDouble();
                if (input < 1 && rateDoll + input <= 1) {
                    rateLego = input;
                }
                else {
                    System.out.print("Число должнно быть меньше 1. Сумма Doll + Lego должна быть равна либо меньше 1 \n");
                }
            }
            catch (Exception err){
                System.out.print("Некорректное значение \n");
                reader.nextLine();
            }

            if (rateDoll + rateLego == 1) {
                rateRobot = 0;
            }
            else {
                System.out.print("частота для Robot (от 0 до 1 через запятую): \n");
                try {
                    input= reader.nextDouble();
                    if (input < 1 && rateDoll + rateLego + input <= 1) {
                        rateRobot = input;
                    }
                    else {
                        System.out.print("Число должнно быть меньше 1. Сумма Doll + Lego + Robot  должна быть равна либо меньше 1 \n");
                        rateRobot = (1 - rateDoll - rateLego);
                        System.out.printf("частота для Robot = %.2f \n", rateRobot);
                    }
                }
                catch (Exception err){
                    System.out.print("Некорректное значение \n");
                    reader.nextLine();
                }
            }
        }
        reader.close();
    }

    private static void getPlayToys() {
        // выпавшие ирушки в зависимости от общего количества и частоты выпадения
        for (int i = 1; i <= Math.round(SIZE * rateDoll); i++) {
            shopToys.add(new Doll(rateDoll));
        }
        for (int i = 1; i <= Math.round(SIZE * rateLego); i++) {
            shopToys.add(new Lego(rateLego));
        }
        for (int i = 1; i <= (SIZE - Math.round(SIZE * rateDoll) - Math.round(SIZE * rateLego)); i++) {
            shopToys.add(new Robot(rateRobot));
        }

        System.out.println("Shop Toys");
        for (Toy T: shopToys) {
            T.getInfo();
        }

    }

    private static void toysGame(){
        Collections.shuffle(shopToys);
        playToys.addAll(shopToys);
  
        for (int i = 1; i < SIZE -1; i++) {
            playToys.poll();
        }
        prizeToy = playToys.peek();
        
        System.out.print("Ваш приз: \n");
        prizeToy.getInfo();
    }

    // запись в файл 
    private static void put() {
        String str;
        str = prizeToy.getStr();
        FileWriter file = null;
        try {
            file = new FileWriter("Toy_shop_OOP/prizeToy.txt", true);
            file.append(str);
        } catch (IOException ex) {
            System.err.println("Ошибка: " + ex);
        } finally {
            if (file != null) {
                try {
                    file.close();
                } catch (IOException ex) {
                    System.err.println("Ошибка: " + ex);
                }
            }
        }
    }

    private static void init() {
        userView();
        getPlayToys();
        toysGame();
        put();
    }

    private static void get() {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Cыграем (y/n)? \n");
        String userAnswer = scanner.nextLine().toLowerCase();
        if (userAnswer.equals("y") || userAnswer.equals("yes") || userAnswer.equals("Да")) {
            init();
        }
        scanner.close();
    }
}
