"""Organize the person data through the use of sorting techniques."""

# TODO: Make sure that you understand how to use all of the imported modules;
# if you are not sure how to use one of these modules ask the course instructor

import functools
import sys
from operator import attrgetter
from typing import List

from filesorter.person import Person
from filesorter.profile import timer

# Add all of the required source code to this

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


@timer("Time to Sort Person Data Using Quick Sort (ms)")
def sort_persons_quicksort(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Optimized single-attribute quicksort with median-of-three pivot"""
    if len(persons) <= 1:
        return persons

    # Precompute attribute getter
    get_attr = attrgetter(attribute)
    stack = [(0, len(persons) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        
        # Median-of-three pivot selection
        mid = (low + high) // 2
        if get_attr(persons[high]) < get_attr(persons[low]):
            persons[low], persons[high] = persons[high], persons[low]
        if get_attr(persons[mid]) < get_attr(persons[low]):
            persons[mid], persons[low] = persons[low], persons[mid]
        if get_attr(persons[high]) < get_attr(persons[mid]):
            persons[high], persons[mid] = persons[mid], persons[high]
        
        pivot_val = get_attr(persons[mid])
        i, j = low, high
        
        while i <= j:
            while get_attr(persons[i]) < pivot_val:
                i += 1
            while get_attr(persons[j]) > pivot_val:
                j -= 1
            if i <= j:
                persons[i], persons[j] = persons[j], persons[i]
                i += 1
                j -= 1
        
        # Push smaller partition first
        if (j - low) < (high - i):
            stack.append((low, j))
            stack.append((i, high))
        else:
            stack.append((i, high))
            stack.append((low, j))
    
    return persons


@timer("Time to Sort Person Data Using Quick Sort with Multi-Level Sorting (ms)")
def sort_persons_quicksort_multilevel(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Optimized multi-level quicksort with early comparison shortcut"""
    if len(persons) <= 1:
        return persons

    # Define tie-breakers and precompute getters
    tie_breakers = ["name", "country", "phone_number", "email"]
    keys = [attribute] + tie_breakers
    getters = [attrgetter(key) for key in keys]
    
    stack = [(0, len(persons) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low >= high:
            continue
        
        # Median-of-three pivot selection
        mid = (low + high) // 2
        if getters[0](persons[high]) < getters[0](persons[low]):
            persons[low], persons[high] = persons[high], persons[low]
        if getters[0](persons[mid]) < getters[0](persons[low]):
            persons[mid], persons[low] = persons[low], persons[mid]
        if getters[0](persons[high]) < getters[0](persons[mid]):
            persons[high], persons[mid] = persons[mid], persons[high]
        
        pivot = persons[mid]
        pivot_vals = [getter(pivot) for getter in getters]
        i, j = low, high
        
        while i <= j:
            # Left scan with early exit
            while True:
                left_primary = getters[0](persons[i])
                if left_primary != pivot_vals[0]:
                    if left_primary >= pivot_vals[0]:
                        break
                    i += 1
                    continue
                
                left_vals = [left_primary] + [getter(persons[i]) for getter in getters[1:]]
                if left_vals >= pivot_vals:
                    break
                i += 1
            
            # Right scan with early exit
            while True:
                right_primary = getters[0](persons[j])
                if right_primary != pivot_vals[0]:
                    if right_primary <= pivot_vals[0]:
                        break
                    j -= 1
                    continue
                
                right_vals = [right_primary] + [getter(persons[j]) for getter in getters[1:]]
                if right_vals <= pivot_vals:
                    break
                j -= 1
            
            if i <= j:
                persons[i], persons[j] = persons[j], persons[i]
                i += 1
                j -= 1
        
        # Push smaller partition first
        if (j - low) < (high - i):
            stack.append((low, j))
            stack.append((i, high))
        else:
            stack.append((i, high))
            stack.append((low, j))
    
    return persons


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


@timer("Time to Sort Person Data Using Timsort (ms)")
def sort_persons_timsort(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects using Timsort based on a single attribute."""
    # Use Timsort (Python's built-in sorted function) with the attribute as the key
    sorted_persons = sorted(persons, key=attrgetter(attribute))
    return sorted_persons


@timer("Time to Sort Person Data Using Timsort with Multi-Level Sorting (ms)")
def sort_persons_timsort_multilevel(
    persons: List[Person], attribute: str
) -> List[Person]:
    """Sort a list of Person objects using Timsort with multi-level comparison"""
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