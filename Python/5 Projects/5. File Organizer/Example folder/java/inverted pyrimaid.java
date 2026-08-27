import java.util.*;

public class Main
{
	public static void main(String[] r)
	{
		Scanner sc = new Scanner(System.in);
		
		int input = 4;
		
		int n = 3;
		for(int i=input; i>=1; i--)
	  {
		  int space = input - n;
		  for(int j=1; j<=space; j++)
		  {
		    System.out.print(" ");
		  }
		  n--;
		  
		  for(int j=i; j>=1; j--)
		  {
		    System.out.print("*");
		  }
		  
		  for(int j=1; j<=(i-1); j++)
		  {
		    System.out.print("*");
		  }
		  System.out.println();
		}
		
		//function ends
	}
	// class ends
}