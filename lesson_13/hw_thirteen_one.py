"""This module compares two csv files."""

import csv


def create_list_from_csv(file_path):
    """
    Read a CSV file and create a list of its rows.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        list: A list where each element is a row from the CSV file.
    """
    rows = []
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(tuple(row))
    return rows


def remove_duplicates_from_two_lists(list1, list2):
    """
    Combine two lists and remove duplicate rows.

    Args:
        list1 (list): The first list of rows.
        list2 (list): The second list of rows.

    Returns:
        list: A list of unique rows.
    """
    combined_set = set(list1) | set(list2)
    return [list(row) for row in combined_set]


def write_to_csv(file_path, rows):
    """
    Write a list of rows to a CSV file.

    Args:
        file_path (str): Path to the output CSV file.
        rows (list): List of rows to write.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def process_csv_files(file1, file2, output_file):
    """
    Read two CSV files, remove duplicates, and write
     the unique rows to a new file.

    Args:
        file1 (str): Path to the first CSV file.
        file2 (str): Path to the second CSV file.
        output_file (str): Path to the output CSV file.
    """
    list1 = create_list_from_csv(file1)
    list2 = create_list_from_csv(file2)
    unique_rows = remove_duplicates_from_two_lists(list1, list2)
    write_to_csv(output_file, unique_rows)
    print(f'Unique rows written to {output_file}')


process_csv_files('r-m-c.csv', 'rmc.csv', 'result_c.csv')
