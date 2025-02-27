//This program determines the modifier for an ability score

import java.util.Scanner;

public class skillMod
{
    public static void main(String[] args)
    {
        //declaring variables
        Scanner in = new Scanner(System.in);
        int abilityScore;

        //calling methods
        intro();
        getScore();
    } 

    public static void intro()
    {
        System.out.println("Welcome, player!");
        System.out.println("This program will help you determine your ability modifier.");
        System.out.println("Just enter your ability score and I'll do the rest!")
    }

    public static void getScore(Scanner in, int abilityScore)
    {
        System.out.println("What is your ability score? ");
        abilityScore = in.nextInt();

        if (abilityScore < 1 || abilityScore > 30)
        {
            System.out.println("That's an invalid ability score! Try again.")
            getScore(in, abilityScore);
        }
    }

    public static void modCalculation (int abilityScore)
    {
        //switch case written with Claude
        // Using switch with ranges (Java 14+)
        switch (abilityScore) {
            case 1:
                return -5;
            case 2, 3:
                return -4;
            case 4, 5:
                return -3;
            case 6, 7:
                return -2;
            case 8, 9:
                return -1;
            case 10, 11:
                return 0;
            case 12, 13:
                return 1;
            case 14, 15:
                return 2;
            case 16, 17:
                return 3;
            case 18, 19:
                return 4;
            case 20, 21:
                return 5;
            case 22, 23:
                return 6;
            case 24, 25:
                return 7;
            case 26, 27:
                return 8;
            case 28, 29:
                return 9;
            case 30:
                return 10;
            default:
                return 0; // Should never reach here given range checks
    }
}