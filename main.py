from stats import get_num_word, count_char, sort_count_char
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    num_words = get_num_word(text)
    count = count_char(text)
    sorted_count = sort_count_char(count)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for count in sorted_count:
        if count["character"].isalpha():
            print(f"{count["character"]}: {count["count"]}")
    print("============= END ===============")

main()