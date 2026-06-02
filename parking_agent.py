from constraint import Problem, AllDifferentConstraint


class SmartParkingAgent:

    def __init__(self, vehicles, parking_slots):

        self.vehicles = vehicles
        self.parking_slots = parking_slots

        self.problem = Problem()

    # --------------------------------
    # Generate Domains
    # --------------------------------

    def generate_domains(self):

        for vehicle, vinfo in self.vehicles.items():

            valid_slots = []

            for slot, sinfo in self.parking_slots.items():

                # Size Compatibility Constraint
                if sinfo["size"] >= vinfo["size"]:
                    valid_slots.append(slot)

            self.problem.addVariable(vehicle, valid_slots)

    # --------------------------------
    # Add Constraints
    # --------------------------------

    def add_constraints(self):

        # One Vehicle Per Slot
        self.problem.addConstraint(
            AllDifferentConstraint(),
            self.vehicles.keys()
        )

        # Priority Constraints
        for vehicle in self.vehicles.keys():

            self.problem.addConstraint(
                lambda slot, v=vehicle:
                self.priority_constraint(v, slot),
                [vehicle]
            )

    # --------------------------------
    # Priority Rule
    # --------------------------------

    def priority_constraint(self, vehicle, slot):

        priority = self.vehicles[vehicle]["priority"]

        distance = self.parking_slots[slot]["distance"]

        # Emergency Vehicles
        if priority == "Emergency":

            return distance <= 8

        # VIP Vehicles
        elif priority == "VIP":

            return distance <= 15

        return True

    # --------------------------------
    # Solve CSP
    # --------------------------------

    def solve(self):

        self.generate_domains()

        self.add_constraints()

        solutions = self.problem.getSolutions()

        return solutions