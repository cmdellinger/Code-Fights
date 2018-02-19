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
def isListPalindrome(l):
    if not l or not l.next:
        return True
    
    def get_length(linked_list):
        from itertools import count
        length = count()
        current = linked_list
        while current:
            length.next()
            current = current.next
        return length.next()
    
    def compare_ll(lst_1, lst_2):
        while lst_1 and lst_2:
            #print lst_1.value, lst_2.value
            if lst_1.value != lst_2.value:
                return False
            lst_1 = lst_1.next
            lst_2 = lst_2.next
        return True
    
    def reverse_half(head, length):
        new_head = None
        for index in range(length//2):
            head.next, head, new_head = new_head, head.next, head
        return head, new_head
    
    list_length = get_length(l)
    f_list, r_list = reverse_half(l, list_length)
    if list_length % 2: # if there's a reminder
        return compare_ll(f_list.next, r_list)
    else: # if no remainder (divisible by 2)
        return compare_ll(f_list, r_list)
