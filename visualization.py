from tabulate import tabulate
import matplotlib.pyplot as plt


# --------------------------------
# Display Table
# --------------------------------

def display_solution(solution, vehicles, parking_slots):

    table = []

    for vehicle, slot in solution.items():

        table.append([

            vehicle,
            slot,
            vehicles[vehicle]["priority"],
            parking_slots[slot]["distance"]

        ])

    print("\nSMART PARKING ALLOCATION SYSTEM\n")

    print(tabulate(
        table,
        headers=[
            "Vehicle",
            "Allocated Slot",
            "Priority",
            "Distance"
        ],
        tablefmt="grid"
    ))


# --------------------------------
# Visualize Distance Graph
# --------------------------------

def plot_graph(solution, parking_slots):

    vehicles = list(solution.keys())

    distances = []

    for vehicle in vehicles:

        slot = solution[vehicle]

        distances.append(
            parking_slots[slot]["distance"]
        )

    plt.figure(figsize=(8, 5))

    plt.bar(vehicles, distances)

    plt.xlabel("Vehicles")

    plt.ylabel("Distance")

    plt.title("Parking Slot Distance Allocation")

    plt.show()