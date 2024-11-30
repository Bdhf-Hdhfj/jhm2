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
print(df.iloc[1])


df['Salary'] = [70000, 80000, 75000]
print("\n添加 'Salary' 列后的 DataFrame:")
print(df)


filtered_df = df[df['Age'] > 28]
print("\n年龄大于 28 的过滤后 DataFrame:")
print(filtered_df)


average_salary = df['Salary'].mean()
print(f"\n平均工资: {average_salary}")