from typing import Optional
def print_list (current):
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
    
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        carry = 0
        
        while l1 or l2:
            if l1:
                digit1 = l1.val
            else:
                l1 = ListNode()
            if l2 :
                digit2 = l2.val
            else:
                l2 = ListNode()
            
            digit_sum = digit1 + digit2 + carry
            
            if digit_sum < 10 :
                result.append(ListNode(digit_sum))
            else:
                sum_str = str(digit_sum)
                carry = int(sum_str[0])
                result.append(ListNode(int(sum_str[1])))
            
            l1 = l1.next
            l2 = l2.next      
        
        for i in range(len(result) - 1):
            result[i].next = result[i+1]
        
        return result[0]

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
    
    sol = Solution()
    sol = Solution()
    head = sol.addTwoNumbers(l1=l1, l2=l2)
    print_list(head)

if __name__ == '__main__':
    main()