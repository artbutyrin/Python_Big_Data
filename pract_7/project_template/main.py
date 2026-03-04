import pandas as pd
from app.io.input import read_from_console, read_from_file, read_from_file_pandas
from app.io.output import print_to_console, write_to_file

def main():
    console_text = read_from_console()

    file_text = read_from_file("data/sample.txt")

    pandas_data = read_from_file_pandas("data/sample.csv")
    pandas_text = pandas_data.to_string()

    print_to_console(console_text)
    print_to_console(file_text)
    print_to_console(pandas_text)

    write_to_file(console_text + "\n" + file_text + "\n" + pandas_text, "data/output.txt")

if __name__ == "__main__":
    main()