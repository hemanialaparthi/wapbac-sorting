from enum import Enum


class SortApproach(str, Enum):
    """Define the cool name for the approach for sorting a list contain person objects"""

    bubblesort = "bubblesort"
    timsort = "timsort"
    quicksort = "quicksort"
    bubblesort_multilevel = "bubblesort_multilevel"
    timsort_multilevel = "timsort_multilevel"
    quicksort_multilevel = "quicksort_multilevel"

    def __str__(self):
        """Define a default string representation"""
        return self.value
