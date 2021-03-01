class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        n, m = len(grid), len(grid[0])
        visited = []

        for _ in range(n):
            visited.append([False]*m)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and visited[i][j] is False:
                    count += 1
                    self.bfs(grid, i, j, visited)

        return count

    def bfs(self, grid, i, j, visited):
        q = []
        q.append((i, j))

        while q:
            x, y = q.pop()
            if visited[x][y] is True:
                continue
            if x+1 < len(grid) and grid[x+1][y] == "1":
                q.append((x+1, y))
            if y+1 < len(grid[0]) and grid[x][y+1] == "1":
                q.append((x, y+1))
            if x-1 >= 0 and grid[x-1][y] == "1":
                q.append((x-1, y))
            if y-1 >= 0 and grid[x][y-1] == "1":
                q.append((x, y-1))
            visited[x][y] = True
