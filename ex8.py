class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd( head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next == None:
            return None
        i = 1
        appo = head
        length = 0
        while appo.next != None:
            appo = appo.next
            length += 1
        
        if length == n:
            realHead = head.next
            return realHead

        realHead = head
        i = 1
        while i <= length - n:
            head = head.next
            i += 1 

        if length - n == 0:
            realHead = head.next
        
        if head.next == None:
            realHead.next = None
        else:
            appo = head.next
            head.next = appo.next

        return realHead