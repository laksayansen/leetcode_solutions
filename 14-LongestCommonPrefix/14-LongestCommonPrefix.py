# Last updated: 8/15/2026, 11:12:22 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        prefix = strs[0]
4        for i in strs[1:]:
5            j = 0
6            while j < len(prefix) and j < len(i) and prefix[j] == i[j]:
7                j += 1
8            prefix = prefix[:j]
9            if not prefix:
10                return ""
11        return prefix