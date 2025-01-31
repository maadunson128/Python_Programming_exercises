###Program: Number to wordings


def word(num):
    digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    if num < 10:
        return digits[num]
    
    return word(num // 10) + " " + digits[num % 10]

def main():
    num = input("Enter a number: ")
    num = int(num)
    print(word(num))


main()
