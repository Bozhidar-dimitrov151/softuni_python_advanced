from collections import deque

packages = list(map(int, input().split()))
number_couriers = deque(map(int, input().split()))
total_weight = 0
total_delivered = 0

while packages and number_couriers:
    package = packages.pop()
    courier = number_couriers.popleft()

    if courier >= package:
        total_weight += package

        new_capacity = courier - (2 * package)
        if new_capacity > 0:
            number_couriers.append(new_capacity)

    else:
        total_weight += courier

        remaining_weight = package - courier
        packages.append(remaining_weight)

print(f"Total weight: {total_weight} kg")

if not packages and not number_couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages and not number_couriers:
    print("Unfortunately, there are no more available couriers to deliver the following packages: "+ ", ".join(map(str, packages)))

elif number_couriers and not packages:
    print(f"Couriers are still on duty: {', '.join(map(str, number_couriers))} but there are no more packages to deliver.")