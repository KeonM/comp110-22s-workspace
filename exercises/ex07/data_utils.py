"""Dictionary related utility functions."""

__author__ = "730476939"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf-8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(a: list[dict[str, str]], b: str) -> list[str]:
    """Produce a `list[str]` of all values in a single `column` whose name is the second parameter."""
    result: list[str] = []
    for row in a:
        item: str = row[b]
        result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a table represented as a list of rows into one represented as a dictionary of columns."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = table[0]
    for column in first_row:
        result[column] = column_values(table, column)
    return result


def head(table: dict[str, list[str]], num_rows: int) -> dict[str, list[str]]:
    """Returns the amount of rows requested."""
    result: dict[str, list[str]] = {}
    for column in table:
        if num_rows >= len(table[column]):
            return table
        empt: list[str] = []
        for i in range(0, num_rows):
            empt.append(table[column][i])
        result[column] = empt
    return result           


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Selects only the columns that you need for data."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(columns_one: dict[str, list[str]], columns_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combines datasets for analysis."""
    result: dict[str, list[str]] = {}
    for column in columns_one:
        result[column] = columns_one[column]
    for column in columns_two:
        if column in result:
            result[column] += columns_one[column]
        else:
            result[column] = columns_two[column]
    return result


def count(vals: list[str]) -> dict[str, int]:
    """Counts how many times a certain key is called."""
    result: dict[str, int] = {}
    for item in vals:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result