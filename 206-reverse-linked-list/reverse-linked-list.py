# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        temp=None
        curr=head
        while curr!=None:
            next_node=curr.next
            curr.next=temp
            temp=curr
            curr=next_node
        return temp



        