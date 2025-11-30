def get_book_text(path_to_file: str):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def count_number_of_words(book_text: str):
    number_of_words = len(book_text.split())
    return number_of_words


def count_letter_occurence(book_text: str):
    normalized_book_text = book_text.lower()
    character_tracker = {}
    for character in normalized_book_text:
        if character in character_tracker:
            character_tracker[character] += 1
        else:
            character_tracker[character] = 1
    return character_tracker


def sort_on(items):
    return items["num"]


def sort_dictionary(unsorted_dictionary):
    sorted_list = []
    for key, value in unsorted_dictionary.items():
        sorted_list.append({"char": key, "num": value})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
