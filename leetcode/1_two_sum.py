#! /usr/bin/env python3
# encoding:utf8

"""
Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums:List[int]
        :type target: int
        :rtype List:[int]
        """
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m],i]
            else:
                d[n] = i

    def test(self):
        nums = [3,3]
        target = 6
        wanted = [0,1]
        actual = self.twoSum(nums,target)
        assert(wanted == actual)

        nums = [3,2,4]
        target = 6
        wanted = [1,2]
        actual = self.twoSum(nums,target)
        assert(wanted == actual)




if __name__ == '__main__':
    Solution().test()


