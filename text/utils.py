import glob


def append_files_from_path(path: str) -> str:
    """Given a path to a list of .txt files return a string
    of the concatenated contents of the file."""
    paths = glob.glob(path + "/*.txt")
    text = ""
    for path in paths:
        with open(path, "r") as f:
            read_text = f.read()
            text += read_text
    return text


text = append_files_from_path("../data/debates")


from typing import List


def flatten_list_of_lists(l: List[List[str]]) -> List[str]:
    """do a thing...
    """
    return " ".join(l)
