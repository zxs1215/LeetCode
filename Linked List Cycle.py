#理解题目意思 链表有环 的意思是尾巴可能接链表中的任何一个元素

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None:
            return False
        node = head
        doubleNode = head
        while node != None and doubleNode != None and doubleNode.next != None:
            node = node.next
            doubleNode = doubleNode.next.next
            if node == doubleNode:
                return True
        return False