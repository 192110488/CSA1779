print("         Breadth First Search..")
print("         192110488--subhash")
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A'],
    'C': ['A', 'D'],
    'D': ['A', 'C', 'E'],
    'E': ['D'],
}
def bfs(node):

    # mark vertices as False means not visited
    visited = [False] * (len(graph))

    # make an empty queue for bfs
    queue = []

    # mark gave node as visited and add it to the queue
    visited.append(node)
    queue.append(node)

    while queue:
        # Remove the front vertex or the vertex at the 0th index from the queue and print that vertex.
        v = queue.pop(0)
        print(v, end=" ")

        # Get all adjacent nodes of the removed node v from the graph hash table.
        # If an adjacent node has not been visited yet,
        # then mark it as visited and add it to the queue.
        for neigh in graph[v]:
            if neigh not in visited:
                visited.append(neigh)
                queue.append(neigh)


# Driver Code
print("The path is\n")
if __name__ == "__main__":
    bfs('A')
