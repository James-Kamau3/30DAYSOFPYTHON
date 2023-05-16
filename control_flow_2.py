print("Please select: \n a. Addition(+) \n b.Subtraction(-) \n c.Multiplication(*) \n d.Division(/) \n e.Exit \n ")

while True:
    choise = str(input("Please select (a, b, c, d or e): "))


    if choise in ('a', 'b', 'c', 'd'):
        number_1 = int(input("Please enter 1st number: "))
        number_2 = int(input("Please enter 2nd number: "))
    
        
    if choise == "e":
            print("see you next time!")
            break

    def calculations():
        if choise == "a":
            return (f'sum is: {number_1 + number_2}')

        elif choise == "b":
            return (f'difference is: {number_1 - number_2}')

        elif choise == "c":
            return (f'product is: {number_1 * number_2}')

        elif choise == "d":
            return (f'quotient is: {number_1 / number_2}')
        
        else:
             print("Invlid choise try again")


    ans = calculations()
    print(ans)


