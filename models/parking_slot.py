from dataclasses import dataclass


@dataclass
class ParkingSlot:
    slot_id: str
    area: float
    occupied: bool = False
    vehicle_id: str = ""

    def __str__(self):
        status = "Occupied" if self.occupied else "Free"
        return f"{self.slot_id} | Area={self.area} | {status}"