# 筆記 01 - 基本概念

# 1. Python 基本概念
# -----------------
# Python 是由 Guido van Rossum 創建的高級編程語言
# 特點：解釋型語言，動態類型

# 2. 數據類型示例
# -------------
# 字符串
text = "Python"  # 字符串類型，用於處理文本

# 數字
integer_num = 42  # 整數類型
float_num = 19.99  # 浮點數類型

# 布爾值
is_valid = True  # 布爾類型，表示真或假

# 3. 輸入輸出操作
# -------------
# 基本輸出
print("你好，世界")  # 顯示文本到控制台

# 獲取用戶輸入
name = input("請輸入姓名: ")  # 接收用戶輸入
age = int(input("請輸入年齡: "))  # 將輸入轉換為整數

# 4. 算術運算
# ----------
a = 10
b = 3

# 基本運算示例
addition = a + b      # 加法：13
subtract = a - b      # 減法：7
multiply = a * b      # 乘法：30
divide = a / b        # 除法：3.333...
floor_div = a // b    # 整除：3
modulus = a % b       # 取餘：1
power = a ** 2        # 冪運算：100

# 重要提醒：
# 1. 運算優先級：括號、指數、乘除、加減（PEMDAS）
# 2. 處理數值輸入時記得做類型轉換
# 3. 格式化輸出推薦使用 f-string
# 例如：print(f"結果是：{result}")

# 字符串格式化示例
name = "小明"
age = 20
print(f"我叫{name}，今年{age}歲")  # 使用 f-string 進行格式化輸出