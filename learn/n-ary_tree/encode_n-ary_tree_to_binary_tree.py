class Codec:

    def encode(self, root):

        if not root:
            return None

        rootNode = TreeNode(root.val)

        if len(root.children) > 0:
            firstChild = root.children[0]
            rootNode.left = self.encode(firstChild)

        curr = rootNode.left

        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right

        return rootNode

    def decode(self, data):

        if not data:
            return None

        rootNode = Node(data.val, [])
        curr = data.left

        while curr:
            rootNode.children.append(self.decode(curr))
            curr = curr.right

        return rootNode
