from stats import number_of_words , count_characters, sorted_list

def get_book_text(filepath):
    content = ""
    with open(filepath) as f: content = f.read()
    return content

def main():
    book_text = get_book_text("books/frankenstein.txt")
    report = ("============ BOOKBOT ============\n"
             "Analyzing book found at books/frankenstein.txt...\n" 
             "----------- Word Count ----------\n" 
             f"Found {number_of_words(book_text)} total words\n" 
             "--------- Character Count -------")
    print(report)
    for d in sorted_list(count_characters(book_text)):
        print(f"{d["char"]}: {d["num"]}")
    print("============= END ===============")
main()