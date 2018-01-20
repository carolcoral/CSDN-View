
# -*- coding: utf-8 -* #设置编码格式

import webbrowser as web    
import time    
import os    
import random
import requests

s = requests.session()  #获取session 值
count = random.randint(1,2)    
j=0    
while j<count:    
    i=0    
    while i<=8 :  
        s.get('http://blog.csdn.net')  #获取指定网址的 coockie 值
        web.open_new_tab('http://blog.csdn.net/carolcoral/article/details/79105562')  #网址替换这里  
        s.cookies.clear() # 每次访问后清除 coockie
        i=i+1    
        time.sleep(3)  #这个时间根据自己电脑处理速度设置，单位是s  #每次刷新的间隔时间
    else:    
        time.sleep(10) #这个时间根据自己电脑处理速度设置，单位是s 休眠间隔时间
        os.system('taskkill /Applications/Firefox.app')  #火狐浏览器，其他的更换下就行，这里设置的是你电脑的默认打开浏览器
        #print 'time webbrower closed'  
          
    j=j+1    
 
