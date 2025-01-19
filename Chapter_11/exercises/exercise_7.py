###Cross product of two similar list

def innerProd(x, y):
    inner_product = 0
    for i in range(len(x)):
        inner_product += (x[i] * y[i])

    return inner_product

print(f"Inner product of two lists: {innerProd([1,9, 10], [10, 9, 1])}")