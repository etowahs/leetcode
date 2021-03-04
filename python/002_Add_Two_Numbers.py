class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    convert to number, then back to linked list
    """
    def addTwoNumbers(self, l1, l2):
        def toNum(node_list):
            str1 = ''
            while True:
                str1 += str(node_list.val)
                if node_list.next is None:
                    break
                else:
                    node_list = node_list.next
            return int(str1[::-1])

        s1, s2 = toNum(l1), toNum(l2)
        head = ListNode()
        ll = head
        answer = str(s1 + s2)[::-1]
        for char in answer[:-1]:
            ll.val = int(char)
            ll.next = ListNode()
            ll = ll.next
        ll.val = answer[-1]

        return head


if __name__ == '__main__':
    s = Solution()
