### Program: Lyrics for ten verse of "The Ants Go Marching."

def lyrics(activities)->None:
    lyric:str = 'The ants go marching one by one, hurrah! hurrah! \n' + \
                'The ants go marching one by one, hurrah! hurrah! \n' + \
                'The ants go marching one by one, \n' + \
                f'The little one stops to {activities[0]}, \n' + \
                'And they all go marching down ... \n' + \
                'In the ground ... \n' + \
                'To get out .... \n' + \
                'Of the rain. \n' + \
                'Boom! Boom! Boom! \n' + \
                'The ants go marching two by two, hurrah! hurrah! \n' + \
                'The ants go marching two by two, hurrah! hurrah! \n' + \
                'The ants go marching two by two, \n' + \
                f'The little one stops to {activities[1]}, \n' + \
                'And they all go marching down ... \n' + \
                'In the ground ... \n' + \
                'To get out ... \n' + \
                'Of the rain. \n' + \
                'Boom! Boom!  \n'

    print(lyric)
    

def main()->None:

    #user input for the activity
    activities:list[str] = input("Enter the two activities, separated by comma to put in the lyrics: ").split(',')
    
    #printing the lyrics
    lyrics(activities)

main()
