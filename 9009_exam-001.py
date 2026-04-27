# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 08:52:17 2016

@author: xtong1
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#print quicksort([3,6,8,10,1,2,1])
if __name__ == '__main__':
   print quicksort([3,6,8,10,1,2,1])