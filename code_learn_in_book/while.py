#coding=gbk
#������ �û������whileѭ��

#input
#input�ó�����ͣ�������û�����һЩ�ı�
message=input("Please input your name: ")
print(message)

#��ʾ����һ��ʱ,��+=����ʽ�洢��prompt
prompt="If you can tell me, we can personalize the message you see."
prompt += "\nWhat is your first name?"
name = input(prompt)
print("\nHello, "+name+" !") 

#input�Ὣ�û�������Ϊ�ַ�����������int����������Ϊ��ֵ
age=input("How old are you?")
age =int(age)
if age >= 18:
	print("True")
	
#��ģ
number=10
print(number%2)


#whileѭ��
while number>=5:
	print(number)
	number -=1

#���û���������˳�ֵ
quit="If you want to quit, please enter 'quit'"
message=""  #���ڴ洢����ֵ
while message !='quit':
	message=input(quit)
	if message != 'quit':
		print(message)

#ʹ�ñ�ǣ��ɶ���һ�������������ж����������Ƿ��ڻ״̬
quit="If you want to quit, please enter 'quit'"

#���ֵ
active = True
while active:
	message=input(quit)
	if message == 'quit':
		active = False
	else:
		print(message)
		
#break�˳�ѭ��
while True:
	city=input(quit)
	if city == 'quit':
		break
	else:
		print(city.title())

#continue����ѭ����ͷ���������������Խ�������Ƿ����ִ��ѭ��
#ֻ���6-10������
c_number=5
while c_number<10:
	c_number += 1
	if c_number % 2 == 0:
		continue
	print(c_number)

#��whileѭ���������б���ֵ�
#����֤
un_users=['alice','brian','candy']
#����֤
con_users=[]
#��֤ÿ���û���ֱ��û��δ��֤�û�Ϊֹ
#��ÿ��������֤���б��Ƶ�����֤�û��б���
while un_users:
	current_user=un_users.pop()
	print(current_user.title())
	con_users.append(current_user)

#ɾ�������ض�ֵ�������б���
#��remove����ֻ��ɾ��һ��ֵ������Ҫ��while
pets=['cat','dog','cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')
print(pets)

#ʹ���û�����������ֵ�
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








