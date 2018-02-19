"""
Codefights: Interview Prep - isListPalindrome.py
Written by cmdellinger
    
Checks if a singly linked list is a palindrome.
"""
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
''' works for most tests:
    
    Sample tests: 11/11
    Hidden tests: 8/11
    Score: 120/300
'''

def isListPalindrome(l):
    # edge case for list size 0
    if not l:
        return True

    def get_compare(f_node):
        ''' helper that gets reverse list and compares values '''
        if f_node == None:
            return l
        r_node = get_compare(f_node.next)
        if isinstance(r_node, bool):
            return r_node
        if f_node.value == r_node.value:
            if r_node.next == None:
                return True
            else:
                return r_node.next
        else:
            return False

return get_compare(l)
