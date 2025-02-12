class SuffixTreeNode(object):
    def __init__(self, start=-1, end=None):
        self.start = start
        self.end = end
        self.edges = {}
        self.suffix_link = None
        print(self)

    def __repr__(self):
        return "SuffixTreeNode(%s, %s)" % (self.start, self.end)
    
    def edge_length(self, current_end):
        if self.end is None:
            return current_end - self.start + 1
        else:
            return self.end - self.start + 1
        

class SuffixTree(object):
    def __init__(self, string):
        # add a terminal character ("$") to the string
        self.string = string + "$"
        # create a root node
        self.root = SuffixTreeNode()
        # set the active node to the root
        self.active_node = self.root
        # set the active edge to -1 (-1 indicates that there is no active edge)
        self.active_edge = -1
        # set the active length to 0 (tree is empty)
        self.active_length = 0
        # set the remainder to 0 (remainder is the number of suffixes yet to be added)
        self.remainder = 0
        # set the end of the current phase to -1 (no phase has started yet)
        self.end = -1
        # set the last created internal node to None (no internal node has been created yet)
        self.last_created_internal_node = None

    def build(self):
        # loop through the string and add each suffix to the tree
        for i in range(len(self.string)):
            print(f"-------- Adding suffix {self.string[i]} -------- ")
            self.add_to_tree(i)
            print(f"-------- After adding suffix {self.string[i]} -------- ")
            self.print_tree(self.root, 0)
            print("\n\n\n\n\n")

    def add_to_tree(self, i):
        # set the end of the current phase to the current index
        self.end = i
        # increment the remainder (since we are adding a new suffix) 
        self.remainder += 1
        # set the last created internal node to None (since we are starting a new phase)
        self.last_created_internal_node = None

        # loop through the remainder (the number of suffixes yet to be added)
        while self.remainder > 0:
            # if the active length is 0, set the active edge to the current index
            if self.active_length == 0:
                self.active_edge = i

            # edge_car is the character in the string that corresponds to the active edge
            edge_char = self.string[self.active_edge]
            # if the active edge is not in the active node's edges, create a new edge
            if edge_char not in self.active_node.edges:
                # Rule 2: create a new leaf node and add it to the active node
                # create a new leaf node
                leaf_node = SuffixTreeNode(i)
                # add the new edge to the active node
                self.active_node.edges[edge_char] = leaf_node
                # if an internal node was created in the last phase, set its suffix link to the active node
                if self.last_created_internal_node:
                    # set the suffix link of the last created internal node to the active node
                    self.last_created_internal_node.suffix_link = self.active_node
                    self.last_created_internal_node = None

            else:
                # Follow the edge corresponding to the active edge
                next_node = self.active_node.edges[edge_char]
                # get the length of the edge
                length = next_node.edge_length(self.end)
                print(f"Edge Length: {length}, Active Length: {self.active_length}")
                print(next_node)
                # if the active length is greater than the length of the edge, move to the next node
                if self.active_length >= length:
                    self.active_edge += length
                    self.active_length -= length
                    self.active_node = next_node
                    continue
                
                # Rule 3: if the character at the end of the edge is the same as the character at the current index then increment the active length
                if self.string[next_node.start + self.active_length] == self.string[i]:
                    self.active_length += 1
                    # if an internal node was created in the last phase, set its suffix link to the active node
                    if self.last_created_internal_node:
                        # set the suffix link of the last created internal node to the active node
                        self.last_created_internal_node.suffix_link = self.active_node
                        self.last_created_internal_node = None
                    break

                # Rule 2: create a new internal node and add it to the active node
                # create a new internal node
                print(f"Active Node: {self.active_node}, Edge Char: {edge_char}")
                split_node = SuffixTreeNode(next_node.start, next_node.start + self.active_length - 1)
                self.active_node.edges[edge_char] = split_node
                # create a new leaf node
                leaf_node = SuffixTreeNode(i)
                split_node.edges[self.string[i]] = leaf_node
                # add the existing edge to the split node
                next_node.start += self.active_length
                split_node.edges[self.string[next_node.start]] = next_node
                # if an internal node was created in the last phase, set its suffix link to the split node
                if self.last_created_internal_node:
                    self.last_created_internal_node.suffix_link = split_node

                # set the last created internal node to the split node
                self.last_created_internal_node = split_node
            
            # decrement the remainder (since we added a suffix)
            self.remainder -= 1

            # if the active node is not the root, follow the suffix link else decrement the active length
            if self.active_node == self.root and self.active_length > 0:
                self.active_length -= 1
                self.active_edge = i - self.remainder + 1
            elif self.active_node != self.root:
                self.active_node = self.active_node.suffix_link
        
    def print_tree(self, node=None, depth=0):
        if not node:
            node = self.root
        if depth == 0:
            print(f"Tree Values: End {self.end}, Active Edge {self.active_edge}, Active Length {self.active_length}, Remainder {self.remainder}")
        for char, child in node.edges.items():
            edge_string= self.string[child.start:child.end+1 if child.end else None]
            print("  " * depth + f"{char}: ({edge_string})")
            self.print_tree(child, depth + 1)


# Usage
if __name__ == '__main__':
    string = "banana"
    suffix_tree = SuffixTree(string)
    suffix_tree.build()
    suffix_tree.print_tree()
            


    
