import java.util.*;

public class Main
{
	public static void main(String[] r)
	{
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter the size of the arr");
		int size = sc.nextInt();
		
		int input[] = new int[size];
		
		System.out.println("Enter the values");
		for(int i=0; i<size; i++)
		{
		  input[i] = sc.nextInt();
		}
		
		System.out.println("Enter the value of which you index want");
		int key = sc.nextInt();
		
		boolean check = 1;
		for(int i=0; i<size; i++)
    {
      if(input[i] == key)
      {
        System.out.println("Index of " + key + " is " + i);
        check = 1;
        break;
      }
      else
      {
       check = 0; 
      }
      //loop ends
    }
      
      if(check != 1)
      {
        System.out.println("This value is not in the array");
      }
      
    }
		//function ends
	}
// class ends
