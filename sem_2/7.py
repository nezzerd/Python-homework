import re


def car_number_type(car_number):
    private_pattern = r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}$'
    taxi_pattern = r'^[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}$'
    if re.match(private_pattern, car_number):
        return "Private"
    elif re.match(taxi_pattern, car_number):
        return "Taxi"
    else:
        return "Fail"


car_numbers = [
    "С227НА777",
    "КУ22777",
    "М227К19У9",
    "Т22В7477"
]
for car_number in car_numbers:
    print(f"{car_number} -> {car_number_type(car_number)}")
