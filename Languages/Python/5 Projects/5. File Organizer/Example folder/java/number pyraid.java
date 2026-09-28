import java.util.*;

public class Main
{
	public static void main(String[] r)
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
      
      for(int j=1; j<=i; j++)
      {
        System.out.print(i + " ");
      }
      System.out.println();
		}
		
		//function ends
	}
	// class ends
}