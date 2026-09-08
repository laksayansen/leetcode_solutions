# Last updated: 9/8/2026, 5:33:33 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 1
4        for i in range(1, len(nums)):
5            if nums[i] == nums[k - 1]:
6                nums[i] = nums[k]
7            else:
8                nums[k] = nums[i]
9                k += 1
10        return k
11