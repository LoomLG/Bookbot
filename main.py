from stats import number_of_words

def get_book_text(filepath):
    content = ""
    with open(filepath) as f: content = f.read()
    return content

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(f"{number_of_words(book_text)} words found in the document")

main()