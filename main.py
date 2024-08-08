def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        numOfWords = countWords(file_contents)
        charsDict = countChars(file_contents)
        sortedList = charsDictToList(charsDict)

        print("Book report")
        print(f"There are {numOfWords}")

        for item in sortedList:
            if not item["char"].isalpha():
                continue
            print(f"the '{item['char']}' char was found {item['num']} times")
        print("End report")


def countWords(file_contents):
    words = file_contents.split()
    return len(words)


def countChars(file_contents):
    chars = {}
    for char in file_contents:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(sort):
    return sort["num"]


def charsDictToList(charsDict):
    list = []
    for char in charsDict:
        list.append({"char": char, "num": charsDict[char]})
    list.sort(reverse=True, key=sort_on)
    return list


main()
