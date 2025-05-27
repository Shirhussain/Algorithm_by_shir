# hacker rank problem:
# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem?isFullScreen=true

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


class HuffmanCoding:
    """
    Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies.
    More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords.

    Algorithm Details:
    - All edges along the path to a character contain a code digit
    - Left edges are labeled with 0, right edges with 1
    - Only leaves contain actual characters and their frequencies
    - Internal nodes contain NULL character and sum of descendant frequencies

    Example:
    For string "ABRACADABRA":
    - Frequency based encoding produces variable length codes:
        A - 0
        B - 111
        C - 1100
        D - 1101
        R - 10

    Encoded string example:
    "ABRACADABRA" -> "01111001100011010111100"

    Key Properties:
    - Prefix free encoding: No codeword appears as prefix of another
    - Decoding process: Follow 0s and 1s from root to leaf

    Implementation Details:
    - build_frequency_map: Creates frequency map of characters
    - build_tree: Constructs Huffman tree using frequency map
    - generate_codes: Creates encoding map by traversing tree
    - encode: Converts input text to binary string using encoding map
    - decode: Reconstructs original text from binary string using Huffman tree

    Constraints:
    - Input text must be non-empty
    - Characters must be from ASCII set

    Sample Usage:
    text = "ABACA"
    encoded = "1001011"
    decoded = "ABACA"
    """

    def __init__(self):
        self.encoding_map = {}

    def build_frequency_map(self, text):
        freq_map = {}
        for char in text:
            freq_map[char] = freq_map.get(char, 0) + 1
        return freq_map

    def build_tree(self, freq_map):
        nodes = [Node(char, freq) for char, freq in freq_map.items()]

        while len(nodes) > 1:
            nodes.sort(key=lambda x: x.freq)
            left = nodes.pop(0)
            right = nodes.pop(0)
            parent = Node(None, left.freq + right.freq)
            parent.left = left
            parent.right = right
            nodes.append(parent)

        return nodes[0]

    def generate_codes(self, node, code=""):
        if not node:
            return

        if node.char is not None:
            self.encoding_map[node.char] = code
            return

        self.generate_codes(node.left, code + "0")
        self.generate_codes(node.right, code + "1")

    def encode(self, text):
        return "".join(self.encoding_map[char] for char in text)

    def decode(self, encoded, root):
        decoded = ""
        current = root

        for bit in encoded:
            current = current.left if bit == "0" else current.right

            if current.char is not None:
                decoded += current.char
                current = root

        return decoded


# Example usage
if __name__ == "__main__":
    text = "Hello World"
    huffman = HuffmanCoding()
    freq_map = huffman.build_frequency_map(text)
    root = huffman.build_tree(freq_map)
    huffman.generate_codes(root)

    encoded = huffman.encode(text)
    print("Encoded:", encoded)
    decoded = huffman.decode(encoded, root)
    print("Decoded:", decoded)
