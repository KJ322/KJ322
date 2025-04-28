//import java.util.Arrays;
//import java.util.Collections;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class rollStats 
{
    /*
     * rolls stats for char sheets
     * need an intro, roll function, way for players to assign stats
     */
    public static void main(String[] args) 
    {
        int[] rolledStats = new int[6]; // Array to store the total rolled values
    
        intro();
    
        try (FileWriter writer = new FileWriter("charCreation.txt", true)) 
        {
            for (int i = 0; i < 6; i++) 
            {
                int[] rollsResult = rolls(writer); // Get the full rolls array
                int rollTotal = rollsResult[0] + rollsResult[1] + rollsResult[2] + rollsResult[3] - Math.min(Math.min(rollsResult[0], rollsResult[1]), Math.min(rollsResult[2], rollsResult[3]));
                rolledStats[i] = rollTotal; // Store the total rolled value
            }

            //allows the user to re-roll stats below 7 if they want
            rolledStats = rerollLowStats(rolledStats, writer);

            // Assign stats and calculate modifiers
            assignStatsAndCalculateModifiers(rolledStats, writer);

        } catch (IOException e) 
        {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
    }

    public static void intro()
    {
        System.out.println("Hello! Let's roll up your character's stats!");
        System.out.println("This program will roll your stats, and then you'll be able to assign them.");
        System.out.println("Let's get started!");
    }

    public static int[] rolls(FileWriter writer) throws IOException
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

        return rolls;
    }
    

    public static void assignStats(int[] rolledStats)
    {
        Scanner scanner = new Scanner(System.in);
        String[] statNames = {"STR", "DEX", "CON", "INT", "WIS", "CHA"};
        int[] assignedStats = new int[6];
        boolean[] used = new boolean[6]; // To track which rolled stats have been assigned

        System.out.println("You rolled the following stats: ");
        for (int i = 0; i < rolledStats.length; i++) {
            System.out.print(rolledStats[i] + " ");
        }
        System.out.println("\nNow, assign these stats to your character's attributes.");

        for (int i = 0; i < statNames.length; i++) {
            boolean validInput = false;
            while (!validInput) {
                System.out.print("Assign a value to " + statNames[i] + ": ");
                int value = scanner.nextInt();

                // Check if the value is in the rolled stats and hasn't been used yet
                for (int j = 0; j < rolledStats.length; j++) {
                    if (rolledStats[j] == value && !used[j]) {
                        assignedStats[i] = value;
                        used[j] = true; // Mark this value as used
                        validInput = true;
                        break;
                    }
                }

                if (!validInput) {
                    System.out.println("Invalid input. Please assign an unused rolled value.");
                }
            }
        }

        System.out.println("You have assigned the stats as follows:");
        for (int i = 0; i < statNames.length; i++) {
            System.out.println(statNames[i] + ": " + assignedStats[i]);
        }

        // Optionally, write the assigned stats to the file
        try (FileWriter writer = new FileWriter("charCreation.txt", true)) {
            writer.write("Assigned stats:\n");
            for (int i = 0; i < statNames.length; i++) {
                writer.write(statNames[i] + ": " + assignedStats[i] + "\n");
            }
        } catch (IOException e) {
            System.out.println("An error occurred while writing to the file.");
            e.printStackTrace();
        }
        scanner.close();
    }

    public static int[] rerollLowStats(int[] rolledStats, FileWriter writer) throws IOException 
    {
        Scanner scanner = new Scanner(System.in);
    
        for (int i = 0; i < rolledStats.length; i++) 
        {
            if (rolledStats[i] < 7) {
                System.out.println("Stat " + rolledStats[i] + " is below 7. Would you like to re-roll it? (yes/no)");
                String response = scanner.nextLine().trim().toLowerCase();
    
                if (response.equals("yes")) 
                {
                    int[] rollsResult = rolls(writer); // Re-roll the stat
                    int rollTotal = rollsResult[0] + rollsResult[1] + rollsResult[2] + rollsResult[3] - Math.min(Math.min(rollsResult[0], rollsResult[1]), Math.min(rollsResult[2], rollsResult[3]));
                    rolledStats[i] = rollTotal; // Update the stat with the new roll
    
                    // Write the re-rolled stat to the file
                    writer.write("Re-rolled stat: " + rollTotal + "\n");
                    System.out.println("Re-rolled stat: " + rollTotal);
                }
            }
        }
    
        scanner.close();
        return rolledStats;
    }

    public static void assignStatsAndCalculateModifiers(int[] rolledStats, FileWriter writer) throws IOException 
    {
        Scanner scanner = new Scanner(System.in);
        String[] statNames = {"STR", "DEX", "CON", "INT", "WIS", "CHA"};
        int[] assignedStats = new int[6];
        boolean[] used = new boolean[6]; // To track which rolled stats have been assigned

        System.out.println("You rolled the following stats: ");
        for (int i = 0; i < rolledStats.length; i++) 
        {
            System.out.print(rolledStats[i] + " ");
        }
        System.out.println("\nNow, assign these stats to your character's attributes.");

        for (int i = 0; i < statNames.length; i++) 
        {
            boolean validInput = false;
            while (!validInput) 
            {
                System.out.print("Assign a value to " + statNames[i] + ": ");
                int value = scanner.nextInt();

                // Check if the value is in the rolled stats and hasn't been used yet
                for (int j = 0; j < rolledStats.length; j++) 
                {
                    if (rolledStats[j] == value && !used[j]) 
                    {
                        assignedStats[i] = value;
                        used[j] = true; // Mark this value as used
                        validInput = true;
                        break;
                    }
                }

                if (!validInput) 
                {
                    System.out.println("Invalid input. Please assign an unused rolled value.");
                }
            }
        }

        System.out.println("You have assigned the stats as follows:");
        writer.write("Assigned stats and modifiers:\n");
        for (int i = 0; i < statNames.length; i++) 
        {
            int modifier = calculateModifier(assignedStats[i]);
            System.out.println(statNames[i] + ": " + assignedStats[i] + " (Modifier: " + modifier + ")");
            writer.write(statNames[i] + ": " + assignedStats[i] + " (Modifier: " + modifier + ")\n");
        }
        scanner.close();
    }

    public static int calculateModifier(int abilityScore) 
    {
        return (abilityScore - 10) / 2;
    }
}