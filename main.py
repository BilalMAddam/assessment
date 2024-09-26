import typing as T
import pandas as pd
import numpy as np


def get_employees_df():
    return pd.read_csv(
        "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82"
            "ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv")


def get_departments_df():
    dep_df = pd.read_csv(
        "https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5"
            "bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv")
    dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})

    return dep_df


#
## Task 1
#
def salary_statistics(
        *,
        employees_df: pd.DataFrame
) -> T.Dict[str, np.float64]:
    """
    Calculate the average, median, lower and upper quartiles of an employees' salaries.
    """
    avg_salary = employees_df["SALARY"].mean()
    median_salary = employees_df["SALARY"].median()
    lower_quartile = employees_df["SALARY"].quantile(0.25)
    upper_quartile = employees_df["SALARY"].quantile(0.75)

    return {
        'average': avg_salary,
        'median': median_salary,
        'lower_quartile': lower_quartile,
        'upper_quartile': upper_quartile
    }


#
## Task 2
#
def avg_salary_per_department(
        *, 
        employees_df: pd.DataFrame,
        departments_df: pd.DataFrame
)-> pd.DataFrame:
    """
    calculate the average salary per department. Please include the department name in the results
    """
    avg_salary_per_depart_df = employees_df.groupby(["DEPARTMENT_ID"])["SALARY"].mean().reset_index()
    avg_salary_per_depart_df = avg_salary_per_depart_df.rename(columns={"SALARY": "AVG_SALARY"})
    avg_salary_per_department_df = pd.merge(
        avg_salary_per_depart_df,
        departments_df,
        left_on="DEPARTMENT_ID",
        right_on="DEPARTMENT_IDENTIFIER"
    )

    return avg_salary_per_department_df[["DEPARTMENT_ID", "DEPARTMENT_NAME", "AVG_SALARY"]]


#
## Task 3
#
def create_salary_category(
        *,
        employees_df: pd.DataFrame,
        avg_salary: np.float64
) -> pd.DataFrame:
    """
    Create a new column named `SALARY_CATEGORY` with value "low"
    when the salary is lower than average and "high" if is it higher or equal.
    """
    employees_df["SALARY_CATEGORY"] = employees_df["SALARY"] \
        .apply(lambda salary: "low" if (salary < avg_salary) else "high")

    return employees_df


#
## Task 4
#
def create_salary_category_among_department(
        *,
        employees_df: pd.DataFrame,
        avg_salary_per_department_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Create another column named `SALARY_CATEGORY_AMONG_DEPARTMENT` with value
    "low" when the employee salary is lower than average in his / her department and "high" in the other case.
    """
    # TODO it seems that the merge results in two salary category
    # This is not expected. An investigation must be conducted to understand the root cause of this behaviour
    merged_df = employees_df.merge(avg_salary_per_department_df, how="inner", on="DEPARTMENT_ID")
    merged_df["SALARY_CATEGORY_AMONG_DEPARTMENT"] = merged_df \
        .apply(lambda e: "low" if (e["SALARY"] < e["AVG_SALARY"]) else "high", axis=1)

    return merged_df[[*employees_df.columns, "SALARY_CATEGORY", "AVG_SALARY", "SALARY_CATEGORY_AMONG_DEPARTMENT"]]


#
## Task 5
#
def filter_employees_depart_id_20(
        *,
        employees_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Filter the dataframe `employees` to include only the rows where `DEPARTMENT_ID` equals to 20. Assign the result to new variable.
    """
    return employees_df[employees_df["DEPARTMENT_ID"] == 20]


#
## Task 6
#
def increase_salary_10_perc(
        *,
        employees_of_depart_id_20_df: pd.DataFrame
) -> pd.DataFrame:
    """
    Increase the salary by 10% for all employees working at the department 20.
    """
    # Note: The deep copy is used to avoid changing the original dataframe
    # Otherwise, we could directly work on the original dataframe
    employees_of_depart_id_20_df_copied = employees_of_depart_id_20_df.copy(deep=True)
    employees_of_depart_id_20_df_copied['SALARY'] *= 1.10

    return employees_of_depart_id_20_df_copied


#
## Task 7
#
def is_any_phone_number_empty(
        *,
        employees_df: pd.DataFrame
) -> bool:
    """
    Check if any of the `PHONE_NUMBER` column values are empty.
    """
    return employees_df['PHONE_NUMBER'].isnull().any() or (employees_df['PHONE_NUMBER'].str.strip() == '').any()


if __name__ == "__main__":
    employees_df = get_employees_df()
    departments_df = get_departments_df()

    salary_stats = salary_statistics(employees_df=employees_df)

    avg_salary_per_department_df = avg_salary_per_department(
        employees_df=employees_df,
        departments_df=departments_df
    )

    employees_df = create_salary_category(
        employees_df=employees_df,
        avg_salary=salary_stats["average"]
    )

    employees_df = create_salary_category_among_department(
        employees_df=employees_df,
        avg_salary_per_department_df=avg_salary_per_department_df
    )

    employees_of_depart_id_20_df = filter_employees_depart_id_20(employees_df=employees_df)

    employees_of_depart_id_20_df = increase_salary_10_perc(
        employees_of_depart_id_20_df=employees_of_depart_id_20_df
    )

    if is_any_phone_number_empty(employees_df=employees_df):
        print("Some phone numbers are missing!")
    else:
        print("All phone numbers are provided!")

