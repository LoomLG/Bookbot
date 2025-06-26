def number_of_words(book_text):
    text_by_line = book_text.split()
    return len(text_by_line)

def count_characters(book_text):
    text = list(book_text)
    char_array = {}
    for char in text:
        char = char.lower()
        if char in char_array:
            char_array[char] = char_array[char] + 1
        else: char_array[char] = 1
    return char_array

def sort_on(item):
    return item["num"]

def sorted_list(char_dictionary):
    ls = []
    for key,value in char_dictionary.items():
        if key.isalpha():
            d = {}
            d["char"] = key
            d["num"] = value
            ls.append(d)
    ls.sort(reverse=True, key=sort_on)
    return ls
