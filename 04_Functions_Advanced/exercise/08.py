def age_assignment(*args, **kwargs):
    name_age = {}
    for name in args:
        name_age[name] = 0
        key = name[0]
        name_age[name] += kwargs.get(key)

    sorted_dict = sorted(name_age.items(), key=lambda x: x[0])
    return '\n'.join(f"{person[0]} is {person[1]} years old." for person in sorted_dict)

print(age_assignment("Peter", "George", G=26, P=19))

