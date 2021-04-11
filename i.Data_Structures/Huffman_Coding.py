# importing priority queue data structure
import heapq
import sys

class Huff_Node:
    def __init__(self,value,freq):
        self.value=value
        self.freq=freq
        self.left=None
        self.right=None

    def __lt__(self, other):
        return self.freq < other.freq

    def __str__(self):
        return str(self.value)+","+str(self.freq)

"""
    Below function returns the sorted list of Huffnodes
"""
def get_sortedhuffnodelist(input_str):
    dict_freq={}
    for char in input_str:
        if char not in dict_freq:
            dict_freq[char]=1
        else:
            dict_freq[char]+=1
    # Now create a sorted key, value tuples from above dictionary using freq
    sorted_list=sorted(dict_freq.items(),key=lambda kv:kv[1])
    return [Huff_Node(each[0],each[1]) for each in sorted_list]

"""
    Below function takes the sorted tuples list and return a huffman tree 
    heapify from heapq module is used to create a heap from input list
"""
def huffmantree(input_str):
    heap=get_sortedhuffnodelist(input_str)
    heapq.heapify(heap) # this function transforms old list into a heap
    while len(heap) > 1:
        initnode=Huff_Node(None,None)
        leftnode=heapq.heappop(heap) # method removes the smallest in the heap
        rightnode=heapq.heappop(heap) # method removes next lowest in the heap
        initnode.left=leftnode
        initnode.right=rightnode
        initnode.freq=rightnode.freq+leftnode.freq
        heapq.heappush(heap,initnode)
    return heap

"""
    Below function takes the root node and traverses through the child nodes and returns a dictionary
    with node value and the huffman code at each node
    D		000
    B		001
    E		01
    A		10
    C		11
"""
def huffcode_table(root):
    dict_code = {}

    def getcode(hnode, currentcode=""):
        if hnode is None:
            return
        if hnode.left is None and hnode.right is None:
            dict_code[hnode.value] = currentcode
        getcode(hnode.left, currentcode + "0")
        getcode(hnode.right, currentcode + "1")
    getcode(root[0])
    return dict_code
"""
Below function encodes the input string into a binary code
"""
def huffman_encode(inp_str):
    if (len(get_sortedhuffnodelist(inp_str))) == 1: #check if there is only one char in given string
        return "0" * len(inp_str)
    huff_code = ""
    root = huffmantree(inp_str)  #heap from the given string
    hufftable = huffcode_table(root)
    for item in inp_str:
        huff_code += hufftable[item]
    return huff_code


def huffman_decode(bin_str, root):  # bit string and root a heap containg the Huffman Tree Root

    if (len(get_sortedhuffnodelist(bin_str))) == 1:
        return len(bin_str) * str(root.value)
    decode = ""
    n = len(bin_str)
    count = 0
    while count < n:
        current = root[0]
        while current.left is not None and current.right is not None:
            if bin_str[count] == "0":
                current = current.left
            else:
                current = current.right
            count += 1
        decode += current.value
    return decode

# returns encoded data and root of the heap
def huffman_encoding(inp_str):
    return huffman_encode(inp_str), huffmantree(inp_str)


# returns decoded Huffman code
def huffman_decoding(bin_str, root):
    return huffman_decode(bin_str, root)


"""
Test harnesss code, special cases are for data =: None, "", and single frequency data
eg. "a", "aa", "aaa", etc.
"""


def test_huffman(inp_str):
    if inp_str is None:
        print("***************************************************************")
        print(None)
    elif inp_str == "":
        print("***************************************************************")
        print("Empty String")
    # single frequency data

    elif len(get_sortedhuffnodelist(inp_str)) == 1:
        print("***************************************************************")
        code = "0" * len(inp_str)
        print("The size of the data is: {}\n".format(sys.getsizeof(inp_str)))
        print("The content of the data is: {}\n".format(inp_str))
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(code, base=2))))
        print("The content of the encoded data is: {}\n".format(code))
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(inp_str)))
    else:
        print("***************************************************************")
        print("The size of the data is: {}\n".format(sys.getsizeof(inp_str)))
        print("The content of the data is: {}\n".format(inp_str))
        encoded_data, tree = huffman_encoding(inp_str)
        print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print("The content of the encoded data is: {}\n".format(encoded_data))
        decoded_data = huffman_decoding(encoded_data, tree)
        print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print("The content of the encoded data is: {}\n".format(decoded_data))


test_huffman(None)
test_huffman("")
test_huffman("a")
test_huffman("aa")
test_huffman("aaa")
test_huffman("aaaa")
test_huffman("ab")
test_huffman("abbb")
test_huffman("abc")
test_huffman("udacity")
test_huffman("huffman")
test_huffman("mississipi")
test_huffman("The bird is the word")
test_huffman("""When in the course of human events it becomes necessary 
for one people to dissolve the political bands which have connected
them with another and to assume among the powers of the earth, 
the separate and equal station to which the Laws of Nature and 
of Nature's God entitle them, a decent respect to the opinions 
of mankind requires that they should declare the causes which impel 
them to the separation.""")