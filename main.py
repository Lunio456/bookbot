import re

def main2():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(str(len(file_contents.split())) + " words found in the document")

def main3():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        letter_count = {}
        for c in file_contents:
            if c.lower() in letter_count.keys():
                letter_count[c.lower()] += 1
            else:
                letter_count[c.lower()] = 1
        for k in letter_count.keys():
            if re.match("^[A-Za-z0-9]+$", k):
                print("The '" + k + "' character was found " + str(letter_count[k]) + " times")    
            
def main():
    print("--- Begin report of books/frankenstein.txt ---")
    main2()
    print()
    main3()

main()