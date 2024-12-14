# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False  # Empty list or single node without a cycle

        slow = head  # Slow pointer moves one step at a time
        fast = head  # Fast pointer moves two steps at a time

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If the slow and fast pointers meet, there is a cycle
            if slow == fast:
                return True

        return False  # If no cycle is detected
