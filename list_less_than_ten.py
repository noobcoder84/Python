def main():

    #lists the numbers that are less than 5
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for i in a:
        if i<5:
            b.append(i)
    print(b)
    
    #list the numbers that are less than the number
    #that is provided by the user
    y = []
    x = int(input("Enter a number: "))
    for i in a:
        if i < x:
            y.append(i)
    print(y)

if __name__ == "__main__":
    main()

