class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        if p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if inorder == p.val:
                return root

            inorder = root.val
            root = root.right

        return None
