# Last updated: 9/11/2026, 8:33:26 AM
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        n, m = len(haystack), len(needle)
4        for i in range(n - m + 1):
5            if haystack[i:i+m] == needle:
6                return i
7        return -1
8