# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def solve(node):
            nonlocal ans

            if not node:
                return 0, 0

            left_sum, left_cnt = solve(node.left)
            right_sum, right_cnt = solve(node.right)

            total = node.val + left_sum + right_sum
            count = 1 + left_cnt + right_cnt

            if node.val == total // count:
                ans += 1

            return total, count

        solve(root)
        return ans