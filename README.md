# Data Cleaning and Pandas Fundamentals

## Introduction

This project demonstrates Data Cleaning and Pandas Fundamentals using Python. It covers handling missing values, checking data types, removing duplicate records, filtering datasets, sorting values, and saving cleaned data using the Pandas library.

---

# Technologies Used

* Python
* Pandas
* CSV Files

---

# Topics Covered

* Missing Values
* Data Types
* Duplicate Data
* Filtering Data
* Sorting Data
* CSV Operations

---

# Importing Pandas

```python
import pandas as pd
```

---

# Loading Dataset

```python
df = pd.read_csv("sample_data.csv")

print(df)
```

---

# Display First Rows

```python
print(df.head())
```

---

# Dataset Information

```python
print(df.info())
```

---

# Missing Values

## Check Missing Values

```python
print(df.isnull())
```

## Count Missing Values

```python
print(df.isnull().sum())
```

## Fill Missing Values

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)
```

## Remove Missing Values

```python
df.dropna(inplace=True)

print(df)
```

---

# Data Types

## Check Data Types

```python
print(df.dtypes)
```

## Change Data Type

```python
df["Age"] = df["Age"].astype(int)

print(df.dtypes)
```

---

# Duplicate Data

## Check Duplicate Rows

```python
print(df.duplicated())
```

## Remove Duplicate Rows

```python
df.drop_duplicates(inplace=True)

print(df)
```

---

# Selecting Columns

## Single Column

```python
print(df["Name"])
```

## Multiple Columns

```python
print(df[["Name", "Age"]])
```

---

# Filtering Data

```python
print(df[df["Age"] > 25])
```

---

# Sorting Data

## Ascending Order

```python
print(df.sort_values("Age"))
```

## Descending Order

```python
print(df.sort_values("Age", ascending=False))
```

---

# Adding New Column

```python
df["Salary"] = [50000, 60000, 45000, 70000]

print(df)
```

---

# Saving Cleaned Data

```python
df.to_csv("cleaned_data.csv", index=False)
```

---


## Project Structure

data-cleaning-and-pandas-fundamentals/
│
├── README.md
├── data_cleaning_pandas.py
├── sample_data.csv
├── cleaned_data.csv
└── requirements.txt


# Project Visualizations

## Data Cleaning Cycle

![Data Cleaning Cycle](data_cleaning_cycle.png)

## Data Cleaning Steps

![Data Cleaning Steps](data_cleaning_steps.png)

## Data Cleaning Workflow

![Data Cleaning Workflow](data_cleaning_workflow.png)


# Insights

* Missing values were successfully identified and handled.
* Dataset quality improved after cleaning operations.
* Duplicate records were detected and removed.
* Data types were checked and converted where necessary.
* Filtering helped extract specific records from the dataset.
* Sorting organized the data for easier analysis.
* Cleaned data was saved for future use and analysis.


# Conclusion

This project explains the fundamentals of Pandas and Data Cleaning techniques in Python. It demonstrates handling missing values, changing data types, removing duplicates, filtering datasets, sorting data, and saving cleaned data for further analysis.
