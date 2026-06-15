import heapq
import time


class UCS:

    @staticmethod
    def search(graph, start, goals):

        start_time = time.time()

        pq = []

        heapq.heappush(
            pq,
            (0, start, [start])
        )

        visited = set()

        nodes_expanded = 0

        while pq:

            cost, current, path = heapq.heappop(pq)

            if current in visited:
                continue

            visited.add(current)

            nodes_expanded += 1

            if current in goals:

                runtime = (
                    time.time() - start_time
                )

                return {
                    "goal": current,
                    "path": path,
                    "cost": cost,
                    "nodes_expanded": nodes_expanded,
                    "runtime": runtime
                }

            for neighbor in graph[current]:

                if neighbor not in visited:

                    heapq.heappush(
                        pq,
                        (
                            cost + 1,
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None