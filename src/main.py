from car_park import CarPark
from display import Display
from sensor import EntrySensor, ExitSensor

def main():
    # Initialize car park
    car_park = CarPark(location="Downtown", capacity=5)

    # Create and register display
    display = Display(display_id="D1", is_on=True)
    car_park.register(display)

    # Create and register sensors
    entry_sensor = EntrySensor(sensor_id="E1", is_active=True, car_park=car_park)
    exit_sensor = ExitSensor(sensor_id="X1", is_active=True, car_park=car_park)
    car_park.register(entry_sensor)
    car_park.register(exit_sensor)

    print("Initial state:")
    print(car_park)
    print(display)

    # Simulate vehicle entries
    print("\nSimulating vehicle entries:")
    for _ in range(3):
        entry_sensor.detect_vehicle()
        print(car_park)
        print(display)

    # Simulate vehicle exit
    print("\nSimulating vehicle exit:")
    exit_sensor.detect_vehicle()
    print(car_park)
    print(display)

    # Simulate another entry
    print("\nSimulating another entry:")
    entry_sensor.detect_vehicle()
    print(car_park)
    print(display)

if __name__ == "__main__":
    main()