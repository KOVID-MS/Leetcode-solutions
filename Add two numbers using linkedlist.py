def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        carry = 0
        final = ListNode(0)
        temp = final
        while l1 is not None or l2 is not None:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            carry = sum // 10
            sum = sum % 10
            temp.next = ListNode(sum)
            temp = temp.next   

        if carry > 0:
            temp.next = ListNode(carry)
    
        return final.next
