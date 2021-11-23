import igraph as ig
import matplotlib.pyplot as plt

g = ig.Graph(
    9,
    [(0, 5), (1, 6), (1, 7), (2, 5), (2, 8), (3, 6), (4, 5), (4, 6)]
)

# Assign nodes 0-4 to one side, and the nodes 5-8 to the other side
for i in range(5):
    g.vs[i]["type"] = True
for i in range(5, 9):
    g.vs[i]["type"] = False


matching = g.maximum_bipartite_matching()

# Print pairings for each node on one side
matching_size = 0
print("Matching is:")
for i in range(5):
    print(f"{i} - {matching.match_of(i)}")
    if matching.match_of(i):
        matching_size += 1
print("Size of Maximum Matching is:", matching_size)

fig, ax = plt.subplots(figsize=(7, 3))
ig.plot(
    g,
    target=ax,
    layout=g.layout_bipartite(),
    vertex_size=0.4,
    vertex_label=range(g.vcount()),
    vertex_color="lightblue",
    edge_width=[2.5 if e.target==matching.match_of(e.source) else 1.0 for e in g.es]
)
plt.show()

# Matching is:
# 0 - 5
# 1 - 7
# 2 - 8
# 3 - None
# 4 - 6
# Size of Maximum Matching is: 4
