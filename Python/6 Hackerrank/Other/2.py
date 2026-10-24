from collections import deque

class Solution:
    def maxOfMins(self, arr, k):
        stack = deque(arr[ : k])
        
        max_num = max(stack)
        i = k
        
        answer: list = [max_num]
        while i < len(arr):
            popped = stack.popleft()
            stack.append( arr[i] )
            
            if popped == max_num :
                max_num = max(stack)
            elif max_num < arr[i] :
                max_num = arr[i]
            
            answer.append(max_num)
            
            i += 1
        
        #print(answer)
        return answer


#{  # Driver Code Starts
if __name__ == "__main__":
    #t = int(input())
    t = 2
    for _ in range(t):
        print(f"Test case {t}")
        arr = list(map(int, input().split(" ")))
        k = int(input(" Enter k "))
        solution = Solution()
        result = solution.maxOfMins(arr, k)
        print(" ".join(map(str, result)))
        print("~")
# } Driver Code Ends