class GraphBuilder:

    @staticmethod
    def build_graph(rows, cols):

        graph = {}

        for r in range(rows):

            row_char = chr(65 + r)

            for c in range(1, cols + 1):

                node = f"{row_char}{c}"

                graph[node] = []

                # UP
                if r > 0:
                    up = f"{chr(65 + r - 1)}{c}"
                    graph[node].append(up)

                # DOWN
                if r < rows - 1:
                    down = f"{chr(65 + r + 1)}{c}"
                    graph[node].append(down)

                # LEFT
                if c > 1:
                    left = f"{row_char}{c - 1}"
                    graph[node].append(left)

                # RIGHT
                if c < cols:
                    right = f"{row_char}{c + 1}"
                    graph[node].append(right)

        return graph