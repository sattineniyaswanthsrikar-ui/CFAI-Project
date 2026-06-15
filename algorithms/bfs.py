from collections import deque
import time


class BFS:

    @staticmethod
    def search(graph, start, goals):

        start_time = time.time()

        queue = deque()

        queue.append((start, [start]))

        visited = set()

        nodes_expanded = 0

        while queue:

            current, path = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            nodes_expanded += 1

            if current in goals:

                runtime = (
                    time.time() - start_time
                )

                return {
                    "path": path,
                    "goal": current,
                    "nodes_expanded": nodes_expanded,
                    "runtime": runtime
                }

            for neighbor in graph[current]:

                if neighbor not in visited:

                    queue.append(
                        (
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None