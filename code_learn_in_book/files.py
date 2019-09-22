#coding=gbk
#第十章 文件与异常

#读取文件内容，重新设置这个数据的格式并将其写入文件，让浏览器可以显示内容
with open('pi_digits.txt') as file_object:
	contents=file_object.read()
	#print(contents)
#输出会比原来的文件多一个空行，read（）到达文件末尾时返回了一个空字符串
#如果要删除空行，只需要添加一个retrip函数
	print(contents.rstrip())
