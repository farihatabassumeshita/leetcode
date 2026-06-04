class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next #store next
            curr.next = prev #reverse link
            prev = curr #move prev
            curr = nxt #move curr forward
        return prev
    
def print_list(head): #helper function
    curr = head
    while curr:
        print(curr.val, end="-->")
        curr = curr.next
    print("None")

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

sol = Solution()
print_list(head)
print_list(sol.reverseList(head))



