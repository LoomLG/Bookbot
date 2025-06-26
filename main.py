import sys
from stats import number_of_words , count_characters, sorted_list

def get_book_text(filepath):
    content = ""
    with open(filepath) as f: content = f.read()
    return content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    report = ("============ BOOKBOT ============\n"
             f"Analyzing book found at {sys.argv[1]}...\n" 
             "----------- Word Count ----------\n" 
             f"Found {number_of_words(book_text)} total words\n" 
             "--------- Character Count -------")
    print(report)
    for d in sorted_list(count_characters(book_text)):
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
main()