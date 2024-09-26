# Employee Salary Analysis

This project provides a set of functions to analyze employee salary data from a CSV file. It includes capabilities to calculate salary statistics, categorize salaries, filter employees, and check for missing phone numbers.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
- [Data Sources](#data-sources)
- [License](#license)

## Installation

To run this project, ensure you have Python 3.x installed along with the following libraries:

- pandas
- numpy

You can install the required libraries using pip (ideally in a virtual environment):

```bash
pip install pandas numpy
```

## Usage

To use the code, simply run the `main` block at the bottom of the script. This will execute all the functions defined in the script and print out relevant results.

```
python -i main.py
```
This will run the script in interactive mode. You can then check the dataframes interactively.

## Functions

### `get_employees_df()`
Fetches the employee data from a specified CSV URL.

### `get_departments_df()`
Fetches department data from a specified CSV URL and renames the department ID column.

### `salary_statistics(employees_df: pd.DataFrame) -> Dict[str, np.float64]`
Calculates the average, median, lower, and upper quartiles of employee salaries.

### `avg_salary_per_department(employees_df: pd.DataFrame, departments_df: pd.DataFrame) -> pd.DataFrame`
Calculates the average salary per department and includes the department name in the results.

### `create_salary_category(employees_df: pd.DataFrame, avg_salary: np.float64) -> pd.DataFrame`
Creates a new column `SALARY_CATEGORY` indicating whether the salary is "low" or "high" based on the average salary.

### `create_salary_catergory_among_department(employees_df: pd.DataFrame, avg_salary_per_department_df: pd.DataFrame) -> pd.DataFrame`
Creates another column `SALARY_CATEGORY_AMONG_DEPARTMENT` to indicate salary status relative to the department average.

### `filter_employees_depart_id_20(employees_df: pd.DataFrame) -> pd.DataFrame`
Filters the employee DataFrame to include only those in department ID 20.

### `increase_salary_10_perc(employees_of_depart_id_20_df: pd.DataFrame) -> pd.DataFrame`
Increases the salary by 10% for all employees working in department 20.

### `is_any_phone_number_empty(employees_df: pd.DataFrame) -> bool`
Checks if any phone numbers in the `PHONE_NUMBER` column are empty.

## Data Sources

The employee and department data are fetched from the following URLs:
- [Employees Data](https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv)
- [Departments Data](https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv)