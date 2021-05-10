
def is_word_in_text(word):
    file = open("Check.txt", "r")

    if word in file.read():
        print(f"Found! {word} in {file.name}")
    else:
        print(f"Did not find: {word} in {file.name}")

    file.close()


def how_many_words_in_text(file):
    words = 0

    with open(file, "r") as openFile:
        content = openFile.readlines()
        for item in content:
            temp_word = item.strip().split(" ")
            for count in temp_word:
                words += 1
    print(f"Words in this text file(numbers included): {words}")


def how_many_chars_in_text(file):
    with open(file, "r") as file:
        chars = 0
        for char in file.readlines():
            chars += len(char)
    print(f"single chars in this file: {chars}")

