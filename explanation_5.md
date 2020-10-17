# Autocomplete with Tries

- Each trie `Node` has a `isWord` property (so we can determine whether or not we have reached a word), an `insert()` method, and a `suffixes()` method
- `insert()` creates a new node and adds it to the `children` dictionary if it is not stored in it already. It has a time and space complexity of O(1)
- `suffixes()` return an array of complete words that can form from the current `Node`. The time complexity and space complexity are O(m*n) where m is the depth of the tree and n is the number of words stored in the tree
- The `Trie` object has 2 methods `insert()` and `find()`
- `insert()` has a time and space complexity of O(n) where n is the number of characters in the word
- `find()` has a space complexity of O(1) and a time complexity of O(n) where n is the number of characters in the prefix

