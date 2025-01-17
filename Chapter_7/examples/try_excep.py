###Program: Try exception
import math
def main()->None:

    try:
        a = float(input("Enter the co-efficient a: "))
        b = float(input("Enter the co-efficient b: "))
        c = float(input("Enter the co-efficient c: "))

        disc = math.sqrt((b**2) - (4*a*c))
        root_1 = (-b + disc) / (2*a)
        root_2 = (-b - disc) / (2*a)
        print(f"Real roots: {root_1}    {root_2}")

    except ValueError as exObj:
        if str(exObj) == "math domain error":
            print("No real roots")
        else:
            print("Invalid co-efficients given.")

    except:
        print("Something is going wrong.")

if __name__ == "__main__":
    main()
        
        
