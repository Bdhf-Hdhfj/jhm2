# 控制流程

# 條件語句 if-elif-else
# 基本結構示例
age = 18
if age < 18:
    print("未成年")  # 如果年齡小於18
elif age == 18:
    print("剛好成年")  # 如果年齡等於18
else:
    print("成年")  # 其他情況

# 循環語句
# while循環：不確定循環次數時使用
# 示例：計算1到10的和
sum = 0
i = 1
while i <= 10:  # 當i小於等於10時持續執行
    sum += i # sum = sum + 1
    i += 1  # 記得更新計數器，否則會無限循環 | i = i + 1

# for循環：已知循環次數時使用
# 示例：打印列表元素
fruits = ["蘋果", "香蕉", "橙子"]
for fruit in fruits:  # 遍歷列表中的每個元素
    print(fruit)

# 循環控制
# break: 跳出整個循環
# 當找到特定水果時跳出循環
fruits = ["蘋果", "香蕉", "橙子"]
for fruit in fruits:
    if fruit == "香蕉":
        print("找到香蕉了！停止搜索。")
        break
    print(fruit)
    
# continue: 跳過當前迭代
# 跳過打印香蕉
fruits = ["蘋果", "香蕉", "橙子"]
for fruit in fruits:
    if fruit == "香蕉":
        continue
    print(fruit)
    
# pass: 空語句，用作佔位符
# 使用pass作為佔位符
for fruit in fruits:
    if fruit == "香蕉":
        pass  # 不做任何事，純佔位
    else:
        print(fruit)

# 異常處理
try:
    result = 10 / 0  # 可能發生錯誤的代碼
except ZeroDivisionError:
    print("除數不能為零")  # 處理特定錯誤
except Exception as e:
    print(f"發生錯誤：{e}")  # 處理其他錯誤
else:
    print("執行成功")  # 沒有錯誤時執行
finally:
    print("總是執行")  # 無論是否發生錯誤都執行

# 重要知識點：
# 1. 條件判斷要注意邏輯運算符的使用（and, or, not）
# 2. 循環時注意避免無限循環
# 3. 異常處理要針對具體錯誤類型進行處理
# 4. 代碼縮進很重要，Python用縮進表示代碼塊