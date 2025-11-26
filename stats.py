def get_book_text(path: str) -> str | None:
    """Get the text from a file
    Args:
        path (str): The relative path of the file.
    Returns:
        str: The text of the file if succesful.
        None: In case of an error.
    """
    with open(path, "r") as file:
        if file is not None:
            text = file.read()
            return text
        else:
            print("Error: File not found")
            return None


def get_num_words(path: str) -> int:
    """Get the number of words in a file
    Args:
        path (str): The relative path of the file.
    Returns:
        int: The number of words in the file if succesful.
        0: In case of an error.
    """
    text = get_book_text(path)
    if text is not None:
        words = text.split()
        return len(words)
    else:
        return 0


def get_charachter_sum(path: str) -> dict | None:
    """Get the character sum of a file
    Args:
        path (str): The relative path of the file.
    Returns:
        dict: The character sum of the file if succesful.
        None: In case of an error.
    """
    text = get_book_text(path)
    db = {}
    if text is not None:
        text = text.lower()
        for char in text.lower():
            db[char] = db.get(char, 0) + 1
        return db


def sort_chars(db: dict) -> list[dict]:
    """Sort the character sum of a file
    Args:
        db (dict): The character sum of the file.
    Returns:
        list[dict]: The sorted character sum of the file if succesful.
        None: In case of an error.
    """
    flat_list = []
    for k, v in db.items():
        if k.isalpha():
            obj = {"char": k, "num": v}
            flat_list.append(obj)
    flat_list.sort(key=lambda f: f["num"], reverse=True)
    return flat_list
