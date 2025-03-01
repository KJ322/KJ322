//This program determines the modifier for an ability score

import java.util.Scanner;

public class skillMod
{
    public static void main(String[] args)
    {
        //declaring variables
        int abilityScore = 0;

        //calling methods
        intro();
        abilityScore = getScore();
        modCalculation(abilityScore);
    } 

    public static void intro()
    {
        System.out.println("Welcome, player!");
        System.out.println("This program will help you determine your ability modifier.");
        System.out.println("Just enter your ability score and I'll do the rest!");
    }

    public static int getScore()
    {
        Scanner in = new Scanner(System.in);
        int abilityScore;

        System.out.println("What is your ability score? ");
        abilityScore = in.nextInt();

        if (abilityScore < 1 || abilityScore > 30)
        {
            System.out.println("That's an invalid ability score! Try again.");
            getScore();
        }

        return abilityScore;
    }

    public static void modCalculation (int abilityScore)
    {
        //switch case written with Claude
        // Using switch with ranges (Java 14+)
        /*Switch case only works in Java 14 onward
        switch (abilityScore) 
        {
            case 1:
                System.out.println("Your ability modifer is -5");
            case 2, 3:
                System.out.println("Your ability modifer is -4");
            case 4, 5:
                System.out.println("Your ability modifer is -3");
            case 6, 7:
                System.out.println("Your ability modifer is -2");
            case 8, 9:
                System.out.println("Your ability modifer is -1");
            case 10, 11:
                System.out.println("Your ability modifer is 0");
            case 12, 13:
                System.out.println("Your ability modifer is 1");
            case 14, 15:
                System.out.println("Your ability modifer is 2");
            case 16, 17:
                System.out.println("Your ability modifer is 3");
            case 18, 19:
                System.out.println("Your ability modifer is 4");
            case 20, 21:
                System.out.println("Your ability modifer is 5");
            case 22, 23:
                System.out.println("Your ability modifer is 6");
            case 24, 25:
                System.out.println("Your ability modifer is 7");
            case 26, 27:
                System.out.println("Your ability modifer is 8");
            case 28, 29:
                System.out.println("Your ability modifer is 9");
            case 30:
                System.out.println("Your ability modifer is 10");
            default:
                System.out.println("Your ability modifer is 0"); // Should never reach here given range checks
        }*/
                
        if (abilityScore == 1) 
        {
            System.out.println("Your ability modifer is -5");
            goAgain();
        } 
        else if (abilityScore >= 2 && abilityScore <= 3) 
        {
            System.out.println("Your ability modifer is -4");
            goAgain();
        } 
        else if (abilityScore >= 4 && abilityScore <= 5) 
        {
            System.out.println("Your ability modifer is -3");
            goAgain();
        } 
        else if (abilityScore >= 6 && abilityScore <= 7) 
        {
            System.out.println("Your ability modifer is -2");
            goAgain();
        } 
        else if (abilityScore >= 8 && abilityScore <= 9) 
        {
            System.out.println("Your ability modifer is -1");
            goAgain();
        } 
        else if (abilityScore >= 10 && abilityScore <= 11) 
        {
            System.out.println("Your ability modifer is 0");
            goAgain();
        } 
        else if (abilityScore >= 12 && abilityScore <= 13) 
        {
            System.out.println("Your ability modifer is 1");
            goAgain();
        } 
        else if (abilityScore >= 14 && abilityScore <= 15) 
        {
            System.out.println("Your ability modifer is 2");
            goAgain();
        } 
        else if (abilityScore >= 16 && abilityScore <= 17) 
        {
            System.out.println("Your ability modifer is 3");
            goAgain();
        } 
        else if (abilityScore >= 18 && abilityScore <= 19) 
        {
            System.out.println("Your ability modifer is 4");
            goAgain();
        } 
        else if (abilityScore >= 20 && abilityScore <= 21) 
        {
            System.out.println("Your ability modifer is 5");
            goAgain();
        } 
        else if (abilityScore >= 22 && abilityScore <= 23) 
        {
            System.out.println("Your ability modifer is 6");
            goAgain();
        } 
        else if (abilityScore >= 24 && abilityScore <= 25) 
        {
            System.out.println("Your ability modifer is 7");
            goAgain();
        } 
        else if (abilityScore >= 26 && abilityScore <= 27) 
        {
            System.out.println("Your ability modifer is 8");
            goAgain();
        } 
        else if (abilityScore >= 28 && abilityScore <= 29) 
        {
            System.out.println("Your ability modifer is 9");
            goAgain();
        } 
        else if (abilityScore == 30) 
        {
            System.out.println("Your ability modifer is 10");
            goAgain();
        } 
        else {
            // Should never reach here with our test range
            System.out.println("Your ability modifer is 0");
        }
    }

    public static void goAgain()
    {
        int abilityScore;
        Scanner in = new Scanner(System.in);
        String answer;

        System.out.println("Would you like to calculate another ability modifier? (yes or no)");
        answer = in.nextLine();

        if (answer.equalsIgnoreCase("yes") || answer.equalsIgnoreCase("y"))
        {
            abilityScore = getScore();
            modCalculation(abilityScore);
        }
        else if (answer.equalsIgnoreCase("no") || answer.equalsIgnoreCase("n"))
        {
            System.out.println("Goodbye!");
        }
        else
        {
            System.out.println("Invalid input. Please try again.");
            goAgain();
        }
    }
}