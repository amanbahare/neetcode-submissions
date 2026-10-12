# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = head

        while curr:
            temp = ListNode(curr.val)  # naya node

            temp.next = new_head   #current reversed list se jodo

            new_head = temp            # naya node ab new head ban gaya

            curr = curr.next           # original list me aage badho

        return new_head
