## Node creation

class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


# modified verison of the iteration
def node_iteration(root_node):
    output = []
    # if empty then root is not None
    if root_node is None:
        return None

    if root_node.next is None:
        output.append(root_node.data)
    else:
        # O(n)
        while root_node is not None:
            output.append(root_node.data)
            root_node = root_node.next

    return output


# finding the element in the linked list
def iterate_for_target(root_node, target):
    if root_node is None:
        return False
    if root_node.next is None:
        if root_node.data == target:
            return True
    else:
        # Time complexity is Big-O(n)
        while root_node is not None:
            if root_node.data == target:
                return True
            root_node = root_node.next

    return False


# add the node at the begining of the linked list
def add_node_begin(root_node, new_data):
    new_node = Node(new_data)
    new_node.next, root_node = root_node, new_node
    return root_node

# add the node at the end of the linked list
def add_node_end(root_node, new_data):
    head = root_node
    new_node = Node(new_data)
    while root_node.next is not None:
        root_node = root_node.next
    root_node.next = new_node

    return head


# add the node based on the input position
def add_node_position(root_node, new_node, pos):
    count, head = 0, root_node
    head = root_node
    while root_node.next is not None:
        if pos == count:
            break
        prev_node = root_node
        root_node = root_node.next
        count += 1
    new_node = Node(new_node)
    new_node.next, prev_node.next = root_node, new_node

    return head




# Linked List creation
root = None
root = Node(10)
root.next = Node(11)
root.next.next = Node(12)
root.next.next = Node(13)
root.next.next.next = Node(14)
# Print iteration
print(node_iteration(root))

# find the target element 15
print(iterate_for_target(root, 11))

# add node
new_root = add_node_begin(root, 5)
# Print iteration
print(node_iteration(new_root))

# add node at the end
new_root = add_node_end(new_root, 16)
print(node_iteration(new_root))


# add node in the middle based on the position
new_root = add_node_position(new_root, 12, 3)
print(node_iteration(new_root))

# add node in the middle based on the position
new_root = add_node_position(new_root, 120, 3)
print(node_iteration(new_root))