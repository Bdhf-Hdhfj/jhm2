import pandas as pd


data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)


print("Original DataFrame:")
print(df)


print("\nAccess the 'Name' column:")
print(df['Name'])


print("\nAccess the second row using iloc:")
print(df)


