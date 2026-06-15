from algorithms.graph_builder import GraphBuilder
from algorithms.astar import AStar

graph = GraphBuilder.build_graph(
    rows=3,
    cols=3
)

free_slots = [
    "B2",
    "C3"
]

result = AStar.search(
    graph,
    "A1",
    free_slots
)

print("\nA* RESULT\n")

print(
    "Goal Slot:",
    result["goal"]
)

print(
    "Path:",
    " -> ".join(
        result["path"]
    )
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