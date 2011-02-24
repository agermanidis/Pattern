import os, sys; sys.path.append(os.path.join("..", "..", ".."))

from pattern.graph import Graph, CENTRALITY

# Simple Graph demonstration.

g = Graph()
for n in ("tree", "nest", "bird", "fly", "insect", "ant"):
    g.add_node(n)
    
g.add_edge("tree", "nest")
g.add_edge("nest", "bird")
g.add_edge("bird", "fly")
g.add_edge("fly", "insect")
g.add_edge("insect", "ant")
g.add_edge("ant", "tree")
g.add_edge("ant", "bird")

print g.shortest_path(g.node("tree"), g.node("fly"))
print g.shortest_path(g.node("nest"), g.node("ant"))
print

# Which nodes get the most traffic?
print g.sorted(order=CENTRALITY)