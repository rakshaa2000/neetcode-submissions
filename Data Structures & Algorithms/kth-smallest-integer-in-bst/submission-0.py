class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        numNodesMap = {}
        
        def numNodes(node):
            if not node:
                return 0
            if node in numNodesMap:
                return numNodesMap[node]
            numNodesMap[node] = numNodes(node.left) + numNodes(node.right) + 1
            return numNodesMap[node]
        
        # Precompute the sizes once so the cache persists during our search
        numNodes(root) 

        def search(node, rank):
            # Calculate elements strictly smaller than the current node
            left_size = numNodesMap[node.left] if node.left else 0
            
            if rank == left_size + 1:
                return node.val
            elif rank <= left_size:
                return search(node.left, rank)
            else:
                # Subtract left subtree elements AND the current root node
                return search(node.right, rank - left_size - 1)
                
        return search(root, k)