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

# Check Missing Values
print("\nMISSING VALUES")
print(df.isnull())

# Total Missing Values
print("\nTOTAL MISSING VALUES")
print(df.isnull().sum())

# Handle Missing Values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(0)
df["City"] = df["City"].fillna("Unknown")

# Display Dataset After Handling Missing Values
print("\nAFTER HANDLING MISSING VALUES")
print(df)

# Check Data Types
print("\nDATA TYPES BEFORE CONVERSION")
print(df.dtypes)

# Convert Data Types
df["Age"] = df["Age"].astype(int)
df["Marks"] = df["Marks"].astype(int)

# Display Data Types After Conversion
print("\nDATA TYPES AFTER CONVERSION")
print(df.dtypes)

# Check Duplicate Rows
print("\nDUPLICATE ROWS")
print(df.duplicated())

# Remove Duplicate Rows
df = df.drop_duplicates()

# Display Dataset After Removing Duplicates
print("\nAFTER REMOVING DUPLICATES")
print(df)

# Final Cleaned Dataset
print("\nFINAL CLEANED DATASET")
print(df)

#Output:ORIGINAL DATASET
    Name   Age  Marks         City
0   Ravi  23.0   85.0    Hyderabad
1   Sita   NaN   90.0   Vijayawada
2  Kiran  21.0    NaN         None
3   Ravi  23.0   85.0    Hyderabad
4   None  25.0   95.0      Chennai

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
      Name   Age  Marks         City
0     Ravi  23.0   85.0    Hyderabad
1     Sita  23.0   90.0   Vijayawada
2    Kiran  21.0    0.0      Unknown
3     Ravi  23.0   85.0    Hyderabad
4  Unknown  25.0   95.0      Chennai

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

AFTER REMOVING DUPLICATES
      Name  Age  Marks         City
0     Ravi   23     85    Hyderabad
1     Sita   23     90   Vijayawada
2    Kiran   21      0      Unknown
4  Unknown   25     95      Chennai

FINAL CLEANED DATASET
      Name  Age  Marks         City
0     Ravi   23     85    Hyderabad
1     Sita   23     90   Vijayawada
2    Kiran   21      0      Unknown
4  Unknown   25     95      Chennai
