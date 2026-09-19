import java.util.*;

public class Main{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    
    int input = sc.nextInt();
    
    for(int i=1; i<=input; i++)
    {
      int space = input - i;
      
      for(int j=1; j<=space; j++)
      {
        System.out.print(" ");
      }
      
      for(int j=1; j<=input; j++)
      {
        System.out.print("*");
      }
      System.out.println();
    }
    // function ends
  }
  // class ends
}