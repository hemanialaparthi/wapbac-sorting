from enum import Enum


class SortApproach(str, Enum):
    """Define the name for the approach for sorting a list contain person objects."""

    attrgetter = "attrgetter"
    bubblesort = "bubblesort"
    customcompare = "customcompare"
    lambdafunction = "lambdafunction"
    quicksort = "quicksort"

    def __str__(self):
        """Define a default string representation."""
        return self.value
