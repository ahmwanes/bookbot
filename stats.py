# Get the text of a book from a file


def get_book_text(path: str):
    with open(path, "r") as file:
        if file is not None:
            text = file.read()
            return text
        else:
            print("Error: File not found")
            return None


def get_num_words(path: str) -> int:
    text = get_book_text(path)
    if text is not None:
        words = text.split()
        return len(words)
    else:
        return 0


def get_charachter_sum(path: str):
    text = get_book_text(path)
    db = {}
    if text is not None:
        text = text.lower()
        for char in text.lower():
            db[char] = db.get(char, 0) + 1
        return db


def sort_chars(db: dict):
    flat_list = []
    for k, v in db.items():
        if k.isalpha():
            obj = {"char": k, "num": v}
            flat_list.append(obj)
    flat_list.sort(key=lambda f: f["num"], reverse=True)
    return flat_list
