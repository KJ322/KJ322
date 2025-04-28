import java.io.IOException;
import java.util.Scanner;

public class hitPoints 
{

    public static void main(String[] args) 
    {
        intro();

    }

    public static void intro()
    {
        //declaring variables
        Scanner in = new Scanner(System.in);
        final int CLASS_LIST = 1, CALC = 2;

        //introduce program and get user input
        System.out.print("Let's calculate your hit points!\n");
        System.out.print("Press 1 to look at a list of hit dice for base game classes\n");
        System.out.print("Press 2 to calculate your hit points\n");
        System.out.print("Enter 1 or 2: ");
        int userInput = in.nextInt();

        //decision structure for next function
        if (userInput == CLASS_LIST)
        {
            classList();
            calcHitPoints();
        }
        else if (userInput ==  CALC)
        {
            calcHitPoints();
        }
        else 
        {
            System.out.print("That is not a valid input! Try again!");

        }
        in.close();
    }

    public static void classList()
    {
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
        //input for which die to use (allows for easy integration of homebrew classes)
        //math is max roll + con mod
        Scanner in = new Scanner(System.in);
        System.out.println("What die do you want to roll? (ex. 20) ");
        System.out.print("d");
        int sidesOfDice = in.nextInt();
        System.out.println();

        //get the con modifier
        int conMod = getConMod();

        switch (sidesOfDice) 
        {
            case 12:
                System.out.println("Your hit points are: " + (12 + conMod));
                break;
            case 10:
                System.out.println("Your hit points are: " + (10 + conMod));
                break;
            case 8:
                System.out.println("Your hit points are: " + (8 + conMod));
                break;
            case 6:
                System.out.println("Your hit points are: " + (6 + conMod));
                break;
            default:
                System.out.println("Invalid input. Please try again.");
                calcHitPoints();
        }
        in.close();
    }

    public static int getConMod()
    {
        try (Scanner fileScanner = new Scanner(new java.io.File("charCreation.txt")))
        {
            while (fileScanner.hasNextLine()) 
            {
                String line = fileScanner.nextLine();
                if (line.startsWith("CON:")) 
                {
                    // Extract the CON value from the line
                    String[] parts = line.split(":");
                    String conValueString = parts[1].trim().split(" ")[0]; // Get only the numeric part
                    int conValue = Integer.parseInt(conValueString);
                    return (conValue - 10) / 2; // Calculate and return the modifier
                }
            }
        } 
        catch (IOException e) 
        {
            System.out.println("An error occurred while reading the character sheet.");
            e.printStackTrace();
        }
        catch (NumberFormatException e)
        {
            System.out.println("Invalid CON value format in the character sheet.");
            e.printStackTrace();
        }
        return 0; // Default modifier if CON is not found
    }
}