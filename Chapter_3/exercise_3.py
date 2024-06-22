#Program: To find molecular weight of Carbohydrate

def molecular_weight(H, C, O):
    weight = 1.00794 * H + 12.0107 * C + 15.9994 * O
    print(f"Molecular weight: {weight}")

H = int(input("Enter the number of hydrogen atoms: "))
C = int(input("Enter the number of carbon atoms: "))
O = int(input("Enter the number of oxygen atoms: "))

molecular_weight(H, C, O)