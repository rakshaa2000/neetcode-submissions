class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            # Go as deep left as possible
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Process the current node
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # Move to the right subtree
            curr = curr.right