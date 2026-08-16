# Last updated: 8/16/2026, 11:42:21 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stack = []
4        pairs = {
5            ")": "(",
6            "]": "[",
7            "}": "{"
8        }
9
10        for i in s:
11            if i in pairs:
12                if not stack or stack.pop() != pairs[i]:
13                    return False
14            else:
15                stack.append(i)
16
17        return not stack