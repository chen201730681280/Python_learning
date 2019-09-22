# coding=gbk
#排序

#按字母排序_永久性改变
cars=['ooo','hhh','aaa','mmm']
cars.sort()
print(cars)

#按字母反方向排序_永久性改变
cars.sort(reverse=True)
print(cars)

#保留列表元素按原来的排列顺序但又用特定的排列顺序呈现,最后是传参后
print("Original: ")
print(cars)
print("Sorted: ")
print(sorted(cars))
print("Original: ")
print(cars)
print("Sorted: ")
print(sorted(cars,reverse=True))

#反转列表，不是按字母顺序，而只是反转
cars=['lklk','dsadas','sfds']
print("原")
print(cars)
cars.reverse()
print("反转")
print(cars)

#长度
print("取长度")
print(len(cars))

#导入的练习
def print_cars(car):
	car.reverse()
	print(car)
















