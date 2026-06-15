from algorithms.graph_builder import GraphBuilder
from algorithms.bfs import BFS

graph = GraphBuilder.build_graph(
    rows=3,
    cols=3
)

free_slots = [
    "B2",
    "C3"
]

result = BFS.search(
    graph,
    "A1",
    free_slots
)

print("\nBFS RESULT\n")

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
    "Nodes Expanded:",
    result["nodes_expanded"]
)

print(
    "Runtime:",
    result["runtime"]
)