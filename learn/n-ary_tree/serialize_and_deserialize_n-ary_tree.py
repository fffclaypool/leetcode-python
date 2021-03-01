class Codec:

    def serialize(self, root: 'Node') -> str:

        if not root:
            return ""

        serializedList = []
        self._serializeHelper(root, serializedList)
        return "".join(serializedList)

    def _serializeHelper(self, root, serializedList):

        queue = collections.deque()
        queue.append(root)
        queue.append(None)

        while queue:
            node = queue.popleft()

            if node == None:
                serializedList.append("#")
                if queue:
                    queue.append(None)
            elif node == "C":
                serializedList.append("$")
            else:
                serializedList.append(chr(node.val + 48))

                for child in node.children:
                    queue.append(child)

                if queue[0] != None:
                    queue.append("C")

    def deserialize(self, data: str) -> 'Node':

        if not data:
            return None

        rootNode = Node(ord(data[0])-48, [])
        self._deserializeHelper(data, rootNode)
        return rootNode

    def _deserializeHelper(self, data, rootNode):

        prevLevel, currentLevel = collections.deque(), collections.deque()
        currentLevel.append(rootNode)
        parentNode = rootNode

        for i in range(1, len(data)):
            if data[i] == "#":
                prevLevel = currentLevel
                currentLevel = collections.deque()
                parentNode = prevLevel.popleft() if prevLevel else None
            else:
                if data[i] == "$":
                    parentNode = prevLevel.popleft() if prevLevel else None
                else:
                    childNode = Node(ord(data[i]) - 48, [])
                    currentLevel.append(childNode)
                    parentNode.children.append(childNode)
