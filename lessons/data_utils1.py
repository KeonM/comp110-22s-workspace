"""Some helpful utility functions for working with CSV files"""

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table"""
    result: list[dict[str, str]] = []
    
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Read file as a csv
    csv_reader = DictReader(file_handle)
    
    # Reads each row of csv line by line
    for row in csv_reader:
        result.append(row)
    
    # Close file whrn done, to free its resources
    file_handle.close()
    
    return result


def col_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result

def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table into a column orientted table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = col_values(row_table, column)    
    
    return result