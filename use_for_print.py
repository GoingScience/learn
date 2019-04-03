#--coding: utf-8--
num=range(1,10)#创建一个数组从1到9
for this in num:#在for循环中引用这个数组，in同=，用于赋值
    print ("在座有几位？%s个皮皮虾")%this
    #百分号可以用来插入，其中%s和%d都可以
print ('''
但是不得不说
在座的各位都是垃圾
有意见的不可以提
''')#利用三个单引号或双引号，中间的内容全部注释
print ('you\'re very stupid')#利用反斜杠输出单引号
print ('\\\\_v_//'(#利用反斜杠输出反斜杠
speak_the = (hello)
say_the = (' word')
print speak_the + say_the#利用加号来同时输出两个变量
print speak_the + ' this' + say_the#利用加号来输出变量以及字符串
print 'speak '\
+ speak_the\
+ say_the#利用反斜杠来换行
print 'hello\nword'#利用\n在输出中换行
#字符与数字不能用加号连接可以用str来把数字转换为字符串
print '请拨打' + str(12580)
num_1 = 12580
print '请拨打' + str(num_1)
#百分号的插入也不受数字与字符串的影响
print '请拨打%s'%12580
print '请拨打%s'%num_1
#%d用来替换整数%s替换字符串%f替换小数，懒于实例不解释
#%f可以选择保留几位小数比如两位%2f等，懒于实例不解释
#在print后面添加，可以让循环中输出的内容在同一行
for this_1 in range(1,5):
    print '这是第一行',
print '\n'
#for嵌套也是比较有趣的东西
for this_2 in range(0,5):
    for this_3 in range(0,this_2 + 1):
        print '-',
    print '*'
#%s可以套入一个组
print 'age %d name %s'%(17,'Mr.T')
#int(x) #把x转换成整数
#float(x) #把x转换成浮点数
#str(x) #把x转换成字符串
#bool(x) #把x转换成bool值
print bool(-123)#非0则ture
print bool(0)
print bool('abc')#非空或代表空的none其他则true
print bool('False')
print bool('')
#空集合同样也为false
