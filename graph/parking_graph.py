class ParkingGraph:

    @staticmethod
    def display(parking_lot):

        print("\n")
        print("=" * 60)
        print("PARKING GRAPH")
        print("=" * 60)

        for r in range(parking_lot.rows):

            row_char = chr(65 + r)

            row_nodes = []

            for c in range(
                    1,
                    parking_lot.cols + 1):

                row_nodes.append(
                    f"{row_char}{c}"
                )

            print(
                " --- ".join(
                    row_nodes
                )
            )

            if r != parking_lot.rows - 1:

                print("|")
                print("|")

        print()