class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms:
            return

        m, n = len(rooms), len(rooms[0])
        q = []

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        dis = 1

        while q:
            tmp_q = []
            while q:
                x, y = q.pop()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < m and 0 <= yy < n and rooms[xx][yy] == 2147483647:
                        rooms[xx][yy] = dis
                        tmp_q.append((xx, yy))

            q = tmp_q
            dis += 1
