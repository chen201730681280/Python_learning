#coding=gbk
#�ڰ��� ����

#���� def
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

#�����б�
def meet_user(names):
	for name in names:
		print("Hello "+name.title()+" !")


usernames=['chen','li','wu']
meet_user(usernames)

#�޸��б�
comp_usernames=['moon','yellow']

while usernames:
	current_user=usernames.pop()
	print("user: "+current_user)
	comp_usernames.append(current_user)
print("All user: ")
for user in comp_usernames:
	print(user)

#��ֹ�����޸��б�
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
		
#usernames[:]�Ǹ��������ı�����ֵ����һ��ı�username
#�����Ҫһ��ı�����username
print_models(usernames[:],comp_usernames)
show_users(comp_usernames)
print(usernames)

#��������������ʵ�Σ���Ҫ������Ҫ������
#python�������ӵ���������ռ�����������ʵ��
def user_info(user,*toppings):
	print("user: "+user)
	print(toppings)

user_info('chen','aaa')
user_info('li','aaa','cccc')

#���Խ������������ļ�ֵ��-��������ṩ�˶��پͽ��ܶ���
#**user_info������һ��user_info�Ŀ��ֵ�
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

#��������ģ��
#import��ֱ�ӰѴ��븴�Ƶ���һ��ҳ�棬����������Ĳ�����print��
#Ҳ����������Ҫ���ָɾ�������Ҫ����Ĳ��ֶ�Ϊ����

import cars 
car=['ls']
cars.print_cars(car)

#Ҳ���Ե���ģ���е��ض�����a
#9.4�����ʣ�Ϊ�ε������һ���ض������������е�ʱ���ǻὫ����ģ���
#��������
from cars import print_cars as p_car
a_cars=['kkk','lll','mmm']
p_car(a_cars)

	
	
	
	
	

















	
		
	
	
	
	
	
	
	
