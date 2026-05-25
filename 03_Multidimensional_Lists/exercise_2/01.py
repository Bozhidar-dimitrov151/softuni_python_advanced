first_list = [x.split() for x in input().split('|')]
flattened_list = []

for lis in first_list[::-1]:
    for el in lis:
        flattened_list.append(el)

print(' '.join(flattened_list))