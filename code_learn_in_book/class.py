#coding=gbk
#第九章 类

#定义 类.在python中首字母大写的是类
class Dog():
	#初始化,_init_是一个特殊的方法，每次建立dog新实例时，
	#都会自动运行，用两个下划线标记这个特殊的函数
	#self这个形参不可缺少，还必须在前面，运行时自动传参到self
	#self指向实例本身
	#重点！！！！！init前面有两个下划线，后面也有两个下划线！！！
	def __init__(self,name,age):
		self.name=name #以self为前缀的变量都可供类中所有方法使用
		self.age=age
		#给属性指定默认值
		#类中的每个属性都必须要有初始值
		self.food=""
		self.lover=0
	def sit(self):
		print(self.name.title()+" is now sitting.")
	def roll_over(self):
		print(self.name.title()+" rolled over.")
	def get_descriptive_name(self):
		long_name=str(self.age)+" years old's dog: "+self.name
		return long_name
	def read_food(self):
		print(self.name+"'s foods is: "+self.food)
	def read_lover(self):
		print(self.name+" has "+str(self.lover)+" lover.")
	#通过方法修改属性的值
	def update_food(self,foods):
		self.food=foods
		print(self.name+"'s food change to " +self.food)
	#通过方法对属性的值进行递增
	def increment_lover(self):
		self.lover += 1
	
	
#创建实例
my_dog =Dog('willie',6)
my_dog.sit()
my_dog.roll_over()
b_dog=Dog('lucky',3)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
print(my_dog.get_descriptive_name())
my_dog.read_food()
my_dog.read_lover()

#修改属性的值
#直接修改
my_dog.lover=1
my_dog.read_lover()
#通过方法修改
my_dog.update_food('banana')
#通过方法对属性的值进行递增
my_dog.increment_lover()
my_dog.read_lover()

#继承
#一个类继承另一个类时，它将自动获得另一个类的所有属性和方法
#同时可以定义自己的属性和方法
#首先要给父类的所有属性赋值

#将实例用作属性，可以将类的一部分作为一个独立的类提取出来
class Favorite_people():
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex
	def describe(self):
		print("This Taidi's favorite people is : "+self.age
		+" years old person named "+self.name.title())
		
#创建子类时，父类必须包含在当前文件中，并位于前面
#括号内即为父类
class Taidi(Dog):
	def __init__(self,name,age):
		#super调用了父类的方法，让taidi拥有了父类的所有属性
		#此时，传入除了self的所有属性
		super().__init__(name,age)
		self.ml_time=0
		#将实例用作属性
		self.favorite_people=Favorite_people('lili','0','nv')
	#给子类定义属性和方法
	def ml_time_description(self):
		print("This Taidi "+self.name+" had made love for "
		+str(self.ml_time))
	#重写父类的方法,如果对泰迪调用read_lover将会出现这种不同的内容
	def read_lover(self):
		print("Many")
my_taidi=Taidi('wiki',10)
print(my_taidi.get_descriptive_name())
my_taidi.ml_time_description()
my_taidi.read_lover()
my_taidi.favorite_people.describe()

	
#使用python标准库
#字典可以将信息关联起，但不记录添加的顺序
#要创建字典并记录其中键值对的添加顺序，可以使用python标准库
from collections import OrderedDict
favorite_l=OrderedDict()
favorite_l['a']='python'
favorite_l['b']='c'
favorite_l['c']='c++'
for name,language in favorite_l.items():
	print(name.title()+"'s favorite language is "+language.title()+".")










