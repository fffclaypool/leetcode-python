class Solution:
    def isValidBST(self, root):
        return self.helper(root)

    def helper(self, node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True
        val = node.val

        if val <= lower or val >= upper:
            return False
        if not self.helper(node.left, lower, val):
            return False
        if not self.helper(node.right, val, upper):
            return False
        return True
