class Constraints:

    @staticmethod
    def size_constraint(vehicle, slot):
        return slot["area"] >= vehicle.area

    @staticmethod
    def occupancy_constraint(slot):
        return not slot["occupied"]

    @staticmethod
    def priority_constraint(vehicle, slot_id):

        if vehicle.priority == "Emergency":
            return slot_id.startswith("A")

        elif vehicle.priority == "VIP":
            return (
                slot_id.startswith("A")
                or slot_id.startswith("B")
            )

        return True