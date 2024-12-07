import pandas as pd

Data = {
    'Date': [],  # 鍵 'Name' 對應的值是一個列表
    'Category': [],                  # 鍵 'Age' 對應的值是一個列表
    'Amount': [],
    'Type': []  # 鍵 'City' 對應的值是一個列表
}
df = pd.DataFrame(Data)
A = "\nPersonal Expense Tracker\n1.Add Transaction\n2. Edit Transaction\n3. Delete Transaction\n4.View Summary\n5.Save and Exit\nEnter your choice: "
B = input(A)
while B != "5":
    if B == "1":
        print("Add Transaction")
        C = input("Enther the date (YYYY-MM-DD): ")
        D = input("Enther the category (e.g, Food, Transport): ")
        E = float(input("Enter the amount: "))
        F = input("Enter the type (Expense/Income): ")
        df.loc[len(df.index)] = [C, D, E, F]
        print("Transaction added successfully.")
        print(df)
    elif B == "2":
        print("Edit Transaction")
        G = int(input("Enter the transaction index to edit: "))
        print("Current transaction details: ")
        print(df.iloc[G])
    elif B == "3":
        print("Delete Transaction")
    elif B == "4":
        print("View Summary")
    else:
        print("Try again")

    B = input(A)
