class Node:
    def __init__(self, char=None, freq=None):
        self.char = char  
        self.freq = freq  
        self.left = None  
        self.right = None  
def decode_huff(root, s):
    decoded_string = []
    current = root  
    
    for bit in s:
        if bit == '0':
            current = current.left  
        else:
            current = current.right  
        if current.left is None and current.right is None:
            decoded_string.append(current.char)
            current = root  
            
    return ''.join(decoded_string)

root = Node()
root.left = Node('B')
root.right = Node('A')
root.right.left = Node('R')
root.right.right = Node()
root.right.right.left = Node('C')
root.right.right.right = Node('D')

s = "1001011"
decoded_result = decode_huff(root, s)
print(decoded_result)  
