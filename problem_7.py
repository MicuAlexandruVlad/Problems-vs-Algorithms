# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, urlSegment, handler = None):
        # Insert the node as before
        self.children[urlSegment] = RouteTrieNode(handler)

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, urlSegments, handler = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        currentNode = self.root

        for index in range(len(urlSegments)):
            segment = urlSegments[index]
            if segment in currentNode.children:
                print("RouteTrie -> insert: url segment in node chidlren")
                currentNode = currentNode.children[segment]
            else:
                if index == len(urlSegments) - 1:
                    print("RouteTrie -> insert: last url segment in list; inserting new node with handler")
                    currentNode.insert(segment, handler)
                    print("RouteTrie -> insert: inserted node with handler: ", currentNode.children[segment].handler)
                else:
                    print("RouteTrie -> insert: inserting new node and moving to it")
                    currentNode.insert(segment)
                    currentNode = currentNode.children[segment]

        # print(self.root.children)     
        # print(self.root.children["home"].children) 
        # print(currentNode.children)
        print(self.root)

    def find(self, urlSegments):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        currentNode = self.root

        # for index in range(len(urlSegments)):
        #     segment = urlSegments[index]
        #     if segment in currentNode.children:
        #         print("RouteTrie -> find: url segment in node chidlren")
        #         if index == len(urlSegments) - 1:
        #             print("RouteTrie -> find: last segment in list")
        #             return currentNode.children[segment].handler
        #         else:
        #             print("RouteTrie -> find: moving to new node")
        #             currentNode = currentNode.children[segment]
        #     else:
        #         break
        
        return self.root

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
        self.trie.find(self.split_path(url))


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

print(router.lookup("/"))
# print(router.lookup("/home/about"))