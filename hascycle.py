def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
