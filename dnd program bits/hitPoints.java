import java.util.Scanner;

public class hitPoints 
{

    public static void main(String[] args) 
    {
        
    }

    public static void intro()
    {
        //declaring variables
        Scanner in = new Scanner(System.in);
        final int CLASS_LIST = 1, CALC = 2;

        //introduce program and get user input
        System.out.print("Let's calculate your hit points!\n");
        System.out.print("Press 1 to look at a list of hit dice for base game classes\n");
        System.out.print("Press 2 to calculate your hit points\n")
        System.out.print("Enter 1 or 2: ");
        int userInput = in.nextInt();

        //decision structure for next function
        if (userInput == CLASS_LIST)
        {
            classList();
        }
        else if (userInput ==  CALC)
        {
            calcHitPoints();
        }
        else 
        {
            System.out.print("That is not a valid input! Try again!");

        }
    }

    public static void classList()
    {
        //TODO
        //help menu with hit dice for each base game class
        System.out.println("Barbarian Hit Die: d12");
        System.out.println("Bard Hit Die: d8");
        System.out.println("Cleric Hit Die: d8");
        System.out.println("Druid Hit Die: d8");
        System.out.println("Fighter Hit Die: d10");
        System.out.println("Monk Hit Die: d8");
        System.out.println("Paladin Hit Die: d10");
        System.out.println("Ranger Hit Die: d10");
        System.out.println("Rogue Hit Die: d8");
        System.out.println("Sorcerer Hit Die: d6");
        System.out.println("Warlock Hit Die: d8");
        System.out.println("Wizard Hit Die: d6");
        System.out.println("Artificer Hit Die: d8");
    }

    public static void calcHitPoints()
    {
        //TODO
        //input for which die to use (allows for easy integration of homebrew classes)
        //math is max roll + con mod
        System.out.println("What die do you want to roll? (ex. 20) ");
        int sidesOfDice = in.nextInt();
        System.out.println();

        switch (sidesOfDice)
        {
            case "d12":
                d12();
                break;
            case "d10":
                d10();
                break;
            case "d8":
                d8();
                break;
            case "d6":
                d6();
                break;
            default:
                System.out.println("Invalid input. Please try again.");
                getDice();
        }

    }

    public static void d12 ()
    {
        final int SIDES = 12;
        
        

        System.out.println ("Your HP is " + rollTotal);
    }
}