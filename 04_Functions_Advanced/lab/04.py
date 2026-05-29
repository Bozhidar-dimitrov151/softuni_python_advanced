def rectangle(a, b):
    if isinstance(a, int) and isinstance(b, int):

        def area(a1, b1):
            return a1 * b1

        def perimeter(a2, b2):
            return 2 * (a2 + b2)

        return f"Rectangle area: {area(a, b)} \nRectangle perimeter: {perimeter(a, b)}"

    else:
        return "Enter valid values!"

print(rectangle(2, 10))
