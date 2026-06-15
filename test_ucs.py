from algorithms.graph_builder import GraphBuilder
from algorithms.ucs import UCS

graph = GraphBuilder.build_graph(
    rows=3,
    cols=3
)

free_slots = [
    "B2",
    "C3"
]

result = UCS.search(
    graph,
    "A1",
    free_slots
)

print("\nUCS RESULT\n")

print("Goal Slot:", result["goal"])

print(
    "Path:",
    " -> ".join(result["path"])
)

print(
    "Cost:",
    result["cost"]
)

print(
    "Nodes Expanded:",
    result["nodes_expanded"]
)

print(
    "Runtime:",
    result["runtime"]
)