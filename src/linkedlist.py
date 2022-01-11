class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data


class LinkedList:
    head: Node

    def __init__(self) -> None:
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
            return

        current_node = self.head

        while current_node.next:
            current_node = current_node.next
        current_node.next = node

    def __str__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __len__(self):
        if self.head is None:
            return 0

        node = self.head
        cnt = 1
        while node is not None:
            node = node.next
            cnt += 1

        return cnt
