def main():


    try:
        a = int(input("1st #: "))
        b = int(input("2nd #: "))
        res = a / b
        print(res)

    except ZeroDivisionError:
        print("Something happened.")




if __name__ == "__main__":
    main()


