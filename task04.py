[reactants, products]=list(map(str, input().split(" - ")))
reactants = list(map(str, reactants.split(" + ")))
products = list(map(str, products.split(" + ")))

# Using Chempy package
from chempy import balance_stoichiometry
reac,prod=balance_stoichiometry(reactants, products)
for reactant in reactants:
    print(reac[reactant], end=" ")
for product in products:
    print(prod[product], end=" ")