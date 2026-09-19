import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	
		float a;
		float b;
		float c;
		float res = 0;
		int t = 1000000000;
		boolean equal = false;
		String op;
		
    	
    	System.out.println("Enter the value");
    	a=sc.nextFloat();
    	System.out.println("Type the symbol for the following use:\n    + for addition\n    -- for subtraction\n    * for multiplication\n    / for division\n    % for reminder\n    = for result\nRemmber this");
         op = sc.next();
         System.out.println("Enter the next digit");
		  b = sc.nextFloat();
	          switch(op){
                     case "+":
	                      res = a + b;
	                    break;
	                  case "-":
	                       res = a - b;
	                     break;
	                   case "*":
	                        res = a * b;
	                       break;
	                     case "/":
	                           res = a / b;
	                         break;
	                       case "%":
	                            res = a % b;
	                         break;
	                      default : 
	                            System.out.println("Invalid option");
	                           break;
	              }
	                   
		for(int i=1;i<=t;i++){
	          System.out.println("Enter the opration");
	           op = sc.next();
	               switch(op){
                     case "+":
	                      System.out.println("Enter the next digit");
	                       c = sc.nextFloat(); 
	                       res+=c;
	                    break;
	                  case "-":
	                       System.out.println("Enter the next digit");
	                         c = sc.nextFloat();
	                       res-=c;
	                     break;
	                   case "*":
	                        System.out.println("Enter the next digit");
	                         c = sc.nextFloat();
	                         res*=c;
	                       break;
	                     case "/":
	                           System.out.println("Enter the next digit");
	                         c = sc.nextFloat();
	                           res/=c;
	                         break;
	                       case "%":
	                           System.out.println("Enter the next digit");
	                            c = sc.nextFloat();
	                            res%=c;
	                         break;
	                       case "=":
	                            equal = true; 
	                          break;
	                      default : 
	                            System.out.println("Invalid option");
	                           break;
	              }// inner switch ends
	               if(equal == true){
	                             break;
	                   }
	         }//loop ends
	  System.out.println("Result = " + res);
	}
}