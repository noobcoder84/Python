def main():
    print("=== This program reads a file and prints the words ===")
    f = open("file.txt", "r")
    for line in f:
        print(line.strip("\n\r"))
    f.close()
if __name__ == "__main__":
    main()

