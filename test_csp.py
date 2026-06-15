from models.vehicle import Vehicle
from csp.solver import CSPSolver

vehicles = [

    Vehicle(
        "CAR101",
        4,
        2,
        "VIP"
    ),

    Vehicle(
        "AMB001",
        5,
        2,
        "Emergency"
    )
]

parking_slots = {

    "A1": {
        "area": 12,
        "occupied": False
    },

    "A2": {
        "area": 10,
        "occupied": False
    },

    "B1": {
        "area": 8,
        "occupied": False
    },

    "B2": {
        "area": 15,
        "occupied": False
    }
}

solver = CSPSolver(
    vehicles,
    parking_slots
)

result = solver.solve()

print("\nCSP RESULT\n")

print(result)