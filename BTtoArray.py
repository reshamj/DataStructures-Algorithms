#complete binary tree representation as an array 
from collections import deque 
#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    


    #iterative with queue 
      def levelOrder(self, root: TreeNode) -> List[List[int]]:
            if not root:
                return []
            
            queue = [root]
            result =[]
            result.append(root.val)
            
            while len(queue):
                node= queue.pop(0)                
                if node.left:
                    result.append(node.left.val)
                    queue.append(node.left)
                else:
                    result.append('null')
                
                if node.right:
                    queue.append(node.right)
                    result.append(node.right.val)
                else:
                    result.append('null')
            print(result)
            return result 
    
