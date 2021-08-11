import linked_list

class Solution:
    def mergeTwoLists1(self, l1, l2):
        dummy = cur = linked_list.MyLinkedList()
        while l1 and l2:
            if l1.value < l2.value:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next.value

l1 = linked_list.MyLinkedList()
l2 = linked_list.MyLinkedList()

for i in [1,2,3]:
    l1.AddAtTail(i)
for i in [1,3,4]:
    l2.AddAtTail(i)

x = Solution()
# In this example, we pass in the first node  of each list instead of the lists themselves. 
# Each node is evaluated on its own with the list label since a node can be a list once it has a pointer. weird ik.
print(x.mergeTwoLists1(l1.head, l2.head))