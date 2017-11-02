"""
Given two rectangles, find if the given two rectangles overlap or not.

 Notice

l1: Top Left coordinate of first rectangle.
r1: Bottom Right coordinate of first rectangle.
l2: Top Left coordinate of second rectangle.
r2: Bottom Right coordinate of second rectangle.

l1 != r1 and l2 != r2

Example
Given l1 = [0, 8], r1 = [8, 0], l2 = [6, 6], r2 = [10, 0], return true

Given l1 = [0, 8], r1 = [8, 0], l2 = [9, 6], r2 = [10, 0], return `false

"""
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {Point} l1 top-left coordinate of first rectangle
    # @param {Point} r1 bottom-right coordinate of first rectangle
    # @param {Point} l2 top-left coordinate of second rectangle
    # @param {Point} r2 bottom-right coordinate of second rectangle
    # @return {boolean} true if they are overlap or false
    def doOverlap(self, l1, r1, l2, r2):
        # Write your code here
        if r1.x < l2.x or l1.x > r2.x:
            return False
        if r1.y > l2.y or l1.y < r2.y:
            return False
        return True