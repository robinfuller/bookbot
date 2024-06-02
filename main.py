

def main():
    path = "books/frankenstein.txt"
    words = get_words(path)
    num_words = get_word_count(words)
    char_dict  = get_character_count(words)
    char_report = get_list_of_dicts(char_dict)
    print(f"--- begin report of {path} ---\n\n")
    print(f"{num_words} words found in document\n\n")
    print_report(char_report)
    print(f"\n\n--- end report ---")
    

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

def print_report(report: list):
    if __name__ == "__main__":
        report.sort(reverse=True, key=sort_on)
        for dict in report:
                char = dict.get("char")
                count = dict.get("count")
                string = f"The {char} was found {count} times"
                print(string)

main()