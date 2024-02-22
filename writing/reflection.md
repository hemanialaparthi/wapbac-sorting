# File Sorting

## Table of Contents

<!---toc start-->

<!-- TODO: Use one of the tasks specified in the `pyproject.toml` file -->
<!-- to add the required table of contents. -->

<!---toc end-->

## Add Your Name Here

## Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."

TODO: You must retype the sentence here in order to digitally sign your pledge.

"I adhered to the Allegheny College Honor Code while completing this project."

**IMPORTANT:** If you do not type the required sentence then the course
instructor will not know that you adhered to the Allegheny College Honor Code
while completing the project.

## Program Output

### Report at least two examples of program output from when you ran the `systemsense` program

#### First output from running the `systemsense` program

TODO: Add an output from running the specified program

#### Second output from running the `systemsense` program

TODO: Add an output from running the specified program

### Use two fenced code blocks to provide output from five different runs of `filesorter` with five different inputs

TODO: Provide the complete command-line for your use of the `filesorter` program

#### Provide the command the output for the first run of the `filesorter`

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that this run is for one of the three unique approaches

#### Provide the command the output for the second run of the `filesorter`

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that this run is for one of the three unique approaches

#### Provide the command the output for the third run of the `filesorter`

TODO: Provide your own example of a command and the output that it produces
TODO: Make sure that this run is for one of the three unique approaches

## Experiment Design

Describe your design of the `filesorter` experiment that answers your own
research questions (as specified in the next subsection), focusing on these key
issues:

- **Data file**: either subsets of or the entire `input/people.txt` file or
alternative files that contain rows of data with `Person` attributes that can be
parsed and then transformed into instances of the `Person` class; this aspect of
the experiment may also investigate both the number of rows inside of the data
file and the contents of each row inside of the data file.
- **Input time**: the time overhead associated with reading in the specified
data file.
- **Output time**: the time overhead associated with writing to a specified file
all the details about each matching instance of the `Person` class.
- **Sorting time**: the time overhead associated with sorting the in-memory
representation of the input data file stored in a list of `Person` objects.

The **Sorting time** is a critical part of the experiment and, as you study it,
please make sure that you consider how the performance of sorting may be
influenced by, for instance, the size and contents of the data file and the
attribute that was chosen to organize the data file. Please note that you must
justify every part of your experiment design and then furnish output examples to
demonstrate that your program generates correct data! Finally, don't forget that
you should not start to run your experiments until you are convinced that the
each sorting algorithm configuration produces the correct output file.

## Research Questions

TODO: Clearly state at least three research questions that you want to ask and
answer by using the `filesorter` program. You should provide the research
questions in a list that starts with "RQ" and ends with a question mark. Here
are some high-level questions, designated with the letter **Q**, that you may
consider as motivating questions for your actual research questions:

- **Q1**: What is the running time and/or complexity class of the sorting algorithm provided by `sorted`?
- **Q2**: How does the runtime of the sorting algorithms change as the input size increases?
- **Q3**: How is it possible to systematically increase the size of the specified data file?
- **Q4**: What is the time overhead associated with reading in the specified data file?
- **Q5**: What is the time overhead associated with writing data to the specified data file?

TODO: Although the statement of three research questions is required for the
baseline associated with this project, you may need to state and answer
additional questions in order to develop a full-featured understanding of the
performance trade-offs evident through the use of the `filesorter`.

TODO: You must add instrumentation using tools like `timeit` to ensure that the
`filesorter` calculates and reports the time overhead data that you will
need to answer your research questions. Before you conduct your experiments,
please carefully confirm that `filesorter` calculates and reports the time
overhead values in a correct fashion.

## Data Tables

TODO: Use Markdown to provide one or more data tables that summarize the results
from running the `filesorter` program in different configurations. You should
provide enough data tables and output values to ensure that you can answer all
of your research questions and, if possible, use the empirical results to
classify the likely worst-case time complexity of each of the sorting algorithm
configurations that you studied in this algorithm engineering project.

## Performance Analysis

TODO: Provide at least three paragraphs that explain which configuration of the
sorting algorithm inside of the `filesorter` are the fastest, by how much they
are faster, and how you knew that the sorting algorithm configuration was
faster, referencing the data in the aforementioned command outputs and the data
tables to support your response. You should make sure that you answer at least
three research questions that you posed in a previous section of this report.

TODO: Make sure that your responses explain WHY certain configurations are faster!

TODO: It is not sufficient to ONLY explain WHICH configuration is faster!

## Professional Development

### What are the benefits and drawbacks of the three approaches to sorting in Python?

TODO: Provide a one-paragraph response that answers this question in your own words.

TODO: Your response can discuss either issues about algorithmic performance or
software engineering concerns.

### What is challenging about designing an experiment to evaluate the performance of sorting?

TODO: Provide a one-paragraph response that answers this question in your own words.

### How do the empirical results suggest that you don't yet know the entire story about the performance of sorting?

TODO: Provide a one-paragraph response that answers this question in your own words.

## Take Home Points

TODO: Provide a two to three sentence statement about the key takeaways from
conducting this experiment. Please note that the course instructor will display
some student takeaways on the course web site and use them to facilitate
follow-on class discussions.
