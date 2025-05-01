import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class inventory 
{
    private static ArrayList<String> inventory = new ArrayList<>();

    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) 
        {
            System.out.println("\nInventory Tracker:");
            System.out.println("1. Add item");
            System.out.println("2. Remove item");
            System.out.println("3. View inventory");
            System.out.println("4. Exit");
            System.out.print("Choose an option: ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            switch (choice) 
            {
                case 1:
                    addItem(scanner);
                    break;
                case 2:
                    removeItem(scanner);
                    break;
                case 3:
                    viewInventory();
                    break;
                case 4:
                    running = false;
                    System.out.println("Exiting inventory tracker.");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    private static void addItem(Scanner scanner) 
    {
        System.out.print("Enter the name of the item to add: ");
        String item = scanner.nextLine();
        inventory.add(item);
        updateFile();
        System.out.println("Item added to inventory.");
    }

    private static void removeItem(Scanner scanner) 
    {
        System.out.print("Enter the name of the item to remove: ");
        String item = scanner.nextLine();
        if (inventory.remove(item)) 
        {
            updateFile();
            System.out.println("Item removed from inventory.");
        } 
        else 
        {
            System.out.println("Item not found in inventory.");
        }
    }

    private static void viewInventory() 
    {
        System.out.println("\nCurrent Inventory:");
        if (inventory.isEmpty()) 
        {
            System.out.println("Inventory is empty.");
        } 
        else 
        {
            for (String item : inventory) 
            {
                System.out.println("- " + item);
            }
        }
    }

    private static void updateFile() 
    {
        try 
        {
            // Read the existing file content
            File file = new File("charCreation.txt");
            StringBuilder fileContent = new StringBuilder();
            boolean inventorySectionFound = false;

            try (BufferedReader reader = new BufferedReader(new FileReader(file))) 
            {
                String line;
                while ((line = reader.readLine()) != null) 
                {
                    if (line.equals("Inventory:")) 
                    {
                        inventorySectionFound = true;
                        fileContent.append("Inventory:\n");
                        for (String item : inventory) 
                        {
                            fileContent.append("- ").append(item).append("\n");
                        }
                        // Skip old inventory lines
                        while ((line = reader.readLine()) != null && line.startsWith("- ")) 
                        {
                            // Do nothing, just skip
                        }
                    }
                    if (line != null) 
                    {
                        fileContent.append(line).append("\n");
                    }
                }
            }

            // If no inventory section was found, add it at the end
            if (!inventorySectionFound) 
            {
                fileContent.append("\nInventory:\n");
                for (String item : inventory) 
                {
                    fileContent.append("- ").append(item).append("\n");
                }
            }

            // Write the updated content back to the file
            try (FileWriter writer = new FileWriter(file)) 
            {
                writer.write(fileContent.toString());
            }
        } 
        catch (IOException e) 
        {
            System.out.println("An error occurred while updating the file.");
            e.printStackTrace();
        }
    }
}