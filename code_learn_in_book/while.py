#coding=gbk
#第七章 用户输入和while循环

#input
#input让程序暂停，并让用户输入一些文本
message=input("Please input your name: ")
print(message)

#提示超过一行时,用+=的形式存储在prompt
prompt="If you can tell me, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, "+name+" !") 

#input会将用户输入解读为字符串，可以用int（）让其视为数值
age=input("How old are you?")
age =int(age)
if age >= 18:
	print("True")
	
#求模
number=10
print(number%2)


#while循环
while number>=5:
	print(number)
	number -=1

#当用户输入的是退出值
quit="If you want to quit, please enter 'quit'"
message=""  #用于存储输入值
while message !='quit':
	message=input(quit)
	if message != 'quit':
		print(message)

#使用标记，可定义一个变量，用于判断整个程序是否处于活动状态
quit="If you want to quit, please enter 'quit'"

#标记值
active = True
while active:
	message=input(quit)
	if message == 'quit':
		active = False
	else:
		print(message)
		
#break退出循环
while True:
	city=input(quit)
	if city == 'quit':
		break
	else:
		print(city.title())

#continue返回循环开头，并根据条件测试结果决定是否继续执行循环
#只输出6-10的奇数
c_number=5
while c_number<10:
	c_number += 1
	if c_number % 2 == 0:
		continue
	print(c_number)

#用while循环来处理列表和字典
#待验证
un_users=['alice','brian','candy']
#已验证
con_users=[]
#验证每个用户，直到没有未验证用户为止
#将每个经过验证的列表都移到已验证用户列表中
while un_users:
	current_user=un_users.pop()
	print(current_user.title())
	con_users.append(current_user)

#删除包含特定值的所有列表函数
#用remove（）只能删除一个值，所有要用while
pets=['cat','dog','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#使用用户输入来填充字典
responses={}
active=True
while active :
	name=input("What's your name?")
	response=input("Which one is your favorite?")
	responses[name]=response
	repeat=input("Do you want to enter another one?")
	if repeat == 'no':
		active=False
print("result:\n")
for name,favorite in responses.items():
	print(name+"'s favorite is: "+favorite)








