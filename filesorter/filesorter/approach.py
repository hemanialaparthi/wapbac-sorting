from enum import Enum


class SortApproach(str, Enum):
    """Define the name for the approach for sorting a list contain person objects."""

    lambdafunction = "lambdafunction"
    attrgetter = "attrgetter"
    customcompare = "customcompare"

    def __str__(self):
        """Define a default string representation."""
        return self.value
