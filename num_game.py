#coding=utf-8#可以输出中文
import random#生成随机数时需要这句，具体作用未知
again = 'y'#创建一个变量again
while again == 'y':#当变量again等于y时循环
    num_1 = int(random.uniform(1,100))#创建变量为1到100的随机数且为整型
    print 'please guess a num'
    re_start = 'true'#创建变量
    while re_start == 'true':
        num_2 = int(random.uniform(1,100))
        print num_2#添加一个用户输入点
        if num_1 > num_2:#当num_1大于num_2时执行if下的语句
            print'you guess small'
        if num_1 < num_2:
            print'you guess big'
        if num_1 == num_2:
            print"you're very good"
            re_start = 'false'
    print'try again?(y/n)'
    again = raw_input()
    if again == 'y':
        print '======================NEW======================'
    if again == 'n':
        print 'game over'
