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

def mergeKLists(lists: list[ListNode]) -> list[ListNode]:
        
        flag = 0
        first = 0
        if not lists:
            return None
        
        for i,ll in enumerate(lists):
            if ll:
                flag = 1
                break
        
        curr = ListNode()
        head = curr

        if flag == 0:
            return None

        for i,ll in enumerate(lists):
            if not ll:
                continue
            appo2 = ll
            if first == 0:
                curr.next = ll
                first = 1
            else:    
                while ll:
                    if curr.next:
                        appo = curr.next
                        if ll.val >= curr.val and ll.val <= curr.next.val:
                            ll = ll.next
                            curr.next = appo2
                            appo2.next = appo
                        curr = curr.next
                        appo2 = ll
                    else:
                        curr.next = appo2
                        break
                curr = head

        return head.next


# Create inputs
list1 = build_linked_list([1])
list2 = build_linked_list([0])


print_linked_list(mergeKLists([list1,list2]))