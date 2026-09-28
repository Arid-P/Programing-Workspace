
class Solution:
    def __init__ (self) :
        self.stack: list[int] = []
    
    
    def division (self, num1, num2) -> int :
        if num1 * num2 > 0 :
            return num1 // num2
        else :
            return -1 * ( (-1 * num1) // num2)
    
    
    def evaluate(self, arr: list[str]) -> int:
        for el in arr:
            # Checking if el is an operator
            if el in {"+", "-", "*", "/"}:
                num2 = self.stack.pop()
                num1 = self.stack.pop()

                if el == "+":
                    result = num1 + num2
                elif el == "-":
                    result = num1 - num2
                elif el == "*":
                    result = num1 * num2
                elif el == "/":
                    # Handling integer division and zero division
                    result = self.division(num1, num2) if num2 != 0 else 0

                self.stack.append(result)

            else:
                # Append operand as integer to self.stack
                self.stack.append(int(el))

        return self.stack[0]

#{
 # Driver Code Starts


if __name__ == "__main__":
    #t = int(input())
    t = 2
    for _ in range(t):
        print(f"Test case {_}")
        arr = input().split()
        solution = Solution()
        print(solution.evaluate(arr))
        print("~")

# } Driver Code Ends