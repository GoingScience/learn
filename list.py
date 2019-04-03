#--coding: utf-8--
#list是列表的意思并不是具体的指令
#可以用for遍历列表的元素
list = [520, 'happy',3.1415,'random']
for h in list:
    print h
print list
#访问list中的元素
print list[0]#这是访问第一个元素
#修改list中的元素
list[0] = 250#把表格中的第一个元素修改为250
print list[0]#输出第一个元素证明自己是否修改成功
#添加list中的元素
list.append('mdzz?')#添加一个叫mdzz？的元素
for h in list:#验证是否成功
    print h
#删除list中的元素
del list[0]
print list[0]
