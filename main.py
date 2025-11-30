from stats import (
    get_book_text,
    count_number_of_words,
    count_letter_occurence,
    sort_dictionary,
)
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]

    frankenstein_text = get_book_text(path_to_file)
    frankenstein_word_count = count_number_of_words(frankenstein_text)
    frankenstein_character_tracker = count_letter_occurence(frankenstein_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {frankenstein_word_count} total words")
    print("--------- Character Count -------")

    sorted_frankenstein = sort_dictionary(frankenstein_character_tracker)

    for item in sorted_frankenstein:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
