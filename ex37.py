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


def deleteMiddle(head: ListNode) -> ListNode:
        
    count = 0
    appo = head

    while appo:
        count += 1
        appo = appo.next
    
    appo = head
    for i in range(count):
        if i == int(count/2)-1:
            appo2 = appo.next 
            appo.next = appo2.next
            appo2.next = None
            break
        else:
            appo = appo.next
    
    return head


# Create inputs
list1 = build_linked_list([1,3,4,7,1,2,6])

print_linked_list(deleteMiddle(list1))