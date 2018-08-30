# -*- coding: utf-8 -*-
import jieba
import re
import sys

def parseMarkDown(filename):
	with open(filename, 'r') as f:
	    text= f.read()
	# 删除换行
	text=text.replace("\n","")
	# 删除jekyll的md模板文件头
	m=text.split("---")
	temp=""
	for i in range(0,len(m)):
	    if i%2 == 0:
	        temp += m[i]
	    else:
	    	pass
	        #print(m[i])
	#print("-------------------------------------------")
	#print(temp)
	# 删除代码块
	m=temp.split("```")
	temp=""
	for i in range(0,len(m)):
	    if i%2 == 0:
	        temp += m[i]
	    else:
	    	pass
	        #print(m[i])
	#print("-------------------------------------------")
	#print(temp)
	# 删除行内代码
	m=temp.split("`")
	temp=""
	for i in range(0,len(m)):
	    if i%2 == 0:
	        temp += m[i]
	    else:
	    	pass
	        #print(m[i])
	#print("-------------------------------------------")
	# 删除引入的html标签
	temp=re.sub(r'<.{10,100}>',"",temp)
	# 删除md文件链接
	temp=re.sub(r"\(http.{10,100}\)","",temp)
	# 删除md文件目录
	temp=re.sub(r'#.{5,50}\{\:toc\}',"",temp)
	# 删除标题格式
	temp=re.sub(r'#{1,8}',"",temp)
	# 删除粗体与斜体
	temp=re.sub(r'\*{1,2}',"",temp)
	# 删除表格控制线
	temp=re.sub(r'\-{1,20}',"",temp)
	# 删除多余空格
	temp=re.sub(r'\s{1,10}',"",temp)
	# 删除长串数字
	temp=re.sub(r'\d{5,}',"",temp)
	# 替换表格分界线
	temp=temp.replace("|"," ")
	print(temp)
	seg_list = jieba.cut(temp, cut_all=True)
	temp=", ".join(seg_list)
	temp=re.sub(r'[\(\)\[\]\{\},\.（），。 ],',"",temp)
	print(temp)
	saveFile(temp)

def saveFile(string):
	string = '- id: "const"\n  -content: '+string
	with open('out.txt','w') as f:
		print(string,file=f)

if __name__ == '__main__':
	parseMarkDown(sys.argv[1])
