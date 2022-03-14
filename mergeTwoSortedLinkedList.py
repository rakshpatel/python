def mergeTwoLists(list1, list2):
        if list1 and list2:
            if list1.val <= list2.val:
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
        elif list1 and not list2:
            return list1
        else:
            return list2
        output = temp
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        while list1:
            temp = list1
            list1 = list1.next
            temp = temp.next
        
        while list2:
            temp = list2
            list2 = list2.next
            temp = temp.next
        return output
