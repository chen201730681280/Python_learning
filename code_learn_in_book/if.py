# coding=gbk
#������ if���

#if���
cars=['aaa','hhh','fff']
#������ð��
#��Сд��ͬҲ�㲻ͬ�������Сд�޹ؽ�Ҫ����ô������lower�����Сд
for car in cars:
	if car == 'fff':
		print(car.upper())
	else:
		print(car.title())
#�����		
if cars[0] != 'hhh':
	print(cars[0])

#�Ƚ�
age=1
if age>0 or age <2 :
	print(age)

#����ض�ֵ�Ƿ����б���
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
