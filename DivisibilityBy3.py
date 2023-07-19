'''
Divisibility by 3
Given a number in the form of an array A of size N. Each of the digits of the number is represented by A[i]. Check if the number is divisible by 3.

Input 1:
A = [1, 2, 3]

Input 2:
A = [1, 0, 0, 1, 2]

Output 1: 1

Output 2: 0
'''
array = list(map(int, input().split()))

result = 0
for i in range(0,len(array)):
    result += (((10**(len(array)-i-1)))* array[i])
print(1 if result % 3 == 0 else 0)
