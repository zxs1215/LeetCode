# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head == None:
            return
        node = head
        count = 1
        while node.next != None:
            node = node.next
            count += 1
        node = head
        print(count)
        print(node.val)
        i = 1
        while i < count - n:
            node = node.next
            i += 1
        print(node.val) 
        prev = node
        if prev.next == None:
            return None
        else:
            prev.next = prev.next.next
        return head

node = ListNode(1)
next = ListNode(2)
node.next = next
sol = Solution()
sol.removeNthFromEnd(node, 2)    
input()       