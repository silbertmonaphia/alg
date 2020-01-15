class Solution:
    def lowestCommonAncestor(self, root, p, q):
        def find_q_or_q(root,p,q):
          if root == p or root == q or root is None:
              return root
          left = find_q_or_q(root.left,p,q)
          right = find_q_or_q(root.right,p,q)
          if left is None:
              return right
          elif right is None:
              return left
          else:
              return root
        return find_q_or_q(root,p,q)