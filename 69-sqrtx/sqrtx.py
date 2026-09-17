class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x
        while i <= j:
            mid = (i + j) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                i = mid + 1
            else:
                j = mid - 1
        return j
