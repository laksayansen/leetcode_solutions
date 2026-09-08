# Last updated: 9/8/2026, 2:09:12 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        lst = ListNode()
9        node = lst
10        while list1 and list2:
11            if list1.val <= list2.val:
12                node.next = list1
13                list1 = list1.next
14            else:
15                node.next = list2
16                list2 = list2.next
17            node = node.next
18        node.next = list1 if list1 else list2
19        return lst.next
20       