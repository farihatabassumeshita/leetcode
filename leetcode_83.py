class ListNode(object):
    def __init__(self, val=0, next=0):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

sol = Solution()
print(sol.deleteDuplicates(head = [1,1,2]))