import java.util.*;

public class Main
{
	public static void main(String[] r)
	{
		Scanner sc = new Scanner(System.in);
		
		//int input = sc.nextInt();
		int input = 4;
		
		for(int i=1; i<=input; i++)
		{
		  int space = input - i;
      
      for(int j=1; j<=space; j++)
      {
        System.out.print(" ");
      }
      
      for(int j=i; j>=1; j--)
      {
        System.out.print("*");
      }
      
      for(int j=2; j<=i; j++)
      {
        System.out.print("*");
      }
      System.out.println();
		}
		
		int n = 3;
		for(int i=input; i>=1; i--)
		{
		  int space = i - n;
		  for(int j=1; j<=space; j++)
		  {
		    cout << " ";
		  }
		  n++;
		  for(int j=i; j<=1; j--)
		  {
		    
		  }
		}
		//function ends
	}
	//class ends
}