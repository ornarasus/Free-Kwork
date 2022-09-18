class Node:
    name: str | int
    children: list

    def __init__(self, name: str | int):
        self.name = name
        self.children = list()


class Tree:
    nodes: list[Node]

    def __init__(self, nodes: list):
        self.nodes = [Node(nodes[0])]
        i = 0
        for n in nodes[1:]:
            node = Node(n)
            self.nodes.append(node)
            self.nodes[i].children.append(node)
            if len(self.nodes[i].children) == 2:
                i += 1

    def toList(self) -> list[int | str]:
        lst = [self.nodes[0].name]
        nodes: list[Node] = list(self.nodes[0].children)
        for node in nodes:
            if node is None:
                continue
            lst.append(node.name)
            nodes.extend(node.children)
        return lst

    def getNode(self, name: int | str) -> Node:
        for node in self.nodes:
            if node.name == name:
                return node
        raise KeyError

    def getParent(self, node: Node) -> (Node, int):
        for _node in self.nodes:
            if node in _node.children:
                return _node, _node.children.index(node)
        raise KeyError

    def replace(self, nameNode1: int | str, nameNode2: int | str):
        nodes: list[Node] = [self.getNode(nameNode1), self.getNode(nameNode2)]
        nodes.sort(key=lambda node: self.nodes.index(node))
        parentNodeMin, indexMin = self.getParent(nodes[0])
        parentNodeMax, indexMax = self.getParent(nodes[1])
        parentNodeMax.children[indexMax] = None
        parentNodeMin.children[indexMin] = nodes[1]
        if parentNodeMax == nodes[0]:
            parentNodeMax = nodes[1]
        if len(parentNodeMax.children) < 2:
            parentNodeMax.children.append(nodes[0])
        else:
            parentNodeMax.children[indexMax] = nodes[0]


if __name__ == "__main__":
    tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    tree.replace(5, 2)
    print(tree.toList())