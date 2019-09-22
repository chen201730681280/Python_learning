# coding=gbk
#第五章 if语句

#if语句
cars=['aaa','hhh','fff']
#易忘：冒号
#大小写不同也算不同，如果大小写无关紧要，那么可以用lower都变成小写
for car in cars:
	if car == 'fff':
		print(car.upper())
	else:
		print(car.title())
#不相等		
if cars[0] != 'hhh':
	print(cars[0])

#比较
age=1
if age>0 or age <2 :
	print(age)

#检查特定值是否在列表中
a='jjj'	
if a not in cars:
	print(a.title())

#if-elif-else
a=4
if a<3:
	print(a)
elif a>19:
	print(a+1)
else:
	print(a+2)

for car in cars:
	if car == 'hhh':
		print("no hhh")
	else:
		print("add "+car+".")
a_cars=['hhh','mmm']
for a_car in a_cars:
	if a_car in cars:
		print(a_car)
	else:
		print("no")
