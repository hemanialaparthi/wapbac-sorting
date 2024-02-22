"""Extract and save the data about the person from the CSV file."""

import csv
from typing import List

from filesorter import person

# TODO: add a complete implementation of the:
# - extract_person_data function
# - write_person_data function
# Make sure that your implementations are tested
# through a test suite in the test_process.py file


def extract_person_data(data: str) -> List[person.Person]:
    """Extract a specified data column from the provided textual contents."""
    person_data = []
    return person_data


def write_person_data(
    file_name: str, person_data: List[person.Person]
) -> None:
    """Write the person data stored in a list to the specified file."""
    return None
