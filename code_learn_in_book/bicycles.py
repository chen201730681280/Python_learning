
bicycles=['trek','kkk','jjj']
print(bicycles[-1])

bicycles[0]='ooo'
print(bicycles[0])

#在队列尾增加
bicycles.append('ppp')
print(bicycles)

#插在0的位置上而不是0后面
bicycles.insert(0,'rrr')
print(bicycles)

#删除
del bicycles[1]
print(bicycles)

#pop方法删除最后一个
popped_bicycles=bicycles.pop()
print(bicycles)
print(popped_bicycles)


#pop方法删除任意一个
popped_bicycles=bicycles.pop(0)
print(bicycles)
print(popped_bicycles)

#根据值删除元素,若将要删除的赋值给一个变量，那么还可以使用这个值
bicycles.remove('kkk')
print(bicycles)


