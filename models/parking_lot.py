class ParkingLot:

    def __init__(self):

        self.rows = 0
        self.cols = 0

        self.slots = {}

    # -------------------------
    # Create Parking Area
    # -------------------------

    def create_lot(
            self,
            rows,
            cols):

        self.rows = rows

        self.cols = cols

        self.slots = {}

        default_area = float(
            input(
                "\nDefault Slot Area: "
            )
        )

        for r in range(rows):

            row_char = chr(
                65 + r
            )

            for c in range(
                    1,
                    cols + 1):

                slot_id = (
                    f"{row_char}{c}"
                )

                self.slots[
                    slot_id
                ] = {

                    "area":
                    default_area,

                    "occupied":
                    False,

                    "vehicle":
                    None
                }

    # -------------------------
    # Allocate Slot
    # -------------------------

    def allocate_slot(
            self,
            vehicle_id,
            slot_id):

        self.slots[
            slot_id
        ]["occupied"] = True

        self.slots[
            slot_id
        ]["vehicle"] = vehicle_id

    # -------------------------
    # Console View
    # -------------------------

    def display(self):

        print("\n")
        print("=" * 60)
        print("SMART PARKING AREA")
        print("=" * 60)

        occupied = 0

        for slot_id, slot in self.slots.items():

            print(
                slot_id,
                " | Area:",
                slot["area"],
                " | Vehicle:",
                slot["vehicle"]
            )

            if slot["occupied"]:

                occupied += 1

        total = len(
            self.slots
        )

        free = total - occupied

        print("\n")
        print(
            f"Total Slots: {total}"
        )

        print(
            f"Occupied: {occupied}"
        )

        print(
            f"Free: {free}"
        )

    # -------------------------
    # Graphical Visualization
    # -------------------------

    def visualize(self):

        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        occupied_count = 0

        for r in range(self.rows):

            for c in range(self.cols):

                slot_id = (
                    f"{chr(65+r)}{c+1}"
                )

                slot = self.slots[
                    slot_id
                ]

                if slot["occupied"]:

                    color = "red"

                    occupied_count += 1

                else:

                    color = "green"

                rect = plt.Rectangle(

                    (
                        c,
                        self.rows-r-1
                    ),

                    1,

                    1,

                    color=color,

                    alpha=0.5
                )

                ax.add_patch(
                    rect
                )

                label = slot_id

                if slot["occupied"]:

                    label += (
                        "\n"
                        + slot["vehicle"]
                    )

                else:

                    label += (
                        "\nFREE"
                    )

                ax.text(

                    c + 0.5,

                    self.rows-r-0.5,

                    label,

                    ha="center",

                    va="center",

                    fontsize=9
                )

        total_slots = len(
            self.slots
        )

        free_slots = (
            total_slots -
            occupied_count
        )

        utilization = (
            occupied_count /
            total_slots
        ) * 100

        plt.title(

            "SMART PARKING VISUALIZATION\n"
            f"Occupied: {occupied_count} | "
            f"Free: {free_slots} | "
            f"Utilization: {utilization:.1f}%"

        )

        ax.set_xlim(
            0,
            self.cols
        )

        ax.set_ylim(
            0,
            self.rows
        )

        ax.set_aspect(
            "equal"
        )

        plt.axis(
            "off"
        )

        plt.show()