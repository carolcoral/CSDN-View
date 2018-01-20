
# -*- coding: utf-8 -*
import webbrowser as web    
import time    
import os    
import random
import requests
#s = requests.seesion()  
count = random.randint(1,2)   
urllist=[
'http://blog.csdn.net/carolcoral/article/details/79105562',
'http://blog.csdn.net/carolcoral/article/details/79105562',
'http://blog.csdn.net/carolcoral/article/details/79041873',
'http://blog.csdn.net/carolcoral/article/details/79034589',
'http://blog.csdn.net/carolcoral/article/details/79022987',
'http://blog.csdn.net/carolcoral/article/details/79016608',
'http://blog.csdn.net/carolcoral/article/details/79009155',
'http://blog.csdn.net/carolcoral/article/details/78895236']
for j in range(0,100000):#设置循环的总次数   
    i=0    
    while i<=8 :  
        #s.get('http://blog.csdn.net')  
        for url in urllist:
            web.open(url)  #访问网址地址，语法 .open(url,new=0,Autorasise=True),设置 new 的值不同有不同的效果0、1、2  
            #s.cookies.clear()
            i=i+1    
            time.sleep(3)  #设置每次打开新页面的等待时间
    else:    
        time.sleep(10) #设置每次等待关闭浏览器的时间  
        os.system('taskkill /F /IM Firefox.app')  #浏览器，其他的更换下就行
        #/F强制关闭进程  /T关闭的进程树及子树  /IM进程的映像名称
        #print 'time webbrower closed'    
