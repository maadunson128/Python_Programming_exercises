#Program: This will take names from one file and creates username for them
#and store it in another file

def main()->None:

    print("****Username Generator****")

    #getting the files name
    file1 = input("Enter the file name which contains the names: ")
    file2 = input("Enter the file name to store the usernames: ")

    #Opening the files
    infile = open(file1, "r")
    outfile = open(file2, "w")

    #reading the name and creating usernames
    for line in infile:
        first, last = line.split()
        username = (first[0] + last[:7]).lower()
        print(username, file= outfile)

    infile.close()
    outfile.close()
    print("Usernames generated and written in the file.")

main()
    
