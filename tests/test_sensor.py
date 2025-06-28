import unittest
from car_park import CarPark
from sensor import EntrySensor, ExitSensor

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("Test Location", 10)
        self.entry_sensor = EntrySensor("E1", True, self.car_park)
        self.exit_sensor = ExitSensor("X1", True, self.car_park)

    def test_entry_sensor_detects_vehicle(self):
        initial_count = len(self.car_park.plates)
        self.entry_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count + 1)

    def test_exit_sensor_detects_vehicle(self):
        self.car_park.add_car("TEST-001")
        initial_count = len(self.car_park.plates)
        self.exit_sensor.detect_vehicle()
        self.assertEqual(len(self.car_park.plates), initial_count - 1)

if __name__ == "__main__":
    unittest.main()