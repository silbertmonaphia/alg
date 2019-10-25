class Solution:
    def maxSlidingWindow_refine(self, nums, k):
        if not nums: return []
        window, res = [], []
        for i, x in enumerate(nums):
            if i >= k and window[0] <= i - k:
                # Pop from the front if window is full
                window.pop(0)
            while window and nums[window[-1]] <= x:
                # Kick out those less than x in window
                window.pop()
            window.append(i)
            if i >= k - 1:
                # Define the output timing
                res.append(nums[window[0]])
        return res

    def maxSlidingWindow(self, nums, k):
        if not nums: return []
        window = nums[0:k]
        max_num = max(window)
        results = [max_num]
        for i in nums[k:]:
            if i > max_num:
                max_num = i
                window.append(i)
            if i <= max_num:
                window.append(i)

            val = window.pop(0)
            if val == max_num:
                max_num = max(window)
            results.append(max_num)
        print(results)
        return results


#nums = [1,-1]
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = [3,3,5,5,6,7]
assert(Solution().maxSlidingWindow(nums, k) == result)

# [-7,-8,7,5,7,1,6,0]


