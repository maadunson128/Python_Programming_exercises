###Program: Using Sieve of Eratosthenes algorithm for prime numbers


def remove_multiples(sieve_list:list[int], element:int)->list[int]:
    '''Function that removes the multiples of a element in a list'''
    n = len(sieve_list)
    multiples:list[int] = [element*i for i in range(2, n+1)]

    for i in multiples:
        if i in sieve_list:
            sieve_list.remove(i)

    return sieve_list


def sieve_algo(n:int)->list[int]:
    '''Function for finding the primw numbers upto n using Sieve of Eratosthenes algorithm'''
    #creating initial list upto n
    sieve_list = [i for i in range(2, n+1)]

    prime_numbers = []

    while not sieve_list == []:
        first = sieve_list.pop(0)
        prime_numbers.append(first)

        sieve_list = remove_multiples(sieve_list, first)


    return prime_numbers




def main():

    #Input from the user
    n:int = int(input("Enter the value n to find prime numbers upto n: "))

    prime_numbers = sieve_algo(n)

    print(f"Prime numbers list: {prime_numbers}")


if __name__ == "__main__":
    main()