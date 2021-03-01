class Solution(object):

    def flatten(self, head):

        if not head:
            return head

        pseudoHead = Node(None, None, head, None)
        self.flatten_dfs(pseudoHead, head)
        pseudoHead.next.prev = None

        return pseudoHead.next

    def flatten_dfs(self, prev, curr):

        if not curr:
            return prev

        curr.prev = prev
        prev.next = curr
        tempNext = curr.next

        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None

        return self.flatten_dfs(tail, tempNext)
