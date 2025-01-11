# * https://chatgpt.com/share/678298d6-b200-800a-b3ba-4184f7b09cd4 // This chat is to visualize the code
# * https://leetcode.com/problems/merge-nodes-in-between-zeros/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    # Initialize a sentinel/dummy node with the first non-zero value.
    modify = head.next
    next_sum = modify

    while next_sum:
        sum = 0
        # Find the sum of all nodes until you encounter a 0.
        while next_sum.val != 0:
            sum += next_sum.val
            next_sum = next_sum.next

        # Assign the sum to the current node's value.
        modify.val = sum
        # Move nextSum to the first non-zero value of the next block.
        next_sum = next_sum.next
        # Move modify also to this node.
        modify.next = next_sum
        modify = modify.next
    return head.next
