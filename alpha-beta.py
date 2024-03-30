def minimax_alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or node.is_terminal():
        return node.evaluate()
    if maximizing_player:
        value = -float('inf')
        for move in node.get_possible_moves():
            value = max(value, minimax_alpha_beta(move, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float('inf')
        for move in node.get_possible_moves():
            value = min(value, minimax_alpha_beta(move, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if alpha >= beta:
                break
        return value
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def is_terminal(self):
        return len(self.children) == 0
    def evaluate(self):
        return self.value
    def get_possible_moves(self):
        return self.children
root = Node(1)
child1 = Node(7)
child2 = Node(2)
child3 = Node(8)
root.add_child(child1)
root.add_child(child2)
root.add_child(child3)
grandchild1 = Node(2)
grandchild2 = Node(7)
grandchild3 = Node(8)
child1.add_child(grandchild1)
child2.add_child(grandchild2)
child3.add_child(grandchild3)
grandchild1.add_child(Node(1))
grandchild1.add_child(Node(4))
grandchild2.add_child(Node(7))
grandchild2.add_child(Node(10))
grandchild3.add_child(Node(11))
grandchild3.add_child(Node(12))
optimal_value = minimax_alpha_beta(root, 3, -float('inf'), float('inf'), True)
print("Optimal value:", optimal_value)
