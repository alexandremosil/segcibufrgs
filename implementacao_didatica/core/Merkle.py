""" Adaptado de https://www.codementor.io/blog/merkle-trees-5h9arzd3n8 """

from hashlib import sha256


class Node:
    def __init__(self, hash):
        self.hash = hash
        self.parent = None


class Tree:
    def __init__(self, data_chunks):
        leaves = []

        for chunk in data_chunks:
            node = Node(self.compute_hash(chunk))
            leaves.append(node)

        self.root = self.build_merkle_tree(leaves)

    def build_merkle_tree(self, leaves):
        num_leaves = len(leaves)
        if num_leaves == 1:
            return leaves[0]

        parents = []

        i = 0
        while i < num_leaves:
            left_child = leaves[i]
            right_child = leaves[i + 1] if i + 1 < num_leaves else left_child
            parents.append(self.create_parent(left_child, right_child))

            i += 2

        return self.build_merkle_tree(parents)

    def create_parent(self, left_child, right_child):
        parent = Node(
            self.compute_hash(left_child.hash + right_child.hash))
        left_child.parent, right_child.parent = parent, parent

        print("Esquerda: {}\nDireita: {}\nSuperior: {}\n".format(
            left_child.hash, right_child.hash, parent.hash))
        return parent

    @staticmethod
    def compute_hash(data):
        return sha256(str(data).encode()).hexdigest()
