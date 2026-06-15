from dataclasses import dataclass


@dataclass
class Vehicle:
    vehicle_id: str
    length: float
    width: float
    priority: str

    @property
    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"{self.vehicle_id} | Area={self.area:.2f} | Priority={self.priority}"