
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def print_linked_list(node):
    while node:
        print(node.val, end=" -> " if node.next else "\n")
        node = node.next


def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

# Create inputs
list1 = build_linked_list([1, 2, 4])
list2 = build_linked_list([1, 3, 4])

print_linked_list(mergeTwoLists(list1,list2))


