class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        while l1.next:
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)
        while l2.next:
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)
        print(num1, num2)
        num3 = str(int(num1[::-1]) + int(num2[::-1]))
        i = len(num3)-1
        l3 = ListNode(num3[i])
        curr = l3

        for val in num3[::-1][1:]:
            curr.next = ListNode(val)
            curr = curr.next

        return l3
