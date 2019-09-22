#coding=gbk
#第六章 字典

#存储一个对象的多种信息

#一个简单的字典，保存了特定的外星人的特性
alien_0={'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#字典是动态结构，可以随时在其中添加健值对
#add 
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#modify
alien_0['color']='yellow'
print(alien_0)

#删除
del alien_0['points']
print(alien_0)


#存储众多对象的同一种信息
lover = {
	'lin':'python',
	'huang':'c++',
	'zhou':'java',
	}
print("lin's lover is "+lover['lin']+".")

#遍历字典,items()是字典的方法，可以返回一个健值对列表
for key,value in alien_0.items():
	print("\nKey:"+key)
	print("Value:"+str(value))
	
#遍历字典上所有的健
for name in lover.keys():
	print(name.title())

#用当前键来访问相关联的值
love=['lin','c']
for name in lover.keys():
	print(name)
	
	if name in love:
		print(name.title())

#按字母顺序遍历字典中的所有键
for name in sorted(lover.keys()):
	print("\nHello! "+name.title())

#返回值
for love in lover.values():
	print(love.title())

#找出独一无二的元素
lover['hei']='python'
for name in set(lover.values()):
	print(name)

#嵌套 将一系列字典存储在列表中，或将列表作为值存储在字典中
#字典列表
#简单字典列表,把字典存在列表中
alien_1={'color':'green','points':10}
alien_2={'color':'red','points':15}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
	print(alien)

#用代码生成alien
aliens=[]
for alien_number in range(30):
	new_alien={'color':'green','point':5,'speed':'slow'}
	aliens.append(new_alien)
	
for alien in aliens[:5]:
	print(alien)
print("...")

print(str(len(aliens)))

#把列表存在字典中
pizza={
	'crust':'thick',
	'toppings':['mushrooms','extra cheese']
	}
print(pizza['crust'])
for topping in pizza['toppings']:
	print("\t"+ topping)

#例子2
lovers={
	'jin':['hei','ma'],
	'la':['c','a'],
	'kek':['d','f']
	}
for name,lover in lovers.items():
	print(name.title())
	for love in lover:
		print('\t'+love)

#在字典中存储字典
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
	

