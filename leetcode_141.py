class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end="-->")
        curr = curr.next
    print(None)

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
print_list(head)

sol = Solution()
print_list(sol.hasCycle(head))
    
