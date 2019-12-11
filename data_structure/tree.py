class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    @classmethod
    def from_sorted_list(cls, arr):
        if not arr: 
            return None
    
        # find middle 
        mid = (len(arr)) / 2
        
        # make the middle element the root 
        root = TreeNode(arr[mid]) 
        
        # left subtree of root has all 
        # values <arr[mid] 
        root.left = cls.sortedArrayToBST(arr[:mid]) 
        
        # right subtree of root has all  
        # values >arr[mid] 
        root.right = cls.sortedArrayToBST(arr[mid+1:]) 
        return root

