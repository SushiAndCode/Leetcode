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


def reverseList(head: ListNode) -> ListNode:
        
        appo = ListNode()
        dum = appo
        supp = []

        while head:
            supp.append(head.val)
            head = head.next
        
        supp.reverse()

        for i in supp:
            dum.next = ListNode(i)
            dum = dum.next
        
        return dum.next

# Create inputs
list1 = build_linked_list([1,2,3,4,5])

print_linked_list(reverseList(list1))