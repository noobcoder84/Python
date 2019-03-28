def main():
    print("=== This program writes to a file ===")
    f = open("file2.txt", "w")
    for i in range(5):
        f.write(input("Type a new word: ") + "\n")
    f.close()
if __name__ == "__main__":
    main()




