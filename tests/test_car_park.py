import unittest
from car_park import CarPark
from pathlib import Path


class TestCarPark(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark(location="123 Example Street", capacity=100)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def tearDown(self):
        Path("test_log.txt").unlink(missing_ok=True)

    def test_log_file_created(self):
        test_park = CarPark("123 Example Street", 100, log_file="test_log.txt")
        test_park.add_car("LOG-001")
        self.assertTrue(Path("test_log.txt").exists())

    def test_car_logged_when_entering(self):
        test_park = CarPark("123 Example Street", 100, log_file="test_log.txt")
        test_park.add_car("NEW-001")
        with test_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)
        self.assertIn("entered", last_line)
        self.assertIn("\n", last_line)

    def test_car_logged_when_exiting(self):
        test_park = CarPark("123 Example Street", 100, log_file="test_log.txt")
        test_park.add_car("NEW-002")
        test_park.remove_car("NEW-002")
        with test_park.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-002", last_line)
        self.assertIn("exited", last_line)
        self.assertIn("\n", last_line)


if __name__ == "__main__":
    unittest.main()