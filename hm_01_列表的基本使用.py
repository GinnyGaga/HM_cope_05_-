name_list = ["ginny","lamber","momo"]
# 取值
print(name_list[2])
# 取索引
print(name_list.index("momo"))
# 修改
name_list[1] = "兰博"
# 增加
name_list.append("papa")
# 插入
name_list.insert(1,"and")
# 追加
list_temp = ["apple","banana","orange","what"]
# 删除
name_list.extend(list_temp)
name_list.remove("and")
name_list.pop()
name_list.pop(2)
name_list.clear()





print(name_list)