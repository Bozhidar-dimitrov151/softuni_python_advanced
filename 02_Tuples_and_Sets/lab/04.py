number_cars = int(input())

parking_lot = set()

for _ in range(number_cars):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking_lot.add(car_number)

    elif direction == "OUT":
        parking_lot.discard(car_number)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)