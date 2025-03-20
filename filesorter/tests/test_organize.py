"""Test the sorting functions in the organize module."""

import pytest

from filesorter.organize import (
    sort_persons_attrgetter,
    sort_persons_bubblesort,
    sort_persons_bubblesort_multilevel,
    sort_persons_customcompare,
    sort_persons_lambdafunction,
    sort_persons_quicksort,
)
from filesorter.person import Person


# TODO: Consider using this pytest test fixture to write test cases for all
# of the imported functions, listed above, that are in the organize module.

@pytest.fixture
def persons_list():
    """Create a list of Person objects for testing as a fixture."""
    return [
        Person("Alice", "USA", "1234567890", "Engineer", "alice@example.com"),
        Person("Bob", "UK", "0987654321", "Doctor", "bob@example.com"),
        Person(
            "Charlie", "Canada", "5555555555", "Artist", "charlie@example.com"
        ),
    ]


def test_sort_persons_bubblesort_multilevel_non_name_attribute(persons_list):
    # Sort by country (non-name attribute)
    sorted_persons = sort_persons_bubblesort_multilevel(persons_list, "country")
    
    # Check if the list is sorted by country
    assert sorted_persons[0].country == "Canada"
    assert sorted_persons[1].country == "UK"
    assert sorted_persons[2].country == "USA"
    
    # Check if persons with the same country are sorted by name (tie-breaker)
    assert sorted_persons[0].name == "Charlie"
    assert sorted_persons[1].name == "Bob"
    assert sorted_persons[2].name == "Alice"


def test_sort_persons_bubblesort_multilevel_email_tiebreak(persons_list):
    # Add a person with the same email as an existing person
    persons_list.append(Person("David", "Australia", "9876543210", "Manager", "alice@example.com"))
    
    # Sort by email (non-name attribute)
    sorted_persons = sort_persons_bubblesort_multilevel(persons_list, "email")
    
    # Check if the list is sorted by email
    assert sorted_persons[0].email == "alice@example.com"
    assert sorted_persons[1].email == "alice@example.com"
    assert sorted_persons[2].email == "bob@example.com"
    assert sorted_persons[3].email == "charlie@example.com"
    
    # Check if persons with the same email are sorted by name (tie-breaker)
    assert sorted_persons[0].name == "Alice"
    assert sorted_persons[1].name == "David"


def test_sort_persons_bubblesort_multilevel_same_attribute(persons_list):
    # Sort by job (assuming some persons have the same job)
    persons_list.append(Person("David", "Australia", "1111111111", "Engineer", "david@example.com"))
    sorted_persons = sort_persons_bubblesort_multilevel(persons_list, "job")
    
    # Check if the list is sorted by job
    assert sorted_persons[0].job == "Artist"
    assert sorted_persons[1].job == "Doctor"
    assert sorted_persons[2].job == "Engineer"
    assert sorted_persons[3].job == "Engineer"
    
    # Check if persons with the same job are sorted by name (first tie-breaker)
    assert sorted_persons[2].name == "Alice"
    assert sorted_persons[3].name == "David"