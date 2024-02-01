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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = head = ListNode()
        while list1 and list2:
            tail.next = ListNode()
            tail = tail.next

            if list1.val < list2.val:
                tail.val = list1.val
                list1 = list1.next
            else:
                tail.val = list2.val
                list2 = list2.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return head.next
    
list1 = []
list2 = [0]
list1 = ListNode.from_list(list1)
list2 = ListNode.from_list(list2)
print(Solution().mergeTwoLists(list1, list2))
