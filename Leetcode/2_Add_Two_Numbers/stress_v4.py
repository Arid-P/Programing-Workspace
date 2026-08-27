import random
from typing import Optional

def print_list(current):
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# --- New Function: Generates a random linked list ---
def generate_random_list(max_length=10):
    """Generates a linked list of random length (1 to max_length) 
    with random single-digit integers."""
    length = random.randint(1, max_length)
    dummy = ListNode(0)
    current = dummy
    for _ in range(length):
        current.next = ListNode(random.randint(0, 9))
        current = current.next
    return dummy.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def list_to_num (self, ll):
        num = 0
        i = 0
        while ll:
            num = num + ll.val*(10**i)
            ll = ll.next
            i += 1
        
        return num
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.list_to_num(l1)
        num2 = self.list_to_num(l2)
        list_sum = num1 + num2
        
        head = None
        while list_sum :
            digit = list_sum % 10 
            list_sum = list_sum // 10 
            
            if not head:
                head = ListNode(digit)
                neck = head
            else:
                neck.next = ListNode(digit)
                neck = neck.next
        
        return head

def main():
    sol = Solution()
    
    for _ in range(10) :
        # Generate two random lists
        print("--- Generating Random Lists ---")
        l1 = generate_random_list(max_length=9)
        l2 = generate_random_list(max_length=7)
        
        print("List 1:", end=" ")
        print_list(l1)
        print("List 2:", end=" ")
        print_list(l2)
        
        # Process and print results
        print("\n--- Adding Numbers ---")
        result = sol.addTwoNumbers(l1, l2)
        print("Result: ", end=" ")
        print_list(result)
        print('  \n   \n  ')

if __name__ == '__main__':
    main()
