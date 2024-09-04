#random number from 0 to 10

import random as rd
def main()->None:

    outfile = open('ex_16_data.txt', 'w')

    for i in range(100):
        print(rd.randrange(0,11,1), file=outfile)


main()
