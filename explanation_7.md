# HTTPRouter using a Trie

- Given an URL, the algorithm creates a node for each route in the link that may, or may not, have a handler
- `RouteTrieNode` has an `insert()` method with a time complexity of O(1) and a space complexity of O(n) where n is the length of the URL
- `RouteTrie`: `insert()` has a time and space complexity of O(n) where n is the length of the URL; `find()` has a space complexity of O(1) and a time complexity of O(m*n) where m is the depth of the tree and n is the length of the URL
- `Router`: `add_handler()` has a time and space complexity of O(n) where n is the length of the URL; `lookup()` has the same efficiency as `RouteTrie.find()`; `split_path()` has a space and time complexity of O(n) where n is the length of the URL
