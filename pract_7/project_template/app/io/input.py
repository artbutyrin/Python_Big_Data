import pandas as pd

def read_from_console():
    """
    Reads text input from the console

    Returns:    str: The text entered by the user
    """
    text = input("Enter text: ")
    return text


def read_from_file(filepath):
    """
    Reads text from a file using Python built-in capabilities

    Args:   filepath (str): Path to the file to read

    Returns:     str: The content of the file
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def read_from_file_pandas(filepath):
    """
    Reads data from a file using the pandas library

    Args:   filepath (str): Path to the CSV file to read

    Returns:    DataFrame: The content of the file as a pandas DataFrame
    """
    return pd.read_csv(filepath)