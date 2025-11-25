# Bookbot

# BookBot is my first [Boot.dev](https://www.boot.dev) project!
#
from stats import get_charachter_sum, get_num_words, sort_chars

frankenstein_path = "books/frankenstein.txt"


def main():
    number_of_words = get_num_words(frankenstein_path)
    db = get_charachter_sum(frankenstein_path)

    if db is not None:
        sorted = sort_chars(db)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {frankenstein_path}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for i in sorted:
            print(f"{i['char']}: {i['num']}")


if __name__ == "__main__":
    main()
