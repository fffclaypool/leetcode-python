class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        stack, output = [], []

        while root or stack:
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            else:
                output.append(root.val)
                root = None

        return output
