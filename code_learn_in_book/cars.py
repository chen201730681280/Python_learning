# coding=gbk
#����

#����ĸ����_�����Ըı�
cars=['ooo','hhh','aaa','mmm']
cars.sort()
print(cars)

#����ĸ����������_�����Ըı�
cars.sort(reverse=True)
print(cars)

#�����б�Ԫ�ذ�ԭ��������˳�������ض�������˳�����,����Ǵ��κ�
print("Original: ")
print(cars)
print("Sorted: ")
print(sorted(cars))
print("Original: ")
print(cars)
print("Sorted: ")
print(sorted(cars,reverse=True))

#��ת�б����ǰ���ĸ˳�򣬶�ֻ�Ƿ�ת
cars=['lklk','dsadas','sfds']
print("ԭ")
print(cars)
cars.reverse()
print("��ת")
print(cars)

#����
print("ȡ����")
print(len(cars))

#�������ϰ
def print_cars(car):
	car.reverse()
	print(car)
















