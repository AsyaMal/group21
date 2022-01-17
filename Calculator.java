package itacademy_qa;

import tests.Calc;

import java.util.Scanner;

public class Calculator {

    double num1;
    double num2;
    double result;
    char action;

    public double add(double num1, double num2) {
        result = num1 + num2;
        return result;
    }

    public double subtract(double num1, double num2) {
        result = num1 - num2;
        return result;
    }

    public double multiply(double num1, double num2) {
        result = num1 * num2;
        return result;
    }

    public double divide(double num1, double num2) {
        if (num2 == 0) {
            System.out.println("Division by zero is not possible, please change the divisor");
            return 0;
        } else {
            result = num1 / num2;
            return result;
        }
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter two numbers: ");
        Calculator calc = new Calculator();
        calc.num1 = scan.nextDouble();
        calc.num2 = scan.nextDouble();
        System.out.println("Enter an operator (+, -, *, /): ");
        calc.action = scan.next().charAt(0);
        switch (calc.action) {
            case '+':
                calc.add(calc.num1, calc.num2);
                break;
            case '-':
                calc.subtract(calc.num1, calc.num2);
                break;
            case '*':
                calc.multiply(calc.num1, calc.num2);
                break;
            case '/':
                calc.divide(calc.num1, calc.num2);
                break;
            default:
                System.out.println("Error! Please enter a correct operator");
                return;
        }
        System.out.println("The result:");
        System.out.println(calc.num1 + " " + calc.action + " " + calc.num2 + " = " + calc.result);
    }
}


