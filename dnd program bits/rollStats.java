//import java.util.Arrays;
//import java.util.Collections;

public class rollStats 
{
    /*
     * rolls stats for char sheets
     * need an intro, roll function, way for players to assign stats
     */
    public static void main(String[] args) 
    {
        intro();

        for (int i = 0; i < 6; i++)
        {
            int statRolls[] = rolls();
        }

    }

    public static void intro()
    {
        System.out.println("Hello! Let's roll up your character's stats!");
        System.out.println("This program will roll your stats, and then you'll be able to assign them.");
        System.out.println("Let's get started!");
    }

    public static int[] rolls()
    {
            int roll1 = (int)(Math.random() * 6) + 1;
            int roll2 = (int)(Math.random() * 6) + 1;
            int roll3 = (int)(Math.random() * 6) + 1;
            int roll4 = (int)(Math.random() * 6) + 1;

            int rolls[] = {roll1, roll2, roll3, roll4};
            int lowestRoll = 7;

            for (int j = 0; j < rolls.length; j++)
            {
                if (lowestRoll > rolls[j])
                {
                    lowestRoll = rolls[j];
                }
            }

            int rollTotal = roll1 + roll2 + roll3 + roll4 - lowestRoll;

            System.out.println(roll1 + " + " + roll2 + " + " + roll3 + " + " + roll4 + " - " + lowestRoll + " = " + rollTotal);
    }

    public static void assignStats()
    {
        
    }
}
