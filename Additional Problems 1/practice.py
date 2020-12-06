from random import randrange

def largest(arr):
    def largest_impl(acc, rest):
        return largest_impl(max(acc, rest[0]), rest[1:]) if len(rest) else acc
    return largest_impl(arr[0], arr[1:])

def reverse(arr):
    n = len(arr)
    for i in range(n//2):
        j = n-i - 1
        (arr[i], arr[j]) = (arr[j], arr[i])
    return arr

def occurs(elem, arr):
    return elem == arr[0] or occurs(elem, arr[1:]) if len(arr) else False

def odd_elems(arr):
    return arr[::2]

def is_palindrome(str_):
    return len(str_) < 2 or (str_[0] == str_[-1] and is_palindrome(str_[1:-1]))

nums = [randrange(100) for _ in range(10)]
print(nums)
print(largest(nums))
print(reverse(nums))
print(occurs(50, nums))
print(odd_elems(nums))
print(is_palindrome("racecar"))