class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.next = None
        self.parent = None

class RankPairingHeap:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        self.root = self.merge(self.root, new_node)

    def get_min(self):
        return self.root.value if self.root else None

    def delete_min(self):
        if not self.root:
            return None
        old_root = self.root
        self.root = self.combine_siblings(self.root.children)
        return old_root.value

    def empty(self):
        return self.root is None

    def merge(self, x, y):
        if not x:
            return y
        elif not y:
            return x
        if x.value > y.value:
            y.children.append(x)
            x.parent = y
            return y
        else:
            x.children.append(y)
            y.parent = x
            return x

    def combine_nodes(self, x, y):
        if x.value > y.value:
            x, y = y, x
        x.children.append(y)
        y.parent = x
        return x

    def combine_siblings(self, children):
        if not children:
            return None
        if len(children) == 1:
            return children[0]
        new_root = self.combine_nodes(children[0], children[1])
        siblings = [new_root]
        for i in range(2, len(children), 2):
            new_sibling = self.combine_nodes(children[i], children[i + 1]) if i + 1 < len(children) else children[i]
            siblings.append(new_sibling)
        return self.combine_siblings(siblings)

    def printHeap(self):
        if not self.root:
            print("Heap is empty")
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.value, end=' ')
            queue.extend(node.children)
            if node.next:
                print('|', end=' ')
                queue.append(node.next)
            else:
                print()

    def contains_value(self, value):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.value == value:
                return node
            queue.extend(node.children)
            if node.next:
                queue.append(node.next)
        return None

    def get_siblings(self, val):
        node = self.contains_value(val)
        if not node:
            return []
        parent = node.parent
        if not parent:
            return []
        return [child.value for child in parent.children if child != node]


def print_heap(heap):
    if heap.root is None:
        print("Heap is empty")
        return
    queue = [(heap.root, 0)]
    current_rank = 0
    while queue:
        node, rank = queue.pop(0)
        if rank > current_rank:
            current_rank = rank
            print()
        print(node.value, end=' ')
        for child in node.children:
            queue.append((child, rank + 1))
        if node.next:
            print('|', end=' ')
            queue.append((node.next, rank))
    print()


heap = RankPairingHeap()

heap.insert(5)
heap.insert(3)
heap.insert(7)
heap.insert(1)
heap.insert(9)
heap.insert(8)
heap.insert(2)
heap.insert(11)
heap.insert(12)

print_heap(heap)

while True:
    print("Select an option number. Press 0 to exit.")
    print("1. Insert node")
    print("2. Check if a node is in the heap")
    print("3. Delete min")
    print("4. Print heap")
    print("5. Print min value")
    print("6. Print the sibling of a given node")
    print(("7. Print heap on levels"))

    opt = int(input())

    if opt == 0:
        break
    elif opt == 1:
        print("Insert value")
        val = int(input())
        if heap.contains_value(val):
            print("The heap cannot contain duplicate nodes. Try again.")
        else:
            heap.insert(val)
        print()
    elif opt == 2:
        print("Enter node to check if it already is in the heap:")
        val = int(input())
        if heap.contains_value(val) != None:
            print("Node is already in heap")
        else: print("Node is not in heap")
        print()
    elif opt == 3:
        print("Deleted min node")
        heap.delete_min()
        print_heap(heap)
    elif opt == 4:
        heap.printHeap()
    elif opt == 5:
        print("The min value in this heap is:")
        print(heap.get_min())
        print()
    elif opt == 6:
        print("Enter node to find siblings: ")
        val = int(input())
        print("The sibling of the entered node are: ")
        print(heap.get_siblings(val))
    elif opt == 7:
        print_heap(heap)

    else:
        print("No such option")
