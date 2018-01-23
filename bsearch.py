#! /usr/bin/env python3
# encoding:utf-8


def b_search(nums, target):
    # O(logN)
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] > target:
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] == target:
            while(mid > 0 and nums[mid] == nums[mid - 1]):
                mid = mid - 1
            return mid
    print('Not Found')
    return -1


def b_search_recursive(nums, target, low=None, high=None):
    # O(logN)
    low = low or 0
    high = high or len(nums) - 1
    mid = (low + high) // 2
    if low > high:
        return -1
    if nums[mid] == target:
        # define an exit first if recursive
        while(mid > 0 and nums[mid] == nums[mid - 1]):
            mid = mid - 1
        return mid
    elif nums[mid] > target:
        high = mid - 1
    elif nums[mid] < target:
        low = mid + 1
    return b_search_recursive(nums, target, low=low, high=high)


def test_b_search():
    target = 2

    nums = [1, 2, 3, 4, 5]
    result = b_search(nums, target)
    result = b_search_recursive(nums, target)
    print(result)
    assert(result == 1), '1'

    nums = [1, 2, 3, 4, 5, 6]
    result = b_search(nums, target)
    result = b_search_recursive(nums, target)
    print(result)
    assert(result == 1), '5'

    nums = [2, 2, 2, 3, 4, 5, 6]
    result = b_search(nums, target)
    result = b_search_recursive(nums, target)
    print(result)
    assert(result == 0), '2'

    nums = [1, 2, 2, 2, 5]
    result = b_search(nums, target)
    result = b_search_recursive(nums, target)
    print(result)
    assert(result == 1), '3'

    nums = [1, 1, 3, 4, 5]
    result = b_search(nums, target)
    result = b_search_recursive(nums, target)
    print(result)
    assert(result == -1), '4'


if __name__ == '__main__':
    test_b_search()
