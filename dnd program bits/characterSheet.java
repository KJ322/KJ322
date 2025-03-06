
import java.io.*;
import java.util.Scanner;

// By implementing Serializable interface
// we make sure that state of instances of class CharacterSheet
// can be saved in a file.
class CharacterSheet implements Serializable 
{
    private static final long serialVersionUID = 1L;
    
    //character stats
    int experience;
    String charName, charClass, playerName;
    int str, dex, con, intel, wis, cha;

    // CharacterSheet class constructor
    public CharacterSheet(int experience, String charName, String charClass, String playerName, int str, int dex, int con, int intel, int wis, int cha) 
    {
        this.experience = experience;
        this.charName = charName;
        this.charClass = charClass;
        this.playerName = playerName;
        this.str = str;
        this.dex = dex;
        this.con = con;
        this.intel = intel;
        this.wis = wis;
        this.cha = cha;
    }
}

public class Test 
{
    public static void main(String[] args) throws IOException, ClassNotFoundException 
    {
        // TODO: get all the info

        /*
        int steps = 100;
        String dogName = "Esther";
        String dogBreed = "Lab Mix";
        String owner = "norrisa";
        */
        // Ask the User to type the info
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter experience points (or 0): ");
        int experience = scanner.nextInt();
        scanner.nextLine();  // Consume newline

        System.out.print("Enter your charcter's name: ");
        String charName = scanner.nextLine();

        System.out.print("Enter your character's class: ");
        String charClass = scanner.nextLine();

        System.out.print("Enter the player name: ");
        String playerName = scanner.nextLine();

        System.out.print("Enter Strength (STR): ");
        int str = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Dexterity (DEX): ");
        int dex = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Constitution (CON): ");
        int con = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Intelligence (INTEL): ");
        int intel = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Wisdom (WIS): ");
        int wis = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter Charisma (CHA): ");
        int cha = scanner.nextInt();
        scanner.nextLine();
        // cleanup
        scanner.close();

        // Make the object
        CharacterSheet tracker = new CharacterSheet(experience, charName, charClass, playerName, str, dex, con, intel, wis, cha);
        // Write it to a file
        System.out.println("Writing file...");
        // Serializing 'tracker'
        FileOutputStream fos = new FileOutputStream("char_sheet.data");
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(tracker);

        // De-serializing 'tracker'
        FileInputStream fis = new FileInputStream("char_sheet.data");
        ObjectInputStream ois = new ObjectInputStream(fis);
        CharacterSheet new_charsheet = (CharacterSheet) ois.readObject(); // down-casting object
        System.out.println("Reading file...");
        System.out.println("Character Name: " + new_charsheet.charName + ", Experience: " + new_charsheet.experience);
        System.out.println("Character Class: " + new_charsheet.charClass);
        System.out.println("Player: " + new_charsheet.playerName);
        System.out.println("STR: " + new_charsheet.str);
        System.out.println("DEX: " + new_charsheet.dex);
        System.out.println("CON: " + new_charsheet.con);
        System.out.println("INTEL: " + new_charsheet.intel);
        System.out.println("WIS: " + new_charsheet.wis);
        System.out.println("CHA: " + new_charsheet.cha);
        // TODO: print all the other data 
        // closing streams
        oos.close();
        ois.close();
    }
}

