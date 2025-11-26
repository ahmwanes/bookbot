class Bookbot:
    text: str
    word_count: int
    charachter_sum: dict

    def __init__(self, path: str) -> None:
        self.path = path

    def read(self) -> str | None:
        """Get the text from a file
        Args:
            path (str): The relative path of the file.
        Returns:
            str: The text of the file if succesful.
            None: In case of an error.
        """
        with open(self.path, "r") as file:
            if file is not None:
                text = file.read()
                self.text = text

                return text
            else:
                print("Error: File not found")
                return None

    def get_num_words_in_text(self) -> int:
        """Get the number of words in a file
        Args:
            path (str): The relative path of the file.
        Returns:
            int: The number of words in the file if succesful.
            0: In case of an error.
        """
        text = self.read()

        if text is not None:
            words = text.split()
            word_count = len(words)
            self.word_count = word_count

            return word_count
        else:
            return 0

    def get_charachter_sum(self) -> dict | None:
        """Get the character sum of a file
        Args:
            path (str): The relative path of the file.
        Returns:
            dict: The character sum of the file if succesful.
            None: In case of an error.
        """

        text = self.read()

        db = {}

        if text is not None:
            text = text.lower()

            for char in text.lower():
                db[char] = db.get(char, 0) + 1

            self.charachter_sum = db

            return db

    def get_charachter_sum_sorted_and_flatened(self) -> list[dict]:
        """Sort the character sum of a file
        Args:
            db (dict): The character sum of the file.
        Returns:
            list[dict]: The sorted character sum of the file if succesful.
            None: In case of an error.
        """
        self.get_charachter_sum()

        flat_list = []

        for k, v in self.charachter_sum.items():
            if k.isalpha():
                obj = {"char": k, "num": v}
                flat_list.append(obj)

        flat_list.sort(key=lambda f: f["num"], reverse=True)
        return flat_list
