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
    def length_list(self, current):
        length = 0
        while current:
            length += 1
            current = current.next
        return length 

    def make_equal(self, l1, l2):
        l1_length = self.length_list(l1)
        l2_length = self.length_list(l2)
        
        diff = l1_length - l2_length
        
        if diff == 0:
            return l1, l2
        elif diff > 0:
            ln = l2
            while ln.next:
                ln = ln.next
            for _ in range(diff):
                ln.next = ListNode(0)
                ln = ln.next
        else:
            ln = l1
            while ln.next:
                ln = ln.next
            for _ in range(abs(diff)):
                ln.next = ListNode(0)
                ln = ln.next
        
        return l1, l2
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        l1, l2 = self.make_equal(l1, l2)
        
        head = None
        neck = None
        
        while l1 or l2:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            
            digit_sum = digit1 + digit2 + carry
            carry = digit_sum // 10
            val = digit_sum % 10
            
            if head is None:
                head = ListNode(val)
                neck = head
            else:
                neck.next = ListNode(val)
                neck = neck.next
            
            if l1: 
                l1 = l1.next
            if l2: 
                l2 = l2.next
        
        if carry:
            neck.next = ListNode(carry)
            
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
