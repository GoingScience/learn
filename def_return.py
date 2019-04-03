#--coding: utf-8--
#del可以定义一个函数
def this():
    print '使用this则会输出这些this下的内容'
    print '为何我如此机智'
print this()
#def与PHP的funciton差不多
def this_1(num_1,num_2):
    return True
#return用来提前结束一个语句循环或判断并返回一个值
print this_1('50','200')
this_is = False
while this_is == False:
    print '111'
    this_is = this_1(1,1)#这里返回了true
#前面的数字游戏可以通过返回值来重新编写
