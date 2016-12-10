#Given a linked list, remove the nth node from the end of list and return its head.

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        res = ListNode(0)
        res.next = head
        tmp = res
        for i in range(n):
            head = head.next
        while head:
            head = head.next
            tmp = tmp.next
        tmp.next = tmp.next.next
        return res.next
