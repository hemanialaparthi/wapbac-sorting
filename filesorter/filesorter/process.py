"""Extract and save the data about the person from the CSV file."""

import csv
from typing import List

from filesorter import person

# add a complete implementation of the:
# - extract_person_data function
# - write_person_data function
# Make sure that your implementations are tested
# through a test suite in the test_process.py file

# make sure to add type annotations for the
# parameters and return values for the functions

NUM_OF_HEADERS = 5


def extract_person_data(data: str) -> List[person.Person]:
    """Extract a specified data column from the provided textual contents."""
    # create a empty list
    person_data = []
    # split the data into lines and create a reader
    reader = csv.reader(data.splitlines())

    # iterate through each line and create a Person instance for each line
    for line in reader:
        # check if the line has enough elements (headers)
        if len(line) < NUM_OF_HEADERS:
            # if it is, then continue
            continue
        # extract the data from the line and create a Person instance
        name, country, phone_number, job, email = line
        # create a Person instance and append it to the list
        person_instance = person.Person(
            name, country, phone_number, job, email
        )
        # append the Person instance to the list of person data
        person_data.append(person_instance)
    # return the list of person data
    return person_data


def write_person_data(
    data: str, person_data: List[person.Person]
) -> None:
    """Write the person data stored in a list to the specified file."""
    converted_person_data = []

    # add headers for the CSV file (for myself purposes lol)
    # headers = ["Name", "Country", "Phone Number", "Job", "Email"]
    # converted_person_data.append(headers)

    # convert each person instance to a list and append to the data
    for person_instance in person_data:
        # convert the person instance to a list and append to the data list
        converted_person_data.append(person_instance.create_list())

    # write the data to the CSV file
    with open(data, "w", newline="", encoding="utf-8") as csvfile:
        # create a CSV writer
        writer = csv.writer(csvfile)
        # write the data to the CSV file
        writer.writerows(converted_person_data)
