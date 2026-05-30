from collections import deque

def math_operations(*args, **kwargs):
    numbers = deque(args)
    operations = deque(["a", "s", "d", "m"])

    while numbers:
        op = operations.popleft()
        number = numbers.popleft()

        if op == "a":
            kwargs["a"] += number
        elif op == "s":
            kwargs["s"] -= number
        elif op == "d":
            if number != 0:
                kwargs["d"] /= number
        elif op == "m":
            kwargs["m"] *= number

        operations.append(op)

    sorted_kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))

    return "\n".join(f"{k}: {v:.1f}" for k, v in sorted_kwargs)

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))