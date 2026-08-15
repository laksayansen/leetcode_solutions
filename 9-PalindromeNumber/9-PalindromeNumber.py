# Last updated: 8/15/2026, 9:37:55 AM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        string = str(x)
4        if string[::-1] != string:
5            return False
6        return True