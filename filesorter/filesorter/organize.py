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


def quicksort(arr, keys):
    """Sort a list of dictionaries based on multiple keys using quicksort."""
    if len(arr) <= 1:
        return arr  # Base case: if the array has 1 or 0 elements, it's already sorted
    pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
    # Partition the array into three parts: less than, equal to, and greater than the pivot
    left = [x for x in arr if tuple(getattr(x, key) for key in keys) < tuple(getattr(pivot, key) for key in keys)]
    middle = [x for x in arr if tuple(getattr(x, key) for key in keys) == tuple(getattr(pivot, key) for key in keys)]
    right = [x for x in arr if tuple(getattr(x, key) for key in keys) > tuple(getattr(pivot, key) for key in keys)]
    # Recursively sort the left and right parts and concatenate them with the middle part
    return quicksort(left, keys) + middle + quicksort(right, keys)


@timer("Time to Sort Person Data Using Timsort with Multi-Level Sorting (ms)")
def sort_persons_timsort_multilevel(
    persons: List[Person], attribute: str
) -> List[Person]:
    """
    Sort a list of Person objects using Timsort with multi-level comparison.

    :param persons: List of Person objects to sort.
    :param attribute: Primary attribute to sort by.
    :return: Sorted list of Person objects.
    """
    # Define the tie-breaking attributes (e.g., secondary and tertiary attributes)
    tie_breaking_attributes = ["name", "country", "phone_number", "job", "email"]

    # Create a composite key function for multi-level sorting
    def composite_key(person: Person):
        primary_value = getattr(person, attribute)
        tie_values = tuple(getattr(person, tie_attr) for tie_attr in tie_breaking_attributes)
        return (primary_value, *tie_values)

    # Use Timsort (Python's built-in sorted function) with the composite key
    sorted_persons = sorted(persons, key=composite_key)
    return sorted_persons

@timer("Time to Sort Person Data Using Iterative Quick Sort (ms)")
def sort_persons_quicksort(
        persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects based on a given attribute using the iterative quick sort approach."""
    def partition(low, high):
        pivot = getattr(persons[high], attribute)
        i = low - 1
        for j in range(low, high):
            # move elements less than pivot to the left
            if getattr(persons[j], attribute) <= pivot:
                i += 1
                persons[i], persons[j] = persons[j], persons[i]
        persons[i+1], persons[high] = persons[high], persons[i+1]
        return i+1

    stack = [(0, len(persons) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = partition(low, high)
            # Push sub-array to stack for further sorting
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
    return persons


@timer("Time to Sort Person Data Using Quick Sort with Multi-Level Sorting (ms)")
def sort_persons_quicksort_multilevel(
    persons: List[Person], attribute: str
) -> List[Person]:
    """
    Sort a list of Person objects using Quick Sort with multi-level comparison.

    :param persons: List of Person objects to sort.
    :param attribute: Primary attribute to sort by.
    :return: Sorted list of Person objects.
    """
    # Define the tie-breaking attributes (e.g., secondary and tertiary attributes)
    tie_breaking_attributes = ["name", "country", "phone_number", "job", "email"]
    keys = [attribute] + [attr for attr in tie_breaking_attributes if attr != attribute]
    return quicksort(persons, keys)


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
