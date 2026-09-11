class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if guess > target:
                j = mid - 1
            else:
                i = mid + 1
        return i
