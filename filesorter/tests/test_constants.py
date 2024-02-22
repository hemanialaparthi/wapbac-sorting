"""Test suite for the constants module."""

# ruff: noqa: PLR2004

# Note: This provides an example of a test case for the
# constants module. Please make sure that you implement
# your own test cases for all of the code in the constants module.
#
# Note: You also need to implement test cases for:
# - The constant enumeration(s) in the approach module.
# - All of the methods associated with the Person class.
# - All of the data input and storage functions in process module.
# - All of the data sorting functions in the organize module.
#
# Note: If a test case file does not exist, you need to make sure
# that you create that file and add the required test cases. 
#
# Note: You must implement test cases for all of the untested modules, excepting
# the `main` module, while further ensuring that the test suite achieves the
# desired level of code coverage. It is important to note that the coverage
# report produced by the `pytest-cov` plugin will, by default, only report the
# coverage for the test cases already defined in the `tests/` directory. This
# means that if you have not already implemented a test suite for a module it
# will not appear in the coverage report and thus the test coverage may appear
# artificially higher than it is in actuality and you will not achieve the goal.


from filesorter import constants


def test_constant_values_for_person_attributes():
    """Ensure that all of the person_attributes constants have a value."""
    assert len(vars(constants.person_attributes).items()) == 5
    for _, value in vars(constants.person_attributes).items():
        assert value is not None
