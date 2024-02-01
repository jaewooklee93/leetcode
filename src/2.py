from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def from_list(cls, xs):
        if not xs:
            return None
        else:
            return cls(xs[0], cls.from_list(xs[1:]))
    
    def __repr__(self):
        return f"{self.val} {self.next}"

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode()
        carry = 0
        while l1 or l2 or carry:
            tail.next = ListNode()
            tail = tail.next
            v1, n1 = (l1.val, l1.next) if l1 else (0, None)
            v2, n2 = (l2.val, l2.next) if l2 else (0, None)
            l1, l2, carry, tail.val = n1, n2, *divmod(v1 + v2 + carry, 10)
        return head.next

def main():
    l1 = ListNode.from_list([2,4,3])
    l2 = ListNode.from_list([5,6,4])
    print(Solution().addTwoNumbers(l1, l2))
            
if __name__ == "__main__":
    main()