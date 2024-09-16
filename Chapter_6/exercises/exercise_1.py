#program: Lyrics of the song 'Old McDonald'

def lyrics(animal_name:str)->None:
    lyric:str = 'Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n' + \
                f'And on that farm he had a {animal_name}, Ee-igh, Ee-igh, Oh! \n' + \
                'With a moo, moo here and a moo, moo there. \n' + \
                'Here a moo, there a moo, everywhere a moo, moo. \n' + \
                'Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!'
    print(lyric)


def main()->None:
    #animal name from the user
    animal:str = input("Enter a animal name: ")

    #Print the lyrics for the animal
    lyrics(animal)

main()
