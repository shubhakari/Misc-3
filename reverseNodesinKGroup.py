# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, root: Optional[ListNode], k: int) -> Optional[ListNode]:
        if root is None or root.next is None:
            return root
        def reverse(root):
            if root is None or root.next is None:
                return root
            revp = reverse(root.next)
            root.next.next = root
            root.next = None
            return revp
        temp = root
        ct,nodect = 0,0
        while temp:
            ct += 1
            temp = temp.next
        temp = root
        finallist = ListNode(-1)
        finaltemp = finallist
        while temp  and (ct-nodect) >= k  and nodect < ct:
            i = 0
            revlist = ListNode(-1)
            dummy = revlist
            while temp and i < k:
                dummy.next = temp
                i += 1
                nodect += 1
                temp = temp.next
                dummy  = dummy.next
            dummy.next = None
            revlist = reverse(revlist.next)
            finaltemp.next = revlist
            while finaltemp.next is not None:
                finaltemp = finaltemp.next
        while temp != None :
            finaltemp.next = temp
            temp = temp.next
            finaltemp = finaltemp.next
        return finallist.next