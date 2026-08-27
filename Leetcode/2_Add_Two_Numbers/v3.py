import random
from typing import Optional

def print_list(current):
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


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
    l1 = ListNode(9)
    l2 = ListNode(9)
    
    l12 = ListNode(9)
    l22 = ListNode(9)
    
    l1.next = l12
    l2.next = l22
    
    for i in range(5):
        l12.next = ListNode(9)
        l12 = l12.next
        
    for i in range(2):
        l22.next = ListNode(9)
        l22 = l22.next
    
    print_list(l1)
    print_list(l2)
    sol = Solution()
    head = sol.addTwoNumbers(l1=l1, l2=l2)
    print_list(head)

if __name__ == '__main__':
    main()
