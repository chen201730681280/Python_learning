#coding=gbk
#��ʮ�� �ļ����쳣

#��ȡ�ļ����ݣ���������������ݵĸ�ʽ������д���ļ����������������ʾ����
with open('pi_digits.txt') as file_object:
	contents=file_object.read()
	#print(contents)
#������ԭ�����ļ���һ�����У�read���������ļ�ĩβʱ������һ�����ַ���
#���Ҫɾ�����У�ֻ��Ҫ���һ��retrip����
	print(contents.rstrip())
