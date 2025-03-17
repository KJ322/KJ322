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

            int rollTotal = (roll1 + roll2 + roll3 + roll4) - ;
            
            System.out.println(rollTotal);
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

            int rollTotal = (roll1 + roll2 + roll3 + roll4) - //TODO;
            
            System.out.println(rollTotal);
        }
    }
}
