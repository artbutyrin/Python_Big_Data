def print_to_console(text):
    """
    Prints text to the console

    Args:   text (str): The text to print
    """
    print(text)


def write_to_file(text, filepath):
    """
    Writes text to a file using Python's built-in capabilities.

    Args:
        text (str): The text to write
        filepath (str): Path to the file to write to
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)