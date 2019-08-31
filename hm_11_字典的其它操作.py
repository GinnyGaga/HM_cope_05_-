Ginny_dict ={"name":"ginny",
             "age":18}
# 1、统计键值对的数量
print(len(Ginny_dict))
# 2、合并字典
temp_dict = {"height":162,
             "weight":100}
Ginny_dict.update(temp_dict)
# 3、删除指定键值对
del Ginny_dict["weight"]
# 4、随机删除一个键值对
Ginny_dict.popitem()
# 清空字典
Ginny_dict.clear()

print(Ginny_dict)