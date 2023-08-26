print("           192110488--subhash")
print("           9.Travellng sales man.")
from sys import maxsize
from itertools import permutations
V = 4

def travellingSalesmanProblem(graph, s):
    
	vertex = []                                                 # store all vertex apart from source vertex
	for i in range(V):
		if i != s:
			vertex.append(i)

	min_path = maxsize                                          # store minimum weight Hamiltonian Cycle
	next_permutation=permutations(vertex)
	for i in next_permutation:
		current_pathweight = 0                              # store current Path weight(cost)
		k = s                                               # compute current path weight
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]
		min_path = min(min_path, current_pathweight)        # update minimum
	return min_path


# Driver Code
if __name__ == "__main__":
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print("The shortest path is :")
	print(travellingSalesmanProblem(graph, s))
