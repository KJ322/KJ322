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
    }

    public static void calcHitPoints()
    {
        //TODO
        //input for which die to use (allows for easy integration of homebrew classes)
    }
}