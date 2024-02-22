"""Organize the person data through the use of sorting techniques."""

# TODO: Make sure that you understand how to use all of the imported modules;
# if you are not sure how to use one of these modules ask the course instructor

import functools
import sys
from operator import attrgetter
from typing import List

from filesorter.person import Person

# TODO: Add all of the required source code to this module


def sort_persons(
    persons: List[Person], attribute: str, approach: str
) -> List[Person]:
    """Sort the list of Person objects according to the requested approach."""
    # TODO: extract the name of the current module and the sorting function
    # TODO: call the function that was built up and return its result
    # note that the sorting function will be called with the
    # list of the people and the provided attribute of a person
    return []


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
