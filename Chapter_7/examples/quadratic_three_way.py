###Program: Real roots for Quadratic equation from its coefficients

def main()->None:

    #coeffficients input
    a = eval(input("Enter the coefficient a : "))
    b = eval(input("Enter the coefficient b : "))
    c = eval(input("Enter the coefficient c : "))

    discr = b**2 - 4*a*c

    #condition 1: Real roots and distinct
    if discr > 0:
        root_1 = (-b + discr )/ (2*a)
        root_2 = (-b - discr )/ (2*a)
        print(f"The equation has real roots. \nReal roots are {root_1}    {root_2}")
        
    #condition 2: Real roots and same
    elif discr == 0:
        double_root = -b/(2*a)
        print(f"The equation has real roots and they are same. \nReal root: {double_root}")
    #condition 3: No real roots
    elif discr < 0:
        print("The equation has no real roots.")


if __name__ == '__main__':
    main()
    
