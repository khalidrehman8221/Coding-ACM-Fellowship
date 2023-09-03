"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        node_mapping = {}
        
        def dfs(original_node):
            clone_node = Node(original_node.val)
            node_mapping[original_node] = clone_node

            for neighbor in original_node.neighbors:
                if neighbor not in node_mapping:
                    clone_node.neighbors.append(dfs(neighbor))
                else:
                    clone_node.neighbors.append(node_mapping[neighbor])
            return clone_node
        
        return dfs(node)