def main():

    print("=== Multiples of Four (0-100) ===")
    num = []

    for n in range(101):
        if n%4==0:
            num.append(n)

    print('Found', len(num), 'numbers')
    print('Listing the first half')
    print(num[:int(len(num)//2)])
    print('Listing the second half')
    print(num[int(len(num)//2):])

if __name__ == "__main__":
    main()


