def sorting_cheeses(**cheese_dict):
    cheese_dict = sorted(cheese_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese_name, quantity in cheese_dict:
        result.append(cheese_name)
        quantity = sorted(quantity, reverse=True)
        for idx in range(len(quantity)):
            result.append(str(quantity[idx]))


    return "\n".join(result)

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
