"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.


Example
Challenge 
Could you solve it with O(1) space?
"""

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        dic = {}
        tmp = head
        while tmp:
            dic[tmp] = RandomListNode(tmp.label)
            tmp = tmp.next
        tmp = head
        while head:
            if head.next:
                dic[head].next = dic[head.next]
            if head.random:
                dic[head].random = dic[head.random]
            head = head.next
        return dic[tmp]

"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return head
        self.copy_next(head)
        self.copy_random(head)
        return self.split_list(head)
        
        
        
    def copy_next(self, head):
        while head:
            node = RandomListNode(head.label)
            node.next = head.next
            head.next = node
            head = head.next.next
    
    
    def copy_random(self, head):
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
        
    
    def split_list(self, head):
        new_head = head.next
        while head:
            tmp = head.next
            head.next = tmp.next
            head = tmp.next
            if head:
                tmp.next = head.next
            
        return new_head
        
        
        
            
