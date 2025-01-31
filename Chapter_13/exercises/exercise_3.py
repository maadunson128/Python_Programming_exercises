###Palindrome 
def checkPalindrome(xStr, first_check=True):
    if first_check == True:
        for ch in "<}{ ][>.?/:;\\|+=-_),(*&^%$#@!~`":
            xStr = xStr.replace(ch, "")
        xStr = xStr.lower()

    if len(xStr) < 2:
        return True
    elif xStr[0] == xStr[-1]:
        xStr = xStr[1:-1]
        checkPalindrome(xStr, first_check=False)
        return True
    else:
        return False
    

def main():
    xStr = input("Enter a phrase: ")
    if checkPalindrome(xStr):
        print("The given phrase is palindrome")
    else:
        print("The given phrase is not palindrome")



if __name__ == "__main__":
    main()
            