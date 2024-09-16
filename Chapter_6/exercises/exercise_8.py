###Program : To guess the square root ofa number

#function to guess the square root number
def guess_number(number:float, iteration:int)->float: 
    guess = number / 2
    for i in range(iteration):
        guess = (guess + (number / guess)) / 2

    final_value = guess
    return final_value


def main()->None:

    #user input for number guess, iteration for the forumula
    number = float(input("Enter the number: "))
    iteration = int(input("Enter the iteration for the guess formula to run: "))

    #guessing the number
    guess = guess_number(number, iteration)

    print(f"The guessed number : {guess}")


main()
