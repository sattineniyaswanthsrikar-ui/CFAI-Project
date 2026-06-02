from parking_data import vehicles, parking_slots

from parking_agent import SmartParkingAgent

from visualization import (
    display_solution,
    plot_graph
)

# --------------------------------
# Create AI Agent
# --------------------------------

agent = SmartParkingAgent(
    vehicles,
    parking_slots
)

# --------------------------------
# Solve Problem
# --------------------------------

solutions = agent.solve()

# --------------------------------
# Display Results
# --------------------------------

if solutions:

    best_solution = solutions[0]

    display_solution(
        best_solution,
        vehicles,
        parking_slots
    )

    plot_graph(
        best_solution,
        parking_slots
    )

else:

    print("No valid parking allocation found.")