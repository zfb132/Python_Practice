#coding=utf-8
import urllib.request
import re
import urllib
import os
import time

#由于涉及隐私原因，网址和学号已被修改
url_base='http://www.example.com/Web/img/'
stuID=2016000000000

def report_hook(blocks_read, block_size, total_size):
    if not blocks_read:
        print("开始下载")
        return
    if total_size < 0:
        print("读取第%s个8KB数据块，已下载%sB（字节）" % (blocks_read, blocks_read * block_size))
    else:
        amount_read = blocks_read * block_size
        s=amount_read*100.0/(total_size)
        if s>=100:
            s=100
        print("读取第%s个8KB数据块， %sB/%sB, %.0f%%" % (blocks_read, amount_read, total_size, s))


def searchurl(url):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    print(url)
    str0=opener.open(url).read()
    str1=str0.decode('utf-8','ignore')
    pa=r'href="(\d{5})/"'
    patt=re.compile(pa)
    listurl=re.findall(patt,str1)
 

    #这个部分是有用的，只不过由于有的不是big/small导致还是一个学校一个学校比较方便
    f=open("1.txt","r")
    s=f.read()
    f.close()
                    #这是一个数组
    list_s=s.split("\n")
    x=[]
    y=[]
    for i in list_s:
        b=str(i).split(" ")
        x.append(b[3])
        y.append(b[2])
    d={k:v for (k,v) in zip(x,y)}

    for i in listurl:
    	try:
    	    print(d[i])
    	except:
    		print(i+" error")

'''
    filename=listurl
    a=0	
    for m in listurl:
        cmd="cmd.exe /c md C:\\Users\\admin\\Desktop\\1\\%s" %filename[a]
        info=os.system(cmd)
        if info!=1:
            searchimg(m)
        a=a+1
'''

def searchimg(key):
    url1=url_base+key+'/big/'
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393')]
    str0=opener.open(url1).read()
    str1=str0.decode('utf-8','ignore')
	
    pa=r'<a href="(.{,30}\.jpg)">(.{,20}\.jpg)</a>'
    patt=re.compile(pa)
    imgurl=re.findall(patt,str1)

    b=0
    for i in imgurl:
        print(url1+i[0])
        if len(i[0])==17:    #因为有13和14级的学号位数不同
            t=i[0][0:13]
            if int(t)==stuID:      #查漏补缺
                urllib.request.urlretrieve(url1+i[0], 'C:\\Users\\admin\\Desktop\\1\\%s\\%s' %(key,i[1]),reporthook=report_hook)
        b=b+1
    else:
        print(b)    #看一下总共有多少

if __name__=="__main__":
    searchurl(url_base)
    #searchimg("10486")