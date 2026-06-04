class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0) #we can pass any
        tail = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
        if curr1:
            tail.next = curr1
        else:
            tail.next = curr2
        return dummy.next
    
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end="-->")
        curr = curr.next
    print(None)

#Create List1
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)
print_list(list1)

#create List2
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
print_list(list2)

sol = Solution()
merged = sol.mergeTwoLists(list1, list2)


print_list(merged)


