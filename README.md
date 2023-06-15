# Mean Variance Standard Deviation Calculator

This project provides a Python function, `calculate()`, that uses NumPy to calculate various statistical measures for a 3x3 matrix. The function takes a list containing 9 digits as input, converts it into a NumPy array, and returns a dictionary containing the mean, variance, standard deviation, maximum, minimum, and sum for the rows, columns, and elements of the matrix.

## Function Signature

The `calculate()` function has the following signature:

```python
def calculate(list):
    ...
```

## Input

The input to the `calculate()` function is a list containing 9 digits. The function expects exactly 9 numbers in the list. If a list with a different number of elements is provided, a `ValueError` exception is raised with the message "List must contain nine numbers."

## Output

The `calculate()` function returns a dictionary containing the statistical measures calculated from the input matrix. The dictionary has the following structure:

```python
{
  'mean': [[axis1_mean], [axis2_mean], flattened_mean],
  'variance': [[axis1_variance], [axis2_variance], flattened_variance],
  'standard deviation': [[axis1_std_dev], [axis2_std_dev], flattened_std_dev],
  'max': [[axis1_max], [axis2_max], flattened_max],
  'min': [[axis1_min], [axis2_min], flattened_min],
  'sum': [[axis1_sum], [axis2_sum], flattened_sum]
}
```

- `axis1_mean`, `axis2_mean`, and `flattened_mean` represent the mean values along the first axis (rows), second axis (columns), and the flattened matrix, respectively.
- Similarly, `axis1_variance`, `axis2_variance`, and `flattened_variance` represent the variances, and `axis1_std_dev`, `axis2_std_dev`, and `flattened_std_dev` represent the standard deviations.
- `axis1_max`, `axis2_max`, and `flattened_max` represent the maximum values, and `axis1_min`, `axis2_min`, and `flattened_min` represent the minimum values.
- `axis1_sum`, `axis2_sum`, and `flattened_sum` represent the sum of values along the respective axes.


## Unit Tests

Unit tests for the `calculate()` function are provided in the `test_module.py` file. These tests verify the correctness of the implemented calculations and can be run to ensure the function behaves as expected.

To run the unit tests, execute the `main.py` file.


The unit tests will output the test results, indicating whether each test has passed or failed.

---
Note: The `calculate()` function relies on the NumPy library, so make sure you have NumPy installed in your Python environment.
