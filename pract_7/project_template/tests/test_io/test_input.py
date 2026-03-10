import pytest
import os
from app.io.input import read_from_file, read_from_file_pandas


# Tests for read_from_file
def test_read_from_file_returns_string(tmp_path):

    f = tmp_path / "test.txt"
    f.write_text("hello world", encoding="utf-8")
    result = read_from_file(str(f))
    assert isinstance(result, str)


def test_read_from_file_correct_content(tmp_path):

    f = tmp_path / "test.txt"
    f.write_text("hello world", encoding="utf-8")
    result = read_from_file(str(f))
    assert result == "hello world"


def test_read_from_file_not_found():

    with pytest.raises(FileNotFoundError):
        read_from_file("nonexistent_file.txt")


def test_read_from_file_pandas_returns_dataframe(tmp_path):

    import pandas as pd
    f = tmp_path / "test.csv"
    f.write_text("name,age\nAlice,25\nBob,30", encoding="utf-8")
    result = read_from_file_pandas(str(f))
    assert isinstance(result, pd.DataFrame)


def test_read_from_file_pandas_correct_columns(tmp_path):

    f = tmp_path / "test.csv"
    f.write_text("name,age\nAlice,25\nBob,30", encoding="utf-8")
    result = read_from_file_pandas(str(f))
    assert list(result.columns) == ["name", "age"]


def test_read_from_file_pandas_correct_rows(tmp_path):

    f = tmp_path / "test.csv"
    f.write_text("name,age\nAlice,25\nBob,30", encoding="utf-8")
    result = read_from_file_pandas(str(f))
    assert len(result) == 2