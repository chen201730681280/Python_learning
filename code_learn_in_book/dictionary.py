#coding=gbk
#������ �ֵ�

#�洢һ������Ķ�����Ϣ

#һ���򵥵��ֵ䣬�������ض��������˵�����
alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#�ֵ��Ƕ�̬�ṹ��������ʱ��������ӽ�ֵ��
#add 
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#modify
alien_0['color']='yellow'
print(alien_0)

#ɾ��
del alien_0['points']
print(alien_0)


#�洢�ڶ�����ͬһ����Ϣ
lover = {
	'lin':'python',
	'huang':'c++',
	'zhou':'java',
	}
print("lin's lover is "+lover['lin']+".")

#�����ֵ�,items()���ֵ�ķ��������Է���һ����ֵ���б�
for key,value in alien_0.items():
	print("\nKey:"+key)
	print("Value:"+str(value))
	
#�����ֵ������еĽ�
for name in lover.keys():
	print(name.title())

#�õ�ǰ���������������ֵ
love=['lin','c']
for name in lover.keys():
	print(name)
	
	if name in love:
		print(name.title())

#����ĸ˳������ֵ��е����м�
for name in sorted(lover.keys()):
	print("\nHello! "+name.title())

#����ֵ
for love in lover.values():
	print(love.title())

#�ҳ���һ�޶���Ԫ��
lover['hei']='python'
for name in set(lover.values()):
	print(name)

#Ƕ�� ��һϵ���ֵ�洢���б��У����б���Ϊֵ�洢���ֵ���
#�ֵ��б�
#���ֵ��б�,���ֵ�����б���
alien_1={'color':'green','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)

#�ô�������alien
aliens=[]
for alien_number in range(30):
	new_alien={'color':'green','point':5,'speed':'slow'}
	aliens.append(new_alien)
	
for alien in aliens[:5]:
	print(alien)
print("...")

print(str(len(aliens)))

#���б�����ֵ���
pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
	}
print(pizza['crust'])
for topping in pizza['toppings']:
	print("\t"+ topping)

#����2
lovers={
	'jin':['hei','ma'],
	'la':['c','a'],
	'kek':['d','f']
	}
for name,lover in lovers.items():
	print(name.title())
	for love in lover:
		print('\t'+love)

#���ֵ��д洢�ֵ�
users={
	'a':{
		'b':'ba',
		'c':'ca',
		'd':'da',
		},
	'e':{
		'b':'bb',
		'c':'cb',
		'd':'db',
		},
	}
for username,user_info in users.items():
	print("\nusername: "+username)
	full_name=user_info['b']+" "+user_info['c']
	location=user_info['d']
	print("\tfull name: "+full_name)
	print("\tlocation: "+location)
	

