

def main():
    path = "books/frankenstein.txt"
    words = get_words(path)
    num_words = get_word_count(words)
    print(f"{num_words} found found @ {path}")
   
    
def get_words(path):
    with open(path) as f:
        return f.read()


def get_word_count(book: str) -> int:
    words = book.split()
    return len(words)

main()