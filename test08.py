def main():
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    num = int(input("Now enter any number: "))

    def year():
        y = 100 - age + 2017
        return y

    newYear = year()
    for i in range(num):
        print("You will be 100 years old in", newYear)

if __name__ == "__main__":
    main()

