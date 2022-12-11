def middleNode(head):
    """
        if not head:
            return head
        first = head
        second = head
        while first.next and first.next.next:
            print(first.val)
            print(second.val)
            second = second.next
            first = first.next.next
        
        if first.next:
            second = second.next
        
        return second
    """
    """
        total = 0
        temp = head
        while temp.next:
            total += 1
            temp = temp.next
        total += 1
        mid = total//2
        indx = 0
        temp = head
        print(mid, total)
        while indx < mid:
            temp = temp.next
            indx += 1
        
        return temp
    """
    """
        if not head:
            return head
        fast = head
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        if fast.next:
            slow = slow.next
        return slow
    """
    """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
    """