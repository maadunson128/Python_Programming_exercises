#Program: Simplify the Birthday song using function

def song(name:str)->None:

    print('Happy birthday to you.')
    print('Happy birthday to you.')
    print(f'Happy birthday to you, {name.title()}')
    print('Happy birthday to you.')


def main()->None:

    #birthday song for pradeep
    song('Pradeep')
    print()

    #birthday song for Ram kumar
    song('ram kumar')
    print()


main()
