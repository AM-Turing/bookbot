import sys
from stats import number_of_words, character_count, sorted_dictionary

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    number = number_of_words(text)
    dictionary = character_count(text)
    sorted_list = sorted_dictionary(dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['character']}: {item['count']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
