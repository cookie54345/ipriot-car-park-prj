from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
from pathlib import Path

# TODO: create a car park object with the location moondalup, capacity 100, and log_file "moondalup.txt"
car_park = CarPark(location="moondalup", capacity=100, log_file=Path("moondalup.txt"))

# TODO: Write the car park configuration to a file called "moondalup_config.json"
car_park.write_config(config_file="moondalup_config.json")

# TODO: Reinitialize the car park object from the "moondalup_config.json" file
car_park = CarPark.from_config("moondalup_config.json")

# TODO: create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(sensor_id=1, is_active=True, car_park=car_park)

# TODO: create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(sensor_id=2, is_active=True, car_park=car_park)

# TODO: create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(display_id=1, message="Welcome to Moondalup", is_on=True)
car_park.register(display)

# TODO: drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for i in range(1, 11):
    entry_sensor.detect_vehicle()

# TODO: drive 2 cars out of the car park (must be triggered via the sensor - NOT by calling car_park.remove_car directly)
for _ in range(2):
    exit_sensor.detect_vehicle()