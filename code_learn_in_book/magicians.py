# coding=gbk
#������ �����б�

#ʹ��forѭ��
magicians=['alice','david','carolina']
#��magicians��ȡ��һ�����֣�����ֵ��magician��
#��Ȼд�����У�����ͬһ��ѭ���ֻҪ��ͬһ������������һ�������������
for magician in magicians:
	print(magician)
	print(magician.title()+",that is great trick")
#û��������print��ѭ������
print("\nThank you, everyone\n")

#������ֵ�б�
#range()��������
for value in range(1,5):
	print(value)
#��range�������������б���range����list�Ĳ���
numbers=list(range(1,6))
print(numbers)
#��range��������ָ������
numbers=list(range(2,11,2))
print(numbers)

#ƽ��
squares=[]
for value in range(1,11):
	square=value**2
	squares.append(square)
print(squares)
	
#��ͳ��
print(min(squares))
print(max(squares))
print(sum(squares))

#�򻯰�
squares=[value**2 for value in range(1,11)]
print(squares)

#��ϰ
#��ӡ1-20
practice=[value for value in range(1,21)]
print(practice) 
#����
practice=list(range(1,21,2))
print(practice)
#3�ı���
three=[value*3 for value in range(1,11)]
print(three)
#����
lifang=[value**3 for value in range(1,11)]
print(lifang)

#��Ƭ
#���0-3
print(lifang[0:3])
#���2-4
print(lifang[1:4])
#���0-4
print(lifang[:4])
#����������
print(lifang[-3:])
lalas=['aaa','vvv','fff','ggg']

#������Ƭ
for lala in lalas[:3]:
	print(lala.title())

#�����б�
lanas=lalas[:]
print(lalas)
print(lanas)

#����ʾ��,ֱ�Ӹ�ֵ��ʹ����������ָ��ͬһ���б������Ǹ���
lamas=lalas
print(lamas)
lalas.append('asd')
print(lamas)

#Ԫ���ǲ����޸ģ����ɱ�� �б��ǿɱ�ģ��ǿ��޸ĵ�
#���ܸı�Ԫ���Ԫ�أ������Ը��洢Ԫ��ı�����ֵ
aa=(20,2)
print(aa)
aa=(10,1)
print(aa)
