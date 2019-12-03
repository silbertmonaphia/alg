class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        res = set()
        for i,v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                # 如果和前面一个值相等就跳过，因为情况和前面一个值都是一样的
                continue
            d = {}
            for x in nums[i+1:]:
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v,-v-x,x))
        return list(res)
                

test_case = [-1,0,1,2,-1,-4]
res = Solution().threeSum(test_case)
assert(res == [(-1, -1, 2), (-1, 0, 1)])