# Last updated: 8/15/2026, 10:07:16 AM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        roman = {
4            "I": 1,
5            "V": 5,
6            "X": 10,
7            "L": 50,
8            "C": 100,
9            "D": 500,
10            "M": 1000
11        }
12        integer = 0
13        prev_value = 0
14        for i in s[::-1]:
15            curr_value = roman[i]
16            if curr_value < prev_value:
17                integer -= curr_value
18            else:
19                integer += curr_value
20            prev_value = curr_value
21        return integer