

def main():
    path = "books/frankenstein.txt"
    words = get_words(path)
    num_words = get_word_count(words)
    char_dict  = get_character_count(words)
    print(f"{num_words} found found @ {path}")
    print(char_dict)


def get_words(path):
    with open(path) as f:
        return f.read()


def get_word_count(book: str) -> int:
    words = book.split()
    return len(words)



def get_character_count(book: str):
    character_dict = {}
    words = book.split()
    occurence = 1
    for word in words:
        word = word.lower()
        for letter in word:
            if letter in character_dict:
                character_dict[letter] +=1
            else:
                character_dict[letter] = 1
    return character_dict


main()