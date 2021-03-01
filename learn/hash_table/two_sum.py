class Solution:
    def twoSum(self, nums, target):

        dic = {}
        for i, v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v], i]
            dic[v] = i
