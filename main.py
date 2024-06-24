def read_file():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def words_to_list():
    file_text = read_file()
    words = file_text.split()
    return words


def chars_to_dict():
    abc_dict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
        'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
        'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
        'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
        'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    file_text = read_file().lower()

    for letter in file_text:
        if letter in abc_dict:
            x = abc_dict[letter]
            x += 1
            abc_dict[letter] = x

    return abc_dict


def count_words():
    word_count = 0
    for word in words_to_list():
        word_count += 1
    
    return word_count


def main():
    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words()} words found in the document')
    letter_dict = chars_to_dict()
    for letter in letter_dict:
        print(f"The {letter} character was found {letter_dict[letter]} times")

main()
