# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        t_dict = dict()
        while head:
            if t_dict.get(head, False):
                return True
            t_dict[head] = True
            head = head.next
        return False