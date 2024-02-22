from typing import List

from filesorter import constants

# define the index locations for the person
person_index = constants.person_index

# define the names of the attributes for the person
person_attributes = constants.person_attributes

# ruff: noqa: PLR0913


class Person:
    """Define a Person class."""

    def __init__(
        self, name: str, country: str, phone_number: str, job: str, email: str
    ) -> None:
        """Define the constructor for a person."""
        self.name = name
        self.country = country
        self.phone_number = phone_number
        self.job = job
        self.email = email

    def __repr__(self) -> str:
        """Return a textual representation of the person."""
        return f"{self.name} is a {self.job} who lives in {self.country}. You can call this person at {self.phone_number} and email them at {self.email}"

    def create_list(self) -> List[str]:
        """Create a list of strings representing the person."""
        details = []
        details.append(self.name)
        details.append(self.country)
        details.append(self.phone_number)
        details.append(self.job)
        details.append(self.email)
        return details
