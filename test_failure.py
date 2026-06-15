from models.vehicle import Vehicle
from csp.solver import CSPSolver

vehicles = [

    Vehicle(
        "TRUCK101",
        10,
        5,
        "Normal"
    )
]

parking_slots = {

    "A1": {
        "area": 10,
        "occupied": False
    },

    "A2": {
        "area": 12,
        "occupied": False
    }
}

solver = CSPSolver(
    vehicles,
    parking_slots
)

print(
    solver.solve()
)