#! /usr/bin/env python3
# coding:utf8

from math import pow


class Solution(object):
    def reverse_1(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 0
        if x < 0:
            num = -x
            neg = 1
        else:
            num = x

        y = []
        while num != 0:
            y.append(num % 10)
            num = num // 10

        result = 0
        for y_ in y:
            result = result * 10 + y_

        if result >= pow(2, 32):
            return 0
        if neg:
            return -result
        return result

    def reverse_2(self, x):
        neg = 0
        if x < 0:
            x = -x
            neg = 1
        res = 0
        while x:
            res = res * 10 + x % 10
            x = x // 10
        if neg:
            res = -res
        return res if res.bit_length() < 32 else 0

    def reverse(self, x):
        sign = -1 if x < 0 else 1
        res = int(str(abs(x))[::-1]) * sign
        import pdb;pdb.set_trace()
        return True if res == x else False
        # return res if res.bit_length() < 32 else 0

    def test(self):
        # x = 123
        # wanted = 321
        # actual = self.reverse(x)
        # assert(wanted == actual)

        # x = -123
        # wanted = -321
        # actual = self.reverse(x)
        # assert(wanted == actual)

        # x = 120
        # wanted = 21
        # actual = self.reverse(x)
        # assert(wanted == actual)

        # x = 1563847412
        # wanted = 0
        # actual = self.reverse(x)
        # assert(wanted == actual)

        x = -2147447412
        wanted = True
        actual = self.reverse(x)
        assert(wanted == actual)


if __name__ == '__main__':
    Solution().test()
