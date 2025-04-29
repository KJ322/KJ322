import java.util.Scanner;
import java.io.IOException;
import java.io.FileWriter;

public class dndToolbag 
{    
    public static void main(String[] args)
    {
        Scanner k = new Scanner (System.in);
        final int PLAY = 1;
        final int CREATE = 2;


        System.out.println("Welcome to the D&D Toolbag!\n\nDo you want to play or create a character?");
        System.out.println("1. Play\n2. Character Creation");
        System.out.print("Choose: ");
        int userMode = k.nextInt();


        if (userMode == PLAY)
        {
            //TODO
            playMode(k);
        }
        else if (userMode == CREATE)
        {
            //TODO
            charCreation(k);
        }
        else
        {
            System.out.println("Invalid input.");
            System.out.println("1. Play\n2. Character Creation");
            userMode = k.nextInt();
        }
    }


    public static void playMode(Scanner k)
    {
        final int ROLL = 1;
        final int INVENTORY = 2;
        final int CHAR_SHEET = 3;
        final int TRACKER = 4;
        final int COMBAT = 5;


        System.out.print("You are in play mode.\nYou can:\n");
        System.out.println("1. Roll");
        System.out.println("2. Keep track of inventory");
        System.out.println("3. Check your character sheet");
        System.out.println("4. Track inspiration, hp, and xp");
        System.out.println("5. Enter combat");
        System.out.print("Chose an option: ");
        int choice = k.nextInt();


        if (choice == ROLL)
        {
            diceRoller.main(null);
        }
        else if (choice == INVENTORY)
        {
            //TODO
            System.out.print("Call track inventory java file");
        }
        else if (choice == CHAR_SHEET)
        {
            //TODO
            System.out.print("Call character sheet java file");
        }
        else if (choice == TRACKER)
        {
            //TODO
            System.out.print("Call insp/hp/xp tracker");
        }
        else if (choice == COMBAT)
        {
            //TODO
            combatMode(k);
        }
        else
        {
            System.out.println("Invalid input.");
            playMode(k);
        }
    }


    public static void charCreation(Scanner k)
    {
        final int ROLL_STATS = 1;
        final int CALC_HP = 2;
        final int INVENTORY = 3;
        final int NOTES = 4;


        System.out.print("You are in character creation mode.\nYou can:\n");
        System.out.println("1. Roll stats");
        System.out.println("2. Calculate HP");
        System.out.println("3. Start your inventory");
        System.out.println("4. Make notes");
        System.out.print("Chose an option: ");
        int choice = k.nextInt();

        try (FileWriter writer = new FileWriter("charCreation.txt", true)) {
            writer.write("User chose: " + choice + "\n");
    
            switch (choice) {
                case ROLL_STATS:
                    rollStats.main(null); // Call the main method of rollStats.java
                    charCreation(k);
                case CALC_HP:
                    hitPoints.main(null); // Call the main method of hitPoints.java
                    charCreation(k);
                case INVENTORY:
                    System.out.println("Call inventory java file");
                    //inventory.main(null); // Call the main method of inventory.java
                    break;
                case NOTES:
                    System.out.println("Call notes java file");
                    //notes.main(null); // Call the main method of notes.java
                    break;
                default:
                    System.out.println("Invalid input.");
                    charCreation(k); // Restart the process for invalid input
                    break;
            }
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
    }

    public static void combatMode(Scanner k)
    {
        //TODO
        final int ATTACK = 1;
        final int SPELLS = 2;
        final int TRACK = 3;
        final int FLEE = 4;


        System.out.print("You are in combat mode.\nYou can:\n");
        System.out.println("1. Engage");
        System.out.println("2. Cast spells");
        System.out.println("3. Track HP and inspiration");
        System.out.println("4. Flee (exit)");
        System.out.print("Chose an option: ");
        int choice = k.nextInt();

        if (choice == ATTACK)
        {
            rollToAttack.main(null);
        }
        else if (choice == SPELLS)
        {
            //TODO
            System.out.print("Call spell tracker java file");
        }
        else if (choice == TRACK)
        {
            //TODO
            System.out.print("Call insp/hp/xp tracker");
        }
        else if (choice == FLEE)
        {
            System.out.println("You have disengaged from combat.");
            playMode(k);
        }
        else
        {
            System.out.println("Invalid input.");
            combatMode(k);
        }
    }
}