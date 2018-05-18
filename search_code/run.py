# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ap = search.GPSProblem('A', 'P', search.romania)
av = search.GPSProblem('A', 'V', search.romania)
ag = search.GPSProblem('A', 'G', search.romania)


print search.graph_searchRA(ab).path()

print search.graph_searchRAS(ab).path()

print search.graph_searchRA(ap).path()

print search.graph_searchRAS(ap).path()

print search.graph_searchRA(av).path()

print search.graph_searchRAS(av).path()

print search.graph_searchRA(ag).path()

print search.graph_searchRAS(ag).path()


# print ab.h(search.Node(ab.initial))

#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
