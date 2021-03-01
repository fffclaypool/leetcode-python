class Solution:
    def hasPathSum(self, root, root_sum):

        if not root:
            return False

        root_sum -= root.val

        if not root.left and not root.right:
            return root_sum == 0

        return self.hasPathSum(root.left, root_sum) or self.hasPathSum(root.right, root_sum)
