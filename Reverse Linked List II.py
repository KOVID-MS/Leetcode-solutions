def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if left == right:
            return head
        pre = ListNode(0)
        pre.next = head
        for _ in range(left-1):
            pre = pre.next
        temp = pre
        cur = pre.next
        after = cur.next
        if head == cur:
            for _ in range(right-1):
                head = head.next

        for _ in range(right-left):
            pre = cur
            cur = after
            if after:
                after = after.next
                cur.next = pre
        
        temp.next.next = after
        temp.next = cur
        return head
