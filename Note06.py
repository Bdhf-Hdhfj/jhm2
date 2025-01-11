# CSV

import pandas as pd

# 1. 建立與儲存 CSV 檔案
# 建立範例資料
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard'],  # 產品名稱
    'Price': [1000, 50, 80],                    # 價格
    'Stock': [10, 100, 50]                      # 庫存數量
}
df = pd.DataFrame(data)

# 將資料儲存到 CSV 檔案
filename = 'products.csv'
df.to_csv(filename, index=False)
print(f"資料已儲存到 {filename}")

# 2. 從 CSV 載入資料
try:
    loaded_df = pd.read_csv(filename)
    print(f"\n從 {filename} 載入的資料：")
    print(loaded_df)
except FileNotFoundError:
    print(f"\n檔案 {filename} 不存在！")

# 3. 新增資料到 CSV
# 新增一筆新資料，並存回 CSV
new_row = {
    'Product': 'Monitor',  # 產品名稱
    'Price': 200,          # 價格
    'Stock': 20            # 庫存數量
}
loaded_df.loc[len(loaded_df)] = new_row  # 加入新資料
loaded_df.to_csv(filename, index=False)  # 儲存回 CSV
print(f"\n新增資料後的 CSV 檔案內容：")
print(pd.read_csv(filename))

# 4. 更新 CSV 資料
# 修改指定行的資料
loaded_df.loc[1, 'Price'] = 45  # 修改第 1 行的價格
loaded_df.to_csv(filename, index=False)  # 儲存修改後的資料
print(f"\n更新價格後的資料：")
print(pd.read_csv(filename))

# 5. 刪除資料
# 刪除第 0 行的資料
loaded_df = loaded_df.drop(0)
loaded_df.to_csv(filename, index=False)
print(f"\n刪除第 0 行後的資料：")
print(pd.read_csv(filename))

# 6. 篩選 CSV 資料
# 篩選出庫存大於 20 的項目
filtered_df = loaded_df[loaded_df['Stock'] > 20]
print(f"\n庫存大於 20 的項目：")
print(filtered_df)

# 7. 總結數據
# 計算價格總和和平均庫存
total_price = loaded_df['Price'].sum()
average_stock = loaded_df['Stock'].mean()
print(f"\n總價格: {total_price}, 平均庫存: {average_stock}")

# 8. 處理不存在的 CSV
try:
    df_nonexistent = pd.read_csv('nonexistent.csv')
except FileNotFoundError:
    print("\n檔案 nonexistent.csv 不存在，建立空的 DataFrame")
    df_nonexistent = pd.DataFrame(columns=['Product', 'Price', 'Stock'])
    print(df_nonexistent)