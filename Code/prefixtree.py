#!python3

from prefixtreenode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        return self.size == 0

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        node = self.root

        for i in string:
            if node.has_child(i):   # if the node has this as a child
                child = node.get_child(i)     # let's store it in the child var
                node = child                  # set the node as that child
            else:
                return node.is_terminal()      # else, it doesn't contain it
        return node.is_terminal()
                

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        # TODO

        current = self.root          # always begin with creating a variable called current and set it to the root
        for i in range(len(string)):       #  then traverse through the string to check if an element is in the string or not
            if not current.has_child(string[i]):    # if current does not have children
                new_node = PrefixTreeNode(string[i])          # then insert new node with current character in string, create a new node 
                current.add_child(string[i], new_node)        # add it as a child of a node
            current = current.get_child(string[i])    # if there is a child, the child is the letter of the string so current = that child

        current.terminal = True   # when I am at the end of the string(word), I want to make the last character terminal

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:      # if the string is zero
            return self.root, 0      # return the root and zero

        # Start with the root node
        node = self.root
        depth = 0

        for char in string:     # for every character in the string
            if node.has_child(char):      # if the node has the character in its children
                node = node.get_child(char)      # reassign the node to the next child
                depth += 1      # continue traversing and increasing the depth
        return node, depth    # return the node and its index

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []

        node = self._find_node(prefix)[0]     # finds prefix node (first item)

        if node == None:    # if the root doesn't have any children
            return completions     # then return the empty list
        
        if node.terminal == True:    # if the node terminates a string
            completions.append(node)    # append to the list
        else:           # if there are more terminal nodes (more children)
            for child in node.children:      # for every node character (loop over all of the children)
                # get it's children, traverse through and continue searching for more while adding on to the prefix
                self._traverse(child, prefix+child.character, completions.append)
        return completions

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []

        self._traverse(self.root, '', all_strings.append)    # begin with root node, empty prefix, then append 
        return all_strings


    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        if node.is_terminal():     # if the node is at the end
            visit(prefix)          # call visit on the prefix which appends when traverse is called

        if len(node.children) > 0:    # for child nodes including terminal and rest of the children
            for child in node.children:     # for every child in that node's children list
                self._traverse(child, prefix+child.character , visit)     # get its children, recursively call the function until terminal or no children while adding on to the prefix
        

def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


def main():
    # Simpe test case of string with partial substring overlaps
    strings = ['ABC', 'ABD', 'A', 'XYZ']
    create_prefix_tree(strings)

    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
        if len(tongue_twisters) > 1:
            print('\n' + '='*80 + '\n')


if __name__ == '__main__':
    main()
