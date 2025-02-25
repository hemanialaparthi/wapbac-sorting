"""Input and process objects about people."""

from pathlib import Path
from typing import List

import typer
from rich.console import Console

from filesorter import approach, organize, person, process, profile

# create a Typer object to support the command-line interface
cli = typer.Typer()

# create a console for display of rich text
console = Console()


def prepare_person_list_for_display(person_list: List[person.Person]) -> str:
    """Process the list of people for display in the console."""
    person_list_text = ""
    # iterate through each of the people in the person_list and
    # add all of their textual details to a string; making sure to
    # preface each entry with a "-" and add a newline
    for current_person in person_list:
        person_list_text += "- " + str(current_person) + "\n"
    # return the list of generated text for each person
    return person_list_text


@cli.command()
def main(
    attribute: str = typer.Option(...),
    approach: approach.SortApproach = typer.Option(
        approach.SortApproach.lambdafunction
    ),
    input_file: Path = typer.Option(...),
    output_file: Path = typer.Option(...),
):
    """Input data about a person and then analyze and save it."""
    # display details about the file provided on the command line
    data_text = ""
    # the file was specified and it is valid so we should read and check it;
    # note that this needs to be true for both the input and output files
    if input_file.is_file():
        # read in the data from the specified file containing information about people
        console.print(
            f":abacus: Reading in the data from the specified file {input_file!s}"
        )
        data_text = input_file.read_text()
        # transform the data in the CSV file (now in a string) into a list of instances of the Person class
        console.print("")
        console.print(
            ":rocket: Parsing the data file and transforming it into people objects"
        )
        person_list = process.extract_person_data(data_text)
        # sort the data according to the specified attribute
        console.print("")
        console.print(
            f":runner: Sorting the people according to the {attribute}"
        )
        console.print("")
        console.print(f":boom: Using a sorting approach called {approach!s}")
        console.print("")
        sorted_person_list = organize.sort_persons(
            person_list, attribute, approach
        )
        # save the sorted version of the lists to the file system in the specified output directory
        console.print(
            f":sparkles: Saving the sorted people data to the file {output_file!s}"
        )
        process.write_person_data(str(output_file), sorted_person_list)
        # output the performance data that was saved
        profile.output_performance_data(console, ":microscope:")
    else:
        # the file was not specified or it is not valid so we should display an error message
        console.print(
            f":x: The specified file {input_file!s} does not exist or is not a file"
        )
