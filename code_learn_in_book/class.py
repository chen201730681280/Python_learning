#coding=gbk
#�ھ��� ��

#���� ��.��python������ĸ��д������
class Dog():
	#��ʼ��,_init_��һ������ķ�����ÿ�ν���dog��ʵ��ʱ��
	#�����Զ����У��������»��߱���������ĺ���
	#self����ββ���ȱ�٣���������ǰ�棬����ʱ�Զ����ε�self
	#selfָ��ʵ������
	#�ص㣡��������initǰ���������»��ߣ�����Ҳ�������»��ߣ�����
	def __init__(self,name,age):
		self.name=name #��selfΪǰ׺�ı������ɹ��������з���ʹ��
		self.age=age
		#������ָ��Ĭ��ֵ
		#���е�ÿ�����Զ�����Ҫ�г�ʼֵ
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
	#ͨ�������޸����Ե�ֵ
	def update_food(self,foods):
		self.food=foods
		print(self.name+"'s food change to " +self.food)
	#ͨ�����������Ե�ֵ���е���
	def increment_lover(self):
		self.lover += 1
	
	
#����ʵ��
my_dog =Dog('willie',6)
my_dog.sit()
my_dog.roll_over()
b_dog=Dog('lucky',3)

print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
print(my_dog.get_descriptive_name())
my_dog.read_food()
my_dog.read_lover()

#�޸����Ե�ֵ
#ֱ���޸�
my_dog.lover=1
my_dog.read_lover()
#ͨ�������޸�
my_dog.update_food('banana')
#ͨ�����������Ե�ֵ���е���
my_dog.increment_lover()
my_dog.read_lover()

#�̳�
#һ����̳���һ����ʱ�������Զ������һ������������Ժͷ���
#ͬʱ���Զ����Լ������Ժͷ���
#����Ҫ��������������Ը�ֵ

#��ʵ���������ԣ����Խ����һ������Ϊһ������������ȡ����
class Favorite_people():
	def __init__(self,name,age,sex):
		self.name=name
		self.age=age
		self.sex=sex
	def describe(self):
		print("This Taidi's favorite people is : "+self.age
		+" years old person named "+self.name.title())
		
#��������ʱ�������������ڵ�ǰ�ļ��У���λ��ǰ��
#�����ڼ�Ϊ����
class Taidi(Dog):
	def __init__(self,name,age):
		#super�����˸���ķ�������taidiӵ���˸������������
		#��ʱ���������self����������
		super().__init__(name,age)
		self.ml_time=0
		#��ʵ����������
		self.favorite_people=Favorite_people('lili','0','nv')
	#�����ඨ�����Ժͷ���
	def ml_time_description(self):
		print("This Taidi "+self.name+" had made love for "
		+str(self.ml_time))
	#��д����ķ���,�����̩�ϵ���read_lover����������ֲ�ͬ������
	def read_lover(self):
		print("Many")
my_taidi=Taidi('wiki',10)
print(my_taidi.get_descriptive_name())
my_taidi.ml_time_description()
my_taidi.read_lover()
my_taidi.favorite_people.describe()

	
#ʹ��python��׼��
#�ֵ���Խ���Ϣ�����𣬵�����¼��ӵ�˳��
#Ҫ�����ֵ䲢��¼���м�ֵ�Ե����˳�򣬿���ʹ��python��׼��
from collections import OrderedDict
favorite_l=OrderedDict()
favorite_l['a']='python'
favorite_l['b']='c'
favorite_l['c']='c++'
for name,language in favorite_l.items():
	print(name.title()+"'s favorite language is "+language.title()+".")










