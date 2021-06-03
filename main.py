###### First topic: RECURSION - June 02 2021 ######
# Recursion: a process that calls itself -
# Base case: a condition for the recursion to stop

# Example 1: factorial
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print(factorial(6))
'''

# Example 2: productOfArray
# Write a function called productOfArray which takes in an array
# of numbers and returns the product of them all.

#--In JavaScript--#
'''
// productOfArray([1, 2, 3]) // 6
// productOfArray([1, 2, 3, 10]) // 60

function productOfArray(arr){
    if (arr.length === 0){
        return 1;
    }
    return arr[0] * productOfArray(arr.slice(1));
}
'''
#--In Python--#

def productOfArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0]*productOfArray(arr[1:])

print(productOfArray([1, 2, 3]))
print(productOfArray([1, 2, 3, 10]))
