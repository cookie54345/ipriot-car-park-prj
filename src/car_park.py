from display import Display
from sensor import Sensor


class CarPark:
    def __init__(self,
                 location,
                 capacity,
                 plates=None,
                 displays=None):

        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = []

    def __str__(self):
        return f"Car park at {self.location} has {self.capacity} bays available."

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_displays()

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
        self.update_displays()

    @property
    def available_bays(self):
        return max(0, self.capacity - len(self.plates))

    def update_displays(self):
        data = {
            "available_bays": self.available_bays,
            "temperature": 25,  # Placeholder
            "time": "12:00pm"  # Placeholder
        }

        for display in self.displays:
            display.update(data)
