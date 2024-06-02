

def main():
    path = "books/frankenstein.txt"
    words = get_words(path)
    num_words = get_word_count(words)
    char_dict  = get_character_count(words)
    char_report = get_list_of_dicts(char_dict)
    print(f"--- begin report of {path} ---")
    print(f"{num_words} words found in document")
    print(f"Char_report: {char_report.sort(reverse=True, key=sort_on)}")
    

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

def sort_on(dict: dict):
    return(dict["count"])

def get_list_of_dicts(dict: dict[str, int]) -> list:
    list_of_dicts = []
    for k in dict:
        if k.isalpha():
            new_dict = {"char": k, "count": dict[k]}
            list_of_dicts.append(new_dict)
    return list_of_dicts


main()