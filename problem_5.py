class Node:
    def __init__(self, wordEnd = False):
        self.wordEnd = wordEnd
        self.dict = {}

    def insert(self, char):
        if char not in self.dict:
            self.dict[char] = Node()


    def suffixes(self, suffix = ''):
        out = []
        
        for k in self.dict:
            if self.dict[k].wordEnd:
                out.append(suffix + k)
            out += self.dict[k].suffixes(suffix + k)
        
        return out
    

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cNode = self.root
        for char in word:
            cNode.insert(char)
            cNode = cNode.dict[char]
        cNode.wordEnd = True
                

    def find(self, prefix):
        cNode = self.root
        for char in prefix:
            if char in cNode.dict:
                cNode = cNode.dict[char]
            else:
                return Node()
        return cNode


trie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    trie.insert(word)



print(trie.find('antagonist').suffixes())
print(trie.find('fun').suffixes())
print(trie.find('ant').suffixes())
print(trie.find('t').suffixes())
print(trie.find('').suffixes())