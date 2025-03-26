public class dndToolbag 
{
    //just a rough framework for now
    //will probably figure out how to link files for this one

    public static void main(String[] args)
    {
        Scanner k = new Scanner (System.in);
        final int PLAY = 1;
        final int CREATE = 2;

        System.out.println("Welcome to the D&D Toolbag!\n\nAre you in Play mode or Creation mode?");
        System.out.println("1) Play\n2) Character Creation");
        int userMode = k.nextInt();

        if (userMode == PLAY)
        {
            //TODO
            //call a seperate play() function
        }
        else if (userMode == CREATE)
        {
            //TODO
            //call a seperate charCreation() function
        }
        else
        {
            System.out.println("Invalid input.")
            System.out.println("1) Play\n2) Character Creation");
            userMode = k.nextInt();
        }
    }
}