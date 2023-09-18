import collections
from typing import List


class Node:
    def __init__(self, word=None, freq=0):
        self.word = word
        self.freq = freq
        self.left = None
        self.right = None


class RoboticCodeRepresentationGenerator:
    def __init__(self, issued_commands: List[str]):
        self.issued_commands = issued_commands
        self.root = self.build_tree()
        self.rcr_codes = self.generate_rcr_codes('')

    def get_rcr(self, command: str) -> str:
        return self.rcr_codes[command]

    def build_tree(self) -> Node:
        count_dict = collections.Counter(self.issued_commands)
        nodes = [Node(word, freq) for word, freq in count_dict.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            left_child = nodes.pop(0)
            right_child = nodes.pop(0)
            combined_node = Node(freq=left_child.freq + right_child.freq)
            combined_node.left = left_child
            combined_node.right = right_child
            nodes.append(combined_node)
        return nodes[0]

    def generate_rcr_codes(self, code: str) -> dict:
        codes = {}
        stack = [(self.root, code)]

        while stack:
            node, code = stack.pop()
            if node.word:
                codes[node.word] = code
            if node.left:
                stack.append((node.left, code + '0'))
            if node.right:
                stack.append((node.right, code + '1'))
        return codes
