class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # Step 1: Both nodes are empty
        if p is None and q is None:
            return True

        # Step 2: Only one node is empty
        if p is None or q is None:
            return False

        # Step 3: Compare node values
        if p.val != q.val:
            return False

        # Step 4: Compare left and right subtrees
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        return left and right