space_string = " "
# print(space_string.isspace())
# print(space_string.isalnum())
# print(space_string.isalpha())

# num_str = "1"
num_str = "一二三"

print(num_str)
# 如果 string 只包含数字则返回 True，全角数字，用的比较多
print(num_str.isdecimal())

# 如果 string 只包含数字则返回 True，全角数字、⑴、\u00b2
print(num_str.isdigit())

# 如果 string 只包含数字则返回 True，全角数字，汉字数字
print(num_str.isnumeric())

