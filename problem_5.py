class Node:
    def __init__(self, char = "", isRoot = False, isWord = False):
        self.children = {}
        self.char = char
        self.isWord = isWord

    def insert(self, char, isWord = False):
        if char not in self.children:
            self.children[char] = Node(char)


    def suffixes(self, word = "", suffixes = [], newCall = True):
        if newCall:
            suffixes = []

        for key in self.children:
            node = self.children[key]
            if node.isWord:
                suffixes.append(word + key)
            if node.children:
                node.suffixes(word + key, suffixes, False)
    
        return suffixes
    

class Trie:
    def __init__(self):
        self.root = Node("", True)

    def insert(self, word):
        currentNode = self.root
        
        for char in word:
            currentNode.insert(char)
            currentNode = currentNode.children[char]

        currentNode.isWord = True

                
    def find(self, prefix = ""):
        currentNode = self.root 

        for char in prefix:
            if char not in currentNode.children:
                return Node()
            else:
                currentNode = currentNode.children[char]

        return currentNode


trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]

for word in wordList:
    trie.insert(word)

# print(trie.find('antagonist'))
print(trie.find('antagonist').suffixes())
print(trie.find('fun').suffixes())
print(trie.find('ant').suffixes())
print(trie.find('t').suffixes())
print(trie.find('').suffixes())