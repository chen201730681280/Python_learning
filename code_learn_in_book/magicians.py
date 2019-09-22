# coding=gbk
#第四章 操作列表

#使用for循环
magicians=['alice','david','carolina']
#从magicians中取出一个名字，并赋值到magician中
#虽然写了两行，但在同一个循环里，只要是同一个缩进，就是一个体里面的内容
for magician in magicians:
	print(magician)
	print(magician.title()+",that is great trick")
#没有缩进的print在循环体外
print("\nThank you, everyone\n")

#创建数值列表
#range()生成数字
for value in range(1,5):
	print(value)
#用range（）创建数字列表，把range单座list的参数
numbers=list(range(1,6))
print(numbers)
#用range（）可以指定步长
numbers=list(range(2,11,2))
print(numbers)

#平方
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)
	
#简单统计
print(min(squares))
print(max(squares))
print(sum(squares))

#简化版
squares=[value**2 for value in range(1,11)]
print(squares)

#练习
#打印1-20
practice=[value for value in range(1,21)]
print(practice) 
#奇数
practice=list(range(1,21,2))
print(practice)
#3的倍数
three=[value*3 for value in range(1,11)]
print(three)
#立方
lifang=[value**3 for value in range(1,11)]
print(lifang)

#切片
#输出0-3
print(lifang[0:3])
#输出2-4
print(lifang[1:4])
#输出0-4
print(lifang[:4])
#输出最后三个
print(lifang[-3:])
lalas=['aaa','vvv','fff','ggg']

#遍历切片
for lala in lalas[:3]:
	print(lala.title())

#复制列表
lanas=lalas[:]
print(lalas)
print(lanas)

#错误示范,直接赋值是使这两个变量指向同一个列表，而不是副本
lamas=lalas
print(lamas)
lalas.append('asd')
print(lamas)

#元组是不可修改，不可变的 列表是可变的，是可修改的
#不能改变元组的元素，但可以给存储元组的变量赋值
aa=(20,2)
print(aa)
aa=(10,1)
print(aa)
