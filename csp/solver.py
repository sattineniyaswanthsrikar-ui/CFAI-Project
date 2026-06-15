from csp.constraints import Constraints
from csp.heuristics import Heuristics


class CSPSolver:

    def __init__(self, vehicles, parking_slots):

        self.vehicles = vehicles
        self.parking_slots = parking_slots

        self.assignments = {}

    # -------------------------
    # Generate Domains
    # -------------------------

    def generate_domains(self):

        domains = {}

        for vehicle in self.vehicles:

            valid_slots = []

            for slot_id, slot in self.parking_slots.items():

                # Size Constraint
                if not Constraints.size_constraint(
                        vehicle,
                        slot):
                    continue

                # Occupancy Constraint
                if not Constraints.occupancy_constraint(
                        slot):
                    continue

                # Priority Constraint
                if not Constraints.priority_constraint(
                        vehicle,
                        slot_id):
                    continue

                valid_slots.append(slot_id)

            domains[vehicle.vehicle_id] = valid_slots

        return domains

    # -------------------------
    # Assignment Check
    # -------------------------

    def is_valid(
            self,
            vehicle_id,
            slot_id):

        return slot_id not in self.assignments.values()

    # -------------------------
    # Forward Checking
    # -------------------------

    def forward_check(
            self,
            domains,
            assigned_slot):

        new_domains = {}

        for vehicle, domain in domains.items():

            new_domains[vehicle] = [

                slot

                for slot in domain

                if slot != assigned_slot
            ]

        return new_domains

    # -------------------------
    # Backtracking Search
    # -------------------------

    def backtrack(
            self,
            domains):

        # Goal Test
        if len(self.assignments) == len(self.vehicles):

            return True

        # MRV Selection
        vehicle_id = Heuristics.mrv(
            domains
        )

        if vehicle_id is None:

            return False

        for slot_id in domains[vehicle_id]:

            if self.is_valid(
                    vehicle_id,
                    slot_id):

                # Assign
                self.assignments[
                    vehicle_id
                ] = slot_id

                # Forward Checking
                new_domains = self.forward_check(
                    domains,
                    slot_id
                )

                # Remove assigned variable
                new_domains[
                    vehicle_id
                ] = []

                # Recursive Search
                if self.backtrack(
                        new_domains):

                    return True

                # Backtrack
                del self.assignments[
                    vehicle_id
                ]

        return False

    # -------------------------
    # Failure Explanation
    # -------------------------

    def explain_failure(self):

        print("\n" + "=" * 50)
        print("ALLOCATION FAILED")
        print("=" * 50)

        for vehicle in self.vehicles:

            largest_slot = max(
                slot["area"]
                for slot in self.parking_slots.values()
            )

            if vehicle.area > largest_slot:

                print(
                    f"\nVehicle: "
                    f"{vehicle.vehicle_id}"
                )

                print(
                    f"Required Area: "
                    f"{vehicle.area}"
                )

                print(
                    f"Largest Slot Area: "
                    f"{largest_slot}"
                )

                print(
                    "Reason: "
                    "No slot satisfies "
                    "size constraint."
                )

            else:

                print(
                    f"\nVehicle: "
                    f"{vehicle.vehicle_id}"
                )

                print(
                    "Reason: "
                    "No valid slot available."
                )

    # -------------------------
    # Solve CSP
    # -------------------------

    def solve(self):

        domains = self.generate_domains()

        print("\nGenerated Domains\n")

        for vehicle, domain in domains.items():

            print(
                vehicle,
                "->",
                domain
            )

        success = self.backtrack(
            domains
        )

        if success:

            print("\nAllocation Successful\n")

            return self.assignments

        self.explain_failure()

        return None