# Part A Question 7
class TreeNode:
	def __init__(self,data=0, left=None, right=None):
		self.data = data
		self.left = None
		self.right = None

def hasPathSum(root, s:int)->bool:
        ans=0
        sub = s-root.data	
        if(sub == 0 and root.left == None and root.right == None):
            return True
        if root.left is not None:
            ans = ans or hasPathSum(root.left, sub)
            if root.right is not None:
                ans = ans or hasPathSum(root.right, sub)
                return ans
s = 22
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.right = TreeNode(0)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.left.right = TreeNode(2)
root.right.left.left = TreeNode(0)
root.left.left.left= TreeNode(7)
root.left.left.right=TreeNode(2)

if hasPathSum(root, s):
	print ("True") 
else:
	print ("False")