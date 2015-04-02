class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        self.connect_list([root])
    def connect_list(self, list):
        length = len(list)
        i = 0
        next = []
        #print(list)
        while  i < length:
            left = list[i].left
            right = list[i].right
            if left != None:
                next.append(left)
            if right != None:
                next.append(right)
            if i > 0:
                list[i - 1].next = list[i]
            i += 1
        if len(next) != 0:
            self.connect_list(next)

node = TreeLinkNode(1)
left = TreeLinkNode(2)
right = TreeLinkNode(3)
node.left = left
node.right = right
sol = Solution()
sol.connect(node)
input()

