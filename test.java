public static void main (String[args])

public static boolean bears(int initial, int goal, int increment, int n) {
   if (initial == goal)
      return true;
   else if (n == 0)
      return false;
   else if (bears(initial+increment, goal, increment, n-1))
      return true;
   else if ((initial%2 == 0) && bears(initial/2, goal, increment, n-1))
      return true;
   else
      return false;
} 