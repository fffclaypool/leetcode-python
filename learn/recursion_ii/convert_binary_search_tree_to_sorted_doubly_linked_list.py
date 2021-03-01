class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def helper(node):

            nonlocal last, first

            if node:
                helper(node.left)
                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node
                last = node
                helper(node.right)

        if not root:
            return None

        first, last = None, None
        helper(root)
        last.right = first
        first.left = last
        return first
