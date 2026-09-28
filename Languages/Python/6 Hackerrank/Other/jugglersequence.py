#User function Template for Python
from math import sqrt

class Solution:
    arr: list = []
    
    @classmethod
    def jugglerSequence(self, n):
        self.arr.append(n) 
        
        self.new_n_even = int(sqrt(n))
        self.new_n_odd = int( sqrt(n ** 3) )
        
        if self.new_n_odd != 1 and self.new_n_even != 1 :
            if n % 2 == 0 :
                self.jugglerSequence(self.new_n_even)
            elif n % 2 != 0 :
                self.jugglerSequence(self.new_n_odd)
        else :
            final_arr = self.arr
            final_arr.append(1)
            
            Solution.arr = []
            return "hello"
            
        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(f" {ob.jugglerSequence(n) = } ")
        arr = ob.jugglerSequence(n)
        print(f" {arr = } ")
        for i in (arr):
            print(i, end=" ")
        print()

        print("~")
# } Driver Code Ends