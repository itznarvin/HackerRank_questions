# Given the array of integers, find the sum of its elements 
# Example : If the array (ar = [1,2,3]. 1 + 2 + 3 = 6, so return 6

n = (input())
array = list(map(int, input().split()))

print(sum(array))