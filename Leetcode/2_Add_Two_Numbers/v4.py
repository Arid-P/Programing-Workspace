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
        if list_sum == 0:
            head = ListNode(0)
        
        while list_sum :
            digit = list_sum % 10 
            list_sum = list_sum // 10 
            print(digit, list_sum)
            if not head:
                head = ListNode(digit)
                neck = head
            else:
                neck.next = ListNode(digit)
                neck = neck.next
        
        return head

def main():
    l1 = ListNode(0)
    l2 = ListNode(0)
    
    
    print_list(l1)
    print_list(l2)
    sol = Solution()
    head = sol.addTwoNumbers(l1, l2)
    print_list(head)

if __name__ == '__main__':
    main()
