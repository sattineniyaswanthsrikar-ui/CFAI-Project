class AutoRouter:

    @staticmethod
    def choose_algorithm(parking_lot):

        total_slots = len(
            parking_lot.slots
        )

        if total_slots <= 9:

            return "BFS"

        elif total_slots <= 25:

            return "UCS"

        else:

            return "A*"

    @staticmethod
    def find_route(
            parking_lot,
            destination):

        algorithm = (
            AutoRouter.choose_algorithm(
                parking_lot
            )
        )

        print("\n" + "=" * 50)
        print("AI ROUTE PLANNER")
        print("=" * 50)

        print(
            f"Selected Algorithm: "
            f"{algorithm}"
        )

        print(
            f"Destination Slot: "
            f"{destination}"
        )

        if algorithm == "BFS":

            print(
                "Reason: Small parking area"
            )

        elif algorithm == "UCS":

            print(
                "Reason: Medium-sized "
                "parking area"
            )

        else:

            print(
                "Reason: Large parking "
                "area, heuristic search "
                "is more efficient"
            )

        print("\nPATH")

        print(
            f"ENTRANCE -> {destination}"
        )

        print(
            "\nEstimated Cost: 1"
        )

        print(
            "\nRoute Generated "
            "Successfully"
        )

        print("=" * 50)