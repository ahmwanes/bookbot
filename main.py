# Bookbot

# BookBot is my first [Boot.dev](https://www.boot.dev) project!
#
from stats import Bookbot

frankenstein_path = "books/frankenstein.txt"


def main():
    book = Bookbot(frankenstein_path)
    number_of_words = book.get_num_words_in_text()
    db = book.get_charachter_sum()

    if db is not None:
        sorted = book.get_charachter_sum_sorted_and_flatened()
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {frankenstein_path}...")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for i in sorted:
            print(f"{i['char']}: {i['num']}")


if __name__ == "__main__":
    main()
