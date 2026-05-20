number_lines = int(input())
unique_chemical_compounds = set()

for _ in range(number_lines):
    chemical_compounds = input().split()
    unique_chemical_compounds.update(chemical_compounds)

print(*unique_chemical_compounds, sep='\n')