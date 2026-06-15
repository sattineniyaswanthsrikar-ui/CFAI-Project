import heapq
import time


class AStar:

    @staticmethod
    def heuristic(node, goal):

        row1 = ord(node[0]) - 65
        col1 = int(node[1:])

        row2 = ord(goal[0]) - 65
        col2 = int(goal[1:])

        return abs(row1 - row2) + abs(col1 - col2)

    @staticmethod
    def search(graph, start, goals):

        start_time = time.time()

        best_goal = goals[0]

        pq = []

        heapq.heappush(
            pq,
            (
                0,
                0,
                start,
                [start]
            )
        )

        visited = set()

        nodes_expanded = 0

        while pq:

            f_cost, g_cost, current, path = heapq.heappop(pq)

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
                    "cost": g_cost,
                    "nodes_expanded": nodes_expanded,
                    "runtime": runtime
                }

            for neighbor in graph[current]:

                if neighbor not in visited:

                    g = g_cost + 1

                    h = AStar.heuristic(
                        neighbor,
                        best_goal
                    )

                    f = g + h

                    heapq.heappush(
                        pq,
                        (
                            f,
                            g,
                            neighbor,
                            path + [neighbor]
                        )
                    )

        return None