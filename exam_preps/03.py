def boarding_passengers(capacity, *groups):
    boarded = {}
    unprocessed_groups = False

    for passengers, program in groups:
        if capacity == 0:
            unprocessed_groups = True
            break

        if passengers <= capacity:
            capacity -= passengers
            boarded[program] = boarded.get(program, 0) + passengers
        else:
            unprocessed_groups = True

    result = []

    # 1. FIRST: benefit plan output
    for program, guests in sorted(
        boarded.items(),
        key=lambda x: (-x[1], x[0])
    ):
        result.append(f"## {program}: {guests} guests")

    # 2. THEN: status message
    if capacity == 0 and unprocessed_groups:
        result.append("Boarding unsuccessful. Cruise ship at full capacity.")

    elif capacity == 0 and not unprocessed_groups:
        result.append("All passengers are successfully boarded!")

    else:
        result.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(result)

