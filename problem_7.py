# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, urlSegment, handler = None):
        # Insert the node as before
        self.children[urlSegment] = RouteTrieNode(handler)
        return self.children[urlSegment]

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, urlSegments, handler = None, currentNode = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        if currentNode is None:
            currentNode = self.root

        segment = urlSegments[0]
        if segment in currentNode.children:
            currentNode = currentNode.children[segment]
        else:
            if len(urlSegments) == 1:
                currentNode.insert(segment, handler)
            else:
                currentNode = currentNode.insert(segment)

        if len(urlSegments) > 1:
            self.insert(urlSegments[1:], handler, currentNode)

    def find(self, urlSegments):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        currentNode = self.root

        for index in range(len(urlSegments)):
            segment = urlSegments[index]
            if segment in currentNode.children:
                currentNode = currentNode.children[segment]
            else:
                return None
        
        return currentNode.handler

class Router:
    def __init__(self, rootHandler = None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie = RouteTrie(rootHandler)

    def add_handler(self, url, handler = None):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(url), handler)

    def lookup(self, url):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        return self.trie.find(self.split_path(url))


    def split_path(self, url):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions,
        # so it should be placed in a function here
        newUrl = ''
        if url == '/' or url == '':
            return []
        else:
            newUrl = url.split('/')

        if newUrl[0] == '' and newUrl[-1] == '':
            return newUrl[1:-1]
        elif newUrl [0] == '' and newUrl[-1] != '':
            return newUrl[1:]
        elif newUrl [0] != '' and newUrl[-1] == '':
            return newUrl[:-1]

        return newUrl

router = Router("root handler")

router.add_handler("/home/explore/", "Explore handler")
router.add_handler("/home/about", "About handler")
router.add_handler("/help/chat", "Chat handler")
router.add_handler("/help/forum", "Forum handler")

print(router.lookup(""))
print(router.lookup("/"))
print(router.lookup("/home/about"))
print(router.lookup("/home/chat"))
print(router.lookup("/help/chat/test"))
print(router.lookup("/help/chat"))
print(router.lookup("help/forum/"))