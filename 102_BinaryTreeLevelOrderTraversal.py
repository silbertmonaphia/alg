# formmat:cmd+shift+f
# select all occurrence:cmd+shift+l
# select next occurrence:
# multirow edit:cmd+option+shif+up/down

# BFS way
class Solution:
    import collections
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = collections.deque()
        queue.append(root)

        # visited = set(root) # Graph traversal

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)
        return result

# DFS way
class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        self.result = []
        self._dfs(root, 0)
        return self.result

    def _dfs(self, node, level):
        if not node:
            return
        if len(self.result) < level + 1:
            self.result.append([])

        self.result[level].append(node.val)

        self._dfs(node.left, level + 1)
        self._dfs(node.right, level + 1)
