# 1. Solution - Brute Force
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # finding lenght of List
        lenght = 0
        tmp = head
        while tmp != None:
            lenght += 1
            tmp = tmp.next
        # fing middle element
        mid = lenght // 2
        i = 0
        while i < mid:
            head = head.next
            i += 1
        return head


# 2. Solution - Two-Pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head 
        # when the second pointer is at the end of the list, the first one will only be in the middle
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head
