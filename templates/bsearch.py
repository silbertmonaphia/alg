def bsearch(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) / 2
        if array[mid] == target:
            # found the target !!
            break or return result
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
