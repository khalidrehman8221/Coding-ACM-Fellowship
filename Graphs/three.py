class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            # If there's only one node, it's the MHT root
            return [0]

        # Create an adjacency list representation of the tree
        adjacency = defaultdict(list)
        for u, v in edges:
            adjacency[u].append(v)
            adjacency[v].append(u)

        # Initialize a set of leaf nodes
        leaves = {node for node in adjacency if len(adjacency[node]) == 1}

        while n > 2:
            # Remove current leaf nodes
            new_leaves = set()
            for leaf in leaves:
                neighbor = adjacency[leaf][0]
                adjacency[neighbor].remove(leaf)
                if len(adjacency[neighbor]) == 1:
                    new_leaves.add(neighbor)
                n -= 1
            leaves = new_leaves

        # The remaining nodes in 'leaves' are the MHT roots
        return list(leaves)