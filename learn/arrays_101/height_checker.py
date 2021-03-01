class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        orig = heights[:]
        heights.sort()
        diffs = 0

        for i in range(len(orig)):
            if orig[i] != heights[i]:
                diffs += 1
        return diffs
