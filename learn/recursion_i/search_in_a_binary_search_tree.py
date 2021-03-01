class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if not root or root.val == val:
            return root
        return self.searchBST(root.left, val) or self.searchBST(root.right, val)
