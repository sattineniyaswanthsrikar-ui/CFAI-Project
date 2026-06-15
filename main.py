from models.vehicle import Vehicle
from models.parking_lot import ParkingLot
from storage.database import Database

from csp.solver import CSPSolver

from graph.parking_graph import ParkingGraph
from search.auto_router import AutoRouter

db = Database()

parking_lot = ParkingLot()

vehicles = []


# -------------------------
# Add Vehicle
# -------------------------

def add_vehicle():

    vehicle_id = input("Vehicle ID: ")

    length = float(input("Length: "))

    width = float(input("Width: "))

    print("\n1. Normal")
    print("2. VIP")
    print("3. Emergency")

    choice = input("Priority: ")

    priorities = {
        "1": "Normal",
        "2": "VIP",
        "3": "Emergency"
    }

    priority = priorities.get(
        choice,
        "Normal"
    )

    vehicle = Vehicle(
        vehicle_id,
        length,
        width,
        priority
    )

    vehicles.append(vehicle)

    db.add_vehicle(
        vehicle_id,
        length,
        width,
        priority
    )

    print(
        "\nVehicle Added Successfully\n"
    )


# -------------------------
# Create Parking Area
# -------------------------

def create_parking():

    rows = int(
        input("Rows: ")
    )

    cols = int(
        input("Columns: ")
    )

    parking_lot.create_lot(
        rows,
        cols
    )

    print(
        "\nParking Area Created\n"
    )


# -------------------------
# View Vehicles
# -------------------------

def view_vehicles():

    data = db.view_vehicles()

    print(
        "\nREGISTERED VEHICLES\n"
    )

    for row in data:

        print(row)


# -------------------------
# View History
# -------------------------

def view_history():

    data = db.view_history()

    print(
        "\nALLOCATION HISTORY\n"
    )

    for row in data:

        print(row)


# -------------------------
# Allocate Parking
# -------------------------

def allocate_parking():

    if len(vehicles) == 0:

        print(
            "\nNo vehicles registered.\n"
        )

        return

    solver = CSPSolver(
        vehicles,
        parking_lot.slots
    )

    result = solver.solve()

    if result is None:

        return

    print(
        "\nALLOCATED PARKING SLOTS\n"
    )

    for vehicle_id, slot_id in result.items():

        parking_lot.allocate_slot(
            vehicle_id,
            slot_id
        )

        db.add_history(
            vehicle_id,
            slot_id
        )

        print(
            f"{vehicle_id} -> {slot_id}"
        )


# -------------------------
# Find Best Route
# -------------------------

def find_best_route():

    occupied = []

    for slot_id, slot in parking_lot.slots.items():

        if slot["occupied"]:

            occupied.append(
                (
                    slot_id,
                    slot["vehicle"]
                )
            )

    if len(occupied) == 0:

        print(
            "\nNo allocated vehicles.\n"
        )

        return

    print(
        "\nALLOCATED VEHICLES\n"
    )

    for i, item in enumerate(
            occupied,
            start=1):

        print(
            f"{i}. {item[1]} -> {item[0]}"
        )

    choice = int(
        input(
            "\nChoose Vehicle: "
        )
    )

    destination = occupied[
        choice - 1
    ][0]

    AutoRouter.find_route(
        parking_lot,
        destination
    )


# -------------------------
# Remove Vehicle
# -------------------------

def remove_vehicle():

    vehicle_id = input(
        "\nEnter Vehicle ID: "
    )

    db.remove_vehicle(
        vehicle_id
    )

    global vehicles

    vehicles = [

        v

        for v in vehicles

        if v.vehicle_id != vehicle_id

    ]

    for slot in parking_lot.slots.values():

        if slot["vehicle"] == vehicle_id:

            slot["occupied"] = False

            slot["vehicle"] = None


# -------------------------
# Reset Parking Area
# -------------------------

def reset_parking():

    confirm = input(
        "\nReset Entire Parking Area? (Y/N): "
    )

    if confirm.upper() != "Y":

        return

    parking_lot.slots.clear()

    parking_lot.rows = 0

    parking_lot.cols = 0

    vehicles.clear()

    db.reset_database()

    print(
        "\nParking Area Reset Successfully\n"
    )


# -------------------------
# Main Menu
# -------------------------

while True:

    print("\n" + "=" * 60)
    print("SMART PARKING AI AGENT")
    print("=" * 60)

    print("1. Create Parking Area")
    print("2. Add Vehicle")
    print("3. View Vehicles")
    print("4. Allocate Parking (CSP)")
    print("5. Show Parking Map")
    print("6. Visual Parking Layout")
    print("7. Show Parking Graph")
    print("8. Find Best Route")
    print("9. View History")
    print("10. Remove Vehicle")
    print("11. Reset Parking Area")
    print("0. Exit")

    choice = input(
        "\nEnter Choice: "
    )

    if choice == "1":

        create_parking()

    elif choice == "2":

        add_vehicle()

    elif choice == "3":

        view_vehicles()

    elif choice == "4":

        allocate_parking()

    elif choice == "5":

        parking_lot.display()

    elif choice == "6":

        parking_lot.visualize()

    elif choice == "7":

        ParkingGraph.display(
            parking_lot
        )

    elif choice == "8":

        find_best_route()

    elif choice == "9":

        view_history()

    elif choice == "10":

        remove_vehicle()

    elif choice == "11":

        reset_parking()

    elif choice == "0":

        print(
            "\nExiting...\n"
        )

        break

    else:

        print(
            "\nInvalid Choice\n"
        )