# BFS way
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def minDepth(self, root):
        if not root:
            return 0
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        left_min_depth = self.minDepth(root.left)
        right_min_depth = self.minDepth(root.right)

        return 1 + min(left_min_depth, right_min_depth)
