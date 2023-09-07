def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(count_words(text))
    #print(count_each_char(text))

    char_dict = count_each_char(text)
    filtered_dict = only_letters_dict(char_dict)
    sorted_char_dict = sort_dict_by_value(filtered_dict)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words(text)} words found in the document")
    print('\n')
    print_char_count(sorted_char_dict)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_each_char(text):
    char_dict = {}
    for char in text:
        c = char.lower()
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict

def sort_dict_by_value(d):
    return sorted(d.items(), key=lambda x: x[1], reverse=True)

def only_letters_dict(text):
    return {k: v for k, v in text.items() if k.isalpha()}

def print_char_count(char_dict):
    for char, count in char_dict:
        print(f"The '{char}' character was found {count} times")

main()