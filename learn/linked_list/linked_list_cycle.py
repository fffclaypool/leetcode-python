class Solution(object):
    def hasCycle(self, head):
        nodes = set()
        current = head

        while current:
            if current in nodes:
                return True
            else:
                nodes.add(current)
            current = current.next

        return False
