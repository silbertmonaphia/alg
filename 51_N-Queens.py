# LeetCode 51 & 52
class Solution:
    def solveNqueens(self, n):
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.positive_slope = set()
        self.negative_slope = set()
        self.DFS(n, 0, [])

        return self._generate_result(n)

    def DFS(self, n, row, cur_state):
        if row >= n:
            self.result.append(cur_state)
            return

        for col in range(n):
            if col in self.cols or row+col in self.positive_slope or row - col in self.negative_slope:
                # print(cur_state)
                continue

            self.cols.add(col)
            self.positive_slope.add(row + col)
            self.negative_slope.add(row - col)

            self.DFS(n, row+1, cur_state+[col])

            self.cols.remove(col)
            self.positive_slope.remove(row + col)
            self.negative_slope.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.'*i + 'Q'+'.'*(n - i - 1))
        return [board[i:i+n] for i in range(0, len(board), n)]

from pprint import pprint
pprint(Solution().solveNqueens(4))
assert(Solution().solveNqueens(4) == [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']])
