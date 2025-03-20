"""Organize the person data through the use of sorting techniques."""

# TODO: Make sure that you understand how to use all of the imported modules;
# if you are not sure how to use one of these modules ask the course instructor

import functools
import sys
from operator import attrgetter
from typing import List

from filesorter.person import Person
from filesorter.profile import timer

# Add all of the required source code to this module

# Consider using the timer decorator so that you
# can easily collect performance data for the sorting functions


@timer("Time to Sort Person Data Using Bubble Sort (ms)")
def sort_persons_bubblesort(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the bubble sort approach."""
    length_of_persons = len(persons)
    for i in range(length_of_persons):
        for j in range(0, length_of_persons - i - 1):
            if getattr(persons[j], attribute) > getattr(
                persons[j + 1], attribute
            ):
                persons[j], persons[j + 1] = persons[j + 1], persons[j]
    return persons


@timer("Time to Sort Person Data Using Bubble Sort with Multi-Level Sorting (ms)")
def sort_persons_bubblesort_multilevel(
    persons: List[Person], attribute: str
) -> List[Person]:
    """
    Sort a list of Person objects using Bubble Sort with multi-level comparison.

    :param persons: List of Person objects to sort.
    :param attribute: Primary attribute to sort by.
    :return: Sorted list of Person objects.
    """
    # Define the tie-breaking attributes (e.g., secondary and tertiary attributes)
    tie_breaking_attributes = ["name", "country", "phone_number", "job", "email"]

    length_of_persons = len(persons)
    for i in range(length_of_persons):
        for j in range(0, length_of_persons - i - 1):
            # Compare records based on the primary attribute
            value1 = getattr(persons[j], attribute)
            value2 = getattr(persons[j + 1], attribute)

            if value1 == value2:
                # If values are equal, use tie-breaking attributes
                swap = False
                for tie_attr in tie_breaking_attributes:
                    tie_value1 = getattr(persons[j], tie_attr)
                    tie_value2 = getattr(persons[j + 1], tie_attr)
                    if tie_value1 > tie_value2:
                        swap = True
                        break
                    elif tie_value1 < tie_value2:
                        break
            else:
                # If values are not equal, determine if a swap is needed
                swap = value1 > value2

            # Swap if necessary
            if swap:
                persons[j], persons[j + 1] = persons[j + 1], persons[j]
    return persons


@timer("Time to Sort Person Data Using Iterative Quick Sort (ms)")
def sort_persons_quicksort(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the iterative quick sort approach."""
    # TODO: implement the iterative quick sort algorithm to sort the list of people
    # NOTE: If you decide to use the timer decorator it may be easier for you
    # to collect the timing data for the quick sort algorithm by using iteration
    return []


def sort_persons(
    persons: List[Person], attribute: str, approach: str
) -> List[Person]:
    """Sort the list of Person objects according to the requested approach."""
    # extract the name of the current module and the sorting function
    module_name = sys.modules[__name__]
    function_name = f"sort_persons_{approach}"
    # call the function that was built up and return its result
    # note that the sorting function will be called with the
    # list of the people and the provided attribute of a person
    if not hasattr(module_name, function_name):
        raise ValueError(f"Invalid sorting approach: {approach}")
    sorting_function = getattr(module_name, function_name)
    sorted_persons = sorting_function(persons, attribute)
    return sorted_persons


def sort_persons_lambdafunction(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the lambdafunction approach."""
    # TODO: define a dictionary mapping attribute names to their corresponding
    # Person attributes; make sure to use a lambda function to extract the property
    # TODO: ensure that the provided attribute is valid; raise a ValueError
    # if the attribute is not valid and thus sorting cannot be performed
    # TODO: sort the list using the attribute as the sorting key
    # TODO: return the sorted list of people data
    return []


def sort_persons_attrgetter(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the attrgetter approach."""
    # TODO: define a dictionary mapping attribute names to their corresponding
    # Person attributes; make sure to use the getattr function to extract the property
    # TODO: ensure that the provided attribute is valid; raise a ValueError
    # if the attribute is not valid and thus sorting cannot be performed
    # TODO: sort the list using the attribute as the sorting key
    # TODO: return the sorted list of people data
    return []


def sort_persons_customcompare(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the customcompare approach."""

    def compare_persons(person_one: Person, person_two: Person) -> int:
        """Compare two people using the provided attribute."""
        # TODO: extract the attribute values from the two people;
        # this should use the getarr function to extract the
        # attribute from the person object
        # TODO: compare the two people using lexical ordering
        # and return the standard code for a comparison function;
        # see the project documentation for the three return values
        return 0

    # TODO: confirm that an instance of Person has the specified attribute
    # TODO: sort the list using the attribute as the key
    # TODO: return the sorted list of people data
    return []
