 
import pandas as pd

# Sample Dataset
data = {
    "Name": ["Ravi", "Sita", "Kiran", "Ravi", None],
    "Age": [23, None, 21, 23, 25],
    "Marks": [85, 90, None, 85, 95],
    "City": ["Hyderabad", "Vijayawada", None, "Hyderabad", "Chennai"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display Original Dataset
print("ORIGINAL DATASET")
print(df)

# Display Dataset Shape
print("\nDATASET SHAPE")
print(df.shape)

# Check Missing Values
print("\nMISSING VALUES")
print(df.isnull())

# Count Total Missing Values
print("\nTOTAL MISSING VALUES")
print(df.isnull().sum())

# Replace Missing Values
df["Name"] = df["Name"].fillna("Unknown")

# Replace missing Age values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Replace missing Marks values with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Replace missing City values
df["City"] = df["City"].fillna("Unknown")

# Display Dataset After Handling Missing Values
print("\nAFTER HANDLING MISSING VALUES")
print(df)

# Display Statistical Summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Display Data Types Before Conversion
print("\nDATA TYPES BEFORE CONVERSION")
print(df.dtypes)

# Convert float values into integer type
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)

# Display Data Types After Conversion
print("\nDATA TYPES AFTER CONVERSION")
print(df.dtypes)

# Check Duplicate Rows
print("\nDUPLICATE ROWS")
print(df.duplicated())

# Display Duplicate Records
print("\nDUPLICATE RECORDS")
print(df[df.duplicated()])

# Remove Duplicate Rows
df = df.drop_duplicates()

# Display Dataset After Removing Duplicates
print("\nAFTER REMOVING DUPLICATES")
print(df)

# Display Final Dataset Shape
print("\nFINAL DATASET SHAPE")
print(df.shape)

# Display Final Cleaned Dataset
print("\nFINAL CLEANED DATASET")
print(df) 

# Output:
ORIGINAL DATASET
    Name   Age  Marks        City
0   Ravi  23.0   85.0   Hyderabad
1   Sita   NaN   90.0  Vijayawada
2  Kiran  21.0    NaN        None
3   Ravi  23.0   85.0   Hyderabad
4   None  25.0   95.0     Chennai

DATASET SHAPE
(5, 4)

MISSING VALUES
    Name    Age  Marks   City
0  False  False  False  False
1  False   True  False  False
2  False  False   True   True
3  False  False  False  False
4   True  False  False  False

TOTAL MISSING VALUES
Name     1
Age      1
Marks    1
City     1
dtype: int64

AFTER HANDLING MISSING VALUES
      Name   Age  Marks        City
0     Ravi  23.0  85.00   Hyderabad
1     Sita  23.0  90.00  Vijayawada
2    Kiran  21.0  88.75     Unknown
3     Ravi  23.0  85.00   Hyderabad
4  Unknown  25.0  95.00     Chennai

STATISTICAL SUMMARY
             Age      Marks
count   5.000000   5.000000
mean   23.000000  88.750000
std     1.414214   4.145781
min    21.000000  85.000000
25%    23.000000  85.000000
50%    23.000000  88.750000
75%    23.000000  90.000000
max    25.000000  95.000000

DATA TYPES BEFORE CONVERSION
Name      object
Age      float64
Marks    float64
City      object
dtype: object

DATA TYPES AFTER CONVERSION
Name     object
Age       int64
Marks     int64
City     object
dtype: object

DUPLICATE ROWS
0    False
1    False
2    False
3     True
4    False
dtype: bool

DUPLICATE RECORDS
   Name  Age  Marks       City
3  Ravi   23     85  Hyderabad

AFTER REMOVING DUPLICATES
      Name  Age  Marks        City
0     Ravi   23     85   Hyderabad
1     Sita   23     90  Vijayawada
2    Kiran   21     88     Unknown
4  Unknown   25     95     Chennai

FINAL DATASET SHAPE
(4, 4)

FINAL CLEANED DATASET
      Name  Age  Marks        City
0     Ravi   23     85   Hyderabad
1     Sita   23     90  Vijayawada
2    Kiran   21     88     Unknown
4  Unknown   25     95     Chennai

