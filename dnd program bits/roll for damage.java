//import java.util.Random;
import java.util.Scanner;

public class diceRoller 
{
    public static void main(String[] args) 
    {
        //Scanner in = new Scanner(System.in);

        //calling methods
        intro();
        rollAttack();
        //rollAgain();
    }
    
    public static void intro()
    {
        //welcomes player, explains how to use the program
        System.out.println("Welcome to combat!");
        System.out.println("You'll roll for attack and add your modifiers, and a proficiency bonus if applicable.");
        System.out.println();
    }

    public static void rollAttack()
    {
        Scanner in = new Scanner(System.in);

        //gather necessary information from player
        System.out.println("What is your skill modifier? ");
        int modifier = in.nextInt();
        System.out.println();

        System.out.println("What is your proficiency bonus? (enter 0 if not applicable) ");
        int profBonus = in.nextInt();
        System.out.println();

        //rolls d20 for attack
        final int SIDES = 20;
        int roll, i, rollTotal = 0;

        for (i = 0; i < numOfDice; i++)
        {
            roll = (int)(Math.random() * SIDES) + 1;
            System.out.println(roll);
            rollTotal += roll;
        }

        int total = rollTotal + modifier + profBonus;
        System.out.println ("You rolled " + total);
    }

    public static void rollAgain()
    {
        Scanner in = new Scanner(System.in);

        System.out.println("Would you like to roll again? (yes/no) ");
        String answer = in.nextLine();

        if (answer.equalsIgnoreCase("yes") || answer.equalsIgnoreCase("y"))
        {
            System.out.println();
            getDice();
        }
        else if (answer.equalsIgnoreCase("no") || answer.equalsIgnoreCase("n"))
        {
            System.out.println("Thank you for using the dice roller!");
        }
        else
        {
            System.out.println("Invalid input. Please try again.");
            rollAgain();
        }
    }
}