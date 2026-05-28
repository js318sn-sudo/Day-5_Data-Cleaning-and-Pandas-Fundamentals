import pandas as pd
data={
  "Name":["Ram", "sam", "Sam"],
  "Marks":[90, 85, 85]
}
df = pd.DataFrame(data)
print("Duplicate Rows:")
print(df.duplicated())
# Output:
# 0     False
# 1     False
# 2     True
