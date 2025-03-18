import java.util.Arrays;
import java.util.Collections;

public class rollStats 
{
    /*
     * rolls stats for char sheets
     * need an intro, roll function, way for players to assign stats
     */
    public static void main(String[] args) 
    {
        for (int i = 0; i < 6; i++)
        {
            int roll1 = (int)(Math.random() * 6) + 1;
            int roll2 = (int)(Math.random() * 6) + 1;
            int roll3 = (int)(Math.random() * 6) + 1;
            int roll4 = (int)(Math.random() * 6) + 1;

            int rolls[] = {roll1, roll2, roll3, roll4};
            //int lowest_roll = Collections.min(Arrays.asList(rolls));
            //int lowestRoll = 0;
            //rollTotal -= lowestRoll;
            int lowestRoll = 1;

            for (int j = 0; j < rolls.length; j++)
            {
                if (lowestRoll > rolls[j])
                {
                    lowestRoll = rolls[j];
                }
            }

            System.out.println(lowestRoll);

            int rollTotal = roll1 + roll2 + roll3 + roll4 - lowestRoll;

            System.out.println(roll1 + " + " + roll2 + " + " + roll3 + " + " + roll4 + " - " + lowestRoll + " = " + rollTotal);
        }
    }

    public static void intro()
    {
        System.out.println("Hello! Let's roll up your character's stats!");
        System.out.println("This program will roll your stats, and then you'll be able to assign them.");
    }

    public static void rolls()
    {
        for (int i = 0; i < 6; i++)
        {
            int roll1 = (int)(Math.random() * 6) + 1;
            int roll2 = (int)(Math.random() * 6) + 1;
            int roll3 = (int)(Math.random() * 6) + 1;
            int roll4 = (int)(Math.random() * 6) + 1;

            int rollTotal = (roll1 + roll2 + roll3 + roll4); // - //TODO subtract lowest die;
            int[] rolls = {roll1, roll2, roll3, roll4};
            //int lowest_roll = Collections.min(Arrays.asList(rolls));
            int lowest_roll = 0;
            rollTotal -= lowest_roll;

            System.out.println(rollTotal);
        }
    }
}
