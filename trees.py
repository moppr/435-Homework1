class Node:
    '''Basic node used for trees'''
    
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.value)
        
    def is_leaf(self):
        return self.left == self.right == None
    
    
class Tree:
    '''Basic tree using nodes'''
    
    def __init__(self, num_nodes, node_array):
        self.num_nodes = num_nodes
        self.node_array = node_array        
        self.root = self.node_array[0] if self.num_nodes != 0 else None
        
        self.from_array()
        
    def from_array(self):
        '''Convert an array of nodes into a tree.'''
        
        if not self.root:
            return
        
        def populate(node, i):
            '''Recursively point node to its left and right children, if they exist.'''
            # i, l, and r represent indices
            # note: for node at i, left child is at 2i+1, right child is at 2i+2
            l = 2*i + 1
            r = 2*i + 2
            
            # l,r must exist if the index is in bounds
            node.left = self.node_array[l] if l < self.num_nodes else None
            node.right = self.node_array[r] if r < self.num_nodes else None
            
            if node.left:
                populate(node.left, l)
            if node.right:
                populate(node.right, r)
                
        populate(self.root, 0)
        
    def to_array(self):
        '''Format the given array of nodes into a string.'''
        return ' '.join([str(node) for node in self.node_array])
    
    def is_BST(self):
        '''Return True or False whether the tree is a binary search tree or not.'''
        # trees with 0 or 1 nodes are automatically BSTs
        if self.num_nodes <= 1:
            return True
        
        # so, this should only be reached if there are at least 2 nodes
        def BST_helper(node, min, max):
            '''Recursively check if children of given node are in order and that children are also BSTs.'''
            result = False if node.value < min or node.value > max else True
            if node.left:
                result = result and node.left.value < node.value and BST_helper(node.left, min, node.value-1)
            if node.right:
                result = result and node.right.value > node.value and BST_helper(node.right, node.value+1, max)
            return result
        
        tree_min = min([int(value) for value in self.to_array().split()]) - 1
        tree_max = max([int(value) for value in self.to_array().split()]) + 1
        
        return BST_helper(self.root, tree_min, tree_max)
    
    def pre_order(self):
        '''Traverse the tree in pre-order and print result.'''
        #Note: pre-order = root, left, right
        
        def pre_helper(node):
            result = str(node)
            if node.left:
                result += ' ' + pre_helper(node.left)
            if node.right:
                result += ' ' + pre_helper(node.right)
            return result
            
        return pre_helper(self.root) if self.root else ''
    
    def post_order(self):
        '''Traverse the tree in post-order and print result.'''
        #Note: post-order = left, right, root
        
        def post_helper(node):
            result = ''
            if node.left:
                result += post_helper(node.left) + ' '
            if node.right:
                result += post_helper(node.right) + ' '
            result += str(node)
            return result
            
        return post_helper(self.root) if self.root else ''
    
    def num_nodes_in_lookup(self, value):
        '''Search for the given value and return number of nodes visited.'''
        
        if self.is_BST():
            # binary search used for BSTs
            def binary_search(node):
                visited = 1
                if node.value == value:
                    return visited
                return 1 + binary_search(node.left if value < node.value else node.right)
                
            # assumes that value provided is in the tree, therefore, this method won't be called on empty trees
            return binary_search(self.root)
                
        else:
            # level-order traversal used for non BSTs
            queue = [self.root]
            visited = 0
            
            while len(queue) > 0:
                visited += 1
                current_node = queue.pop(0)                
                if current_node.value == value:
                    return visited
                
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    

if __name__ == '__main__':

    # parsing inputs
    num_nodes = int(input())
    node_array = [Node(int(value)) for value in input().split()]
    num_commands = int(input())
    commands = [input() for _ in range(num_commands)]
    
    tree = Tree(num_nodes, node_array)
    
    for command in commands:
        if command == 'toArray':
            print(tree.to_array())
        elif command == 'isBST':
            print("true" if tree.is_BST() else "false") # test cases don't like python :(
        elif command == 'preOrder':
            print(tree.pre_order())
        elif command == 'postOrder':
            print(tree.post_order())
        else: # numNodesInLookup
            print(tree.num_nodes_in_lookup(int(command.split()[-1])))
