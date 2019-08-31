name_list = ["c","a","b","c"]
list_len = len(name_list)
print("name_list的列表长度为%d" % list_len)

list_count = name_list.count("c")
print("c出现了%d次" % list_count)

name_list.remove("c")

print(name_list)