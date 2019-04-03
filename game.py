from random import choice#随机数
print 'Choose one side to shoot:'#输出
print 'left, center, right'#输出
you = raw_input()#用户输入
print 'You kicked ' + you#输出+前面的用户输入
direction = ['left', 'center', 'right']#创建列表
com = choice(direction)#随机上面列表的值
print 'Computer saved ' + com#输出+上面列表随机出的值
if you != com:
    print 'Goal!'#你与电脑不同时输出
else:
    print 'Oops...'#你与电脑相同时输出
