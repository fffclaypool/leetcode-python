class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        l = []
        for v in nums:
            if len(str(v)) % 2 == 0:
                l.append(v)
        return len(l)
