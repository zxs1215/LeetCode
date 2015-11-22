# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

        
def getval(node):
    return node.val if node!=None else 0

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addin = 0
        head = ListNode(addin)
        node = head
        while(l1 or l2):
            addout = getval(l1) + getval(l2) + addin
            addin = addout/10
            addout = addout % 10
            node.val = addout
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or addin != 0:
                node.next = ListNode(addin)
            node = node.next
        return head