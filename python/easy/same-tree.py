# https://leetcode.com/problems/same-tree/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def depth_first_search(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 == None or node2 == None:
                return False
            elif node1.val != node2.val:
                return False
            
            return depth_first_search(node1.left, node2.left) and depth_first_search(node1.right, node2.right)

        return depth_first_search(p, q)

# Can't really run this locally and had to take some help
# Sorry for cheating. Atleast I learnt Depth First Search.
# https://leetcode.com/problems/same-tree/submissions/962446947/