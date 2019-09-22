#coding=gbk
#第八章 函数

#定义 def
def greet_user(first_name,last_name):
	full_name = first_name+' '+last_name
	return full_name.title()
	
while True:
	print("Your name: ")
	print("(or enter 'q' to quit)")
	
	f_name=input("first_name: ")
	if f_name == 'q':
		break
	l_name=input("Last name: ")
	if l_name == 'q':
		break
	
	formatted_name = greet_user(f_name,l_name)
	print("\nHello, "+formatted_name+" !")

#传递列表
def meet_user(names):
	for name in names:
		print("Hello "+name.title()+" !")


usernames=['chen','li','wu']
meet_user(usernames)

#修改列表
comp_usernames=['moon','yellow']

while usernames:
	current_user=usernames.pop()
	print("user: "+current_user)
	comp_usernames.append(current_user)
print("All user: ")
for user in comp_usernames:
	print(user)

#禁止函数修改列表
usernames=['chen','li','wu']
comp_usernames=['moon','yellow']
def print_models(usernames,comp_usernames):
	while usernames:
		current_user=usernames.pop()
		print(current_user+" finishs his job.")
		comp_usernames.append(current_user)

def show_users(comp_usernames):
	for user in comp_usernames:
		print("user: "+user)
		
#usernames[:]是个副本，改变他的值不会一起改变username
#如果需要一起改变则传入username
print_models(usernames[:],comp_usernames)
show_users(comp_usernames)
print(usernames)

#传递任意数量的实参（重要！！重要！！）
#python允许函数从调用语句中收集任意数量的实参
def user_info(user,*toppings):
	print("user: "+user)
	print(toppings)

user_info('chen','aaa')
user_info('li','aaa','cccc')

#可以接受任意数量的键值对-调用语句提供了多少就接受多少
#**user_info建立了一个user_info的空字典
def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile

user_profile = build_profile('albert','einstein',
							 location='princetion',field='physics')
print(user_profile)

#导入整个模块
#import是直接把代码复制到这一个页面，因此如果导入的部分有print，
#也会输出，如果要保持干净，则需要导入的部分都为函数

import cars 
car=['ls']
cars.print_cars(car)

#也可以导入模块中的特定函数a
#9.4的疑问，为何导入的是一个特定函数，但运行的时候还是会将整个模块的
#内容运行
from cars import print_cars as p_car
a_cars=['kkk','lll','mmm']
p_car(a_cars)

	
	
	
	
	

















	
		
	
	
	
	
	
	
	
