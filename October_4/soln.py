class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if not root :                                               # if null node
            return False                                            # return False
    
        if (not root.right and not root.left                        # if target hit on leaf, 
            and root.val == targetSum):                             # return True
            return True
        
        return (self.hasPathSum(root.left ,targetSum-root.val) or   # traverse left  subtree
                self.hasPathSum(root.right,targetSum-root.val))     # traverse right subtree
