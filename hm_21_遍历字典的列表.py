students =[
    {"name":"ginny"},
    {"name":"lamber"}
]
name_found = "gin"
for name_a in students:
    print(name_a)
    if name_a["name"] == name_found:
        print("找到 %s 了" % name_found)
        break
else:
    print("没有找到 %s " % name_found)

print("循环结束")