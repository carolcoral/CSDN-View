
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
j=0    
while j<count:    
    i=0    
    while i<=8 :  
        #s.get('http://blog.csdn.net')  
        for url in urllist:
            web.open(url)  #网址替换这里  
            #s.cookies.clear()
            i=i+1    
            time.sleep(3)  #这个时间根据自己电脑处理速度设置，单位是s  
    else:    
        time.sleep(10) #这个时间根据自己电脑处理速度设置，单位是s</span>  
        os.system('taskkill /F /T /IM /Applications/Firefox.app')  #google浏览器，其他的更换下就行
        #/F强制关闭进程  /T关闭的进程树及子树  /IM进程的映像名称
        #print 'time webbrower closed'  
          
    j=j+1    
 
