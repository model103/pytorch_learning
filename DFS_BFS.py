class TreeNode():
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(0)
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
#n2.left = n5
#n2.right = n6

class Search():
    def __init__(self):
        self.dfs_rst = []
        self.bfs_rst = []
        self.queue = []  #BFS维护的队列
    def DFS(self, root):
        if root == None:
            return
        else:
            self.dfs_rst.append(root.val)
            self.DFS(root.left)
            self.DFS(root.right)
        return self.dfs_rst
    def BFS(self, root):
        self.queue.append(root)
        while self.queue:
            node = self.queue.pop(0)
            if node.left != None:
                self.queue.append(node.left)
            if node.right != None:
                self.queue.append(node.right)
            self.bfs_rst.append(node.val)
        return self.bfs_rst


search = Search()
print(search.DFS(root))
print(search.BFS(root))