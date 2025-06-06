class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
    
def insert(root, key):
        
       
        if root is None:
            return Node(key)
        if root.val == key:
            return root
        if root.val < key:
            root.right = insert(root.right,key)
        else:
            root.left = insert(root.left,key)
        
        return root

def inorder(root):
        if root:
            inorder(root.left)
            print(root.val)
            inorder(root.right)

r = Node(50)
print(r)
r = insert(r, 30)
print(r)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print(r)

# Print inorder traversal of the BST
inorder(r)
 


        
         