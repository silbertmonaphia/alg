class Solution:
    def threeSum(self, nums):
        # This impl is neat!O(n2)
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {} # Extra space for a dict O(n)
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return list(res)

    def threeSum_n2(self, nums):
        # O(n2)
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                # Search from both ends to the middle
                s = nums[i] + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append((nums[i], nums[left], nums[right]))
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left > right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1


test_case = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(test_case)
assert(res == [(-1, -1, 2), (-1, 0, 1)])
for result in res:
    assert(sum(result) == 0)
