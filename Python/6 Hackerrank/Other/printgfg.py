#User function Template for python3

class Solution:
    count = 1
    
    @classmethod
    def printGfg(cls, n):
        print("GFG", end=" ")
        if cls.count < n :
            cls.count += 1
            cls.printGfg(n)
        # Code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        Solution.count = 1
        N = int(input())
        ob = Solution()
        ob.printGfg(N)
        print()
        print("~")
# } Driver Code Ends