import time


class DFS:

    @staticmethod
    def search(graph, start, goals):

        start_time = time.time()

        stack = [(start, [start])]

        visited = set()

        nodes_expanded = 0

        while stack:

            current, path = stack.pop()

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

            for neighbor in reversed(graph[current]):

                if neighbor not in visited:

                    stack.append(
                        (
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None