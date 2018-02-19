# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    sum_l = None
    overage = 0
    while a != None and b != None:
        if not sum_l:
            sum_l = ListNode(a.value + b.value)
            head = sum_l
        else:
            sum_l.next = ListNode(a.value + b.value + overage)
        if sum_l.value > 9999:
            overage = sum_l.value//10000
            sum_l.value %= 10000
        a = a.next
        b = b.next
        sum_l = sum_l.next
    return head
