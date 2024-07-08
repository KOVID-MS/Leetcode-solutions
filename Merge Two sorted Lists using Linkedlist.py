def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        temp = dummy

        while list1 is not None or list2 is not None:
            if list1 is None:
                temp.next = list2
                break
            else:
                x = list1.val
            if list2 is  None:
                temp.next = list1
                break
            else: 
                y = list2.val
            if x <= y:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
        return dummy.next
