from data_structure import Stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()
        lookup = {')': '(', ']':'[', '}': '{'}
        for c in s:
            if c not in lookup:
                stack.push(c)
            elif stack.is_empty() or stack.pop() != lookup[c]:
                return False
        return stack.is_empty()

if __name__ == '__main__':
    tests = ["(){}[]","([{]})","(]","([)]","())","(()"]
    results = []
    for test in tests:
        result = Solution().isValid(test)
        print(result)
        results.append(result)
    assert(results == [True,False,False,False,False,False])
        