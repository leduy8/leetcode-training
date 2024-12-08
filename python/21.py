
# * https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = cur = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return dummy.next


print(mergeTwoLists(list1=[1, 2, 4], list2=[1, 3, 4]))  # [1,1,2,3,4,4]
print(mergeTwoLists(list1=[], list2=[]))  # []
print(mergeTwoLists(list1=[], list2=[0]))  # [0]
