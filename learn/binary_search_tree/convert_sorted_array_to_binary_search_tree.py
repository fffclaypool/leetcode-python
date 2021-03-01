class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right):
        if left > right:
            return None

        p = (left + right) // 2
        root = TreeNode(nums[p])
        root.left = self.helper(nums, left, p - 1)
        root.right = self.helper(nums, p + 1, right)
        return root
