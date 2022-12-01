### John Kull's integration project
### The goal of this program is to sort a list of numbers
### In different ways depending on user inputs
### + string operator to combine text together
print("Sort Numbers In Different" + " Types Of Lists")
Typeoflist = int(input("Type 1 for List1, Type 2 for list2, Type 3 for list3, Type 5 for a sorted list,"
                       "Type 4 for other functions: "))
Sizeoflist = 0
othertype = 0
### == is equal to operator, and // floor division operator
if Typeoflist == (9.1 // 3 or 2 ** 2):
    print("")
### != does not equal operator
### or bolean operator
elif (Typeoflist != (3) or Typeoflist == (1 or 2)):
    Sizeoflist = int(input("How large you want the list to be: "))
### blank list
List = []
### if statement to load the loop determined by the user
if Typeoflist == (1):
    print("Type the numbers you want in the list: ")
    ### in and range structures used to determine the range
    for numamount in range(Sizeoflist):
        usernumbers = int(input())
        List.append(usernumbers)
    print(List)
    print("Your standard list is complete.")
    print("The program is completed.")
### elif statement used to allow the choice of a second list which prints the list vertically
### + operator for addition
elif (Typeoflist == 1+1):
    print("Type the numbers you want in the list: ")
    for numamount in range(Sizeoflist):
        usernumbers = int(input())
        List.append(usernumbers)
    print(*List,sep='\n')
    print("The program is completed.")
### 3rd list style which prints the list in a divided triangle shape
### / operator for division
elif (Typeoflist == 9 / 3):
    print("Type the numbers you want to be listed in a divided triangle: ")
    usernumbers = int(input())
    num_columns = usernumbers
    for numamount in range(usernumbers):
        for columns in range(1, num_columns + 1):
            print(columns, end='')
        num_columns = num_columns - 1
        print()
        print("The program is completed.")
### 4th list style, numerically organizes the list
elif (Typeoflist == 5):
    print("Type the numbers you want in the list: ")
    for numamount in range(Sizeoflist):
        usernumbers = int(input())
        List.append(usernumbers)
    ### sorted, sorts the list numerically
    print(sorted(List))
    print("The program is completed")
if Typeoflist == (4):
    print("Type 1 for Less than function, Type 2 for quiz game, : ")
    othertype = int(input(""))
if othertype == (10 % 3):
    ### input using a float
    lessthan = float(input("type a number less than 10 or greater than 10: "))
    ### % modulus operator
    lessthan = lessthan * 2
    lessthan = lessthan / (10 % 4)
    ### < less than relational operator
    if lessthan <= (10):
        print("Your number is less than 10")
        print("The program is completed.")
    ### else standard conditional
    else:
        print("Your number is greater than 10")
        print("The program is completed.")
### Quiz game
elif othertype == (2):
    answers = 1
    if (answers > 0):
        print("What is the capital of Florida? ")
        print("A. Fort Myers" '\n' "B. Miami" '\n' "C. Jacksonville" '\n' "D. Tallahassee")
        ### str used to convert input to a string
        answer1 = str(input())
        if (answer1) != ("d" or "D"):
            answers = answers - 1
        print("What color can humans see the most shades of")
        print("A. Red" '\n' "B. Green" '\n' "C. Yellow" '\n' "D. Orange")
        answer2 = str(input())
        if (answer2) != ("b" or "B"):
            answers = answers - 1
        print("Which lovcraftian creature is the god of chaos")
        print("A. Azathoth" '\n' "B. Nyarlathotep" '\n' "C. Cthulhu" '\n' "D. Dagon")
        answer3 = str(input())
        if (answer3) != ("a" or "A"):
            answers = answers - 1
    if answers == (1):
        print("Congratulations, "
              "you beat the quiz")
    else:
        print("You failed!!!!!!!!!")
#        print("....................../Â´Â¯/)" '\n' "....................,/Â¯../ ")




