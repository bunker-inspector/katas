class Tree:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, new_val):
        if new_val >= self.val:
            if self.right == None:
                self.right = Tree(new_val)
            else:
                self.right.insert(new_val)
        elif new_val < self.val:
            if self.left == None:
                self.left = Tree(new_val)
            else:
                self.left.insert(new_val)

    def height(self):
        return self._height(self)

    def _height(self, node, ht=0):
        if node is None:
            return ht
        else:
            return max(self._height(node.left, ht+1), self._height(node.right, ht+1))

    def is_balanced(self):
        def _is_balanced(node, ht=0, ht_min=float("inf"), ht_max=0):
            if node is None:
                if ht < ht_min:
                    ht_min = ht
                if ht > ht_max:
                    ht_max = ht 
                return ht, ht_min, ht_max

            ht += 1
            if (ht_max - ht_min) <= 1:
                ht, ht_min, ht_max = _is_balanced(node.left, ht, ht_min, ht_max)
                ht, ht_min, ht_max = _is_balanced(node.right, ht, ht_min, ht_max)

            return ht, ht_min, ht_max
        _, ht_min, ht_max = _is_balanced(self)
        return (ht_max - ht_min) <= 1


    def print_inorder(self):
        if self.left != None:
            self.left.print_inorder()
        print(self.val)
        if self.right != None:
            self.right.print_inorder()

if __name__ == '__main__':
    t = Tree(2)
    t.insert(1)
    t.insert(3)

    print(t.is_balanced())
