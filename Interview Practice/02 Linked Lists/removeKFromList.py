"""
Codefights: Interview Prep - removeKFromList.py
Written by cmdellinger
    
Removes all values of k in the simple linked list.
"""

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def removeKFromList(l, k):
    current = l
    while current:
        if current.next and current.next.value == k:
            current.next  = current.next.next
        else:
            current = current.next
    if l and l.value == k: return l.next
    return l
