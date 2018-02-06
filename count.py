# -*- coding: utf-8 -*
import webbrowser as web    
import time    
import os    
import random
import requests
#s = requests.seesion()  
#count = random.randint(1,2)   
urllist=[
    'http://blog.csdn.net/carolcoral/article/details/79219736',
    'http://blog.csdn.net/carolcoral/article/details/79168741',
    'http://blog.csdn.net/carolcoral/article/details/78895236',
    'http://blog.csdn.net/carolcoral/article/details/78889581',
    'http://blog.csdn.net/carolcoral/article/details/78874916',
    'http://blog.csdn.net/carolcoral/article/details/78869401',
    'http://blog.csdn.net/carolcoral/article/details/78861164',
    'http://blog.csdn.net/carolcoral/article/details/78861129',
    'http://blog.csdn.net/carolcoral/article/details/78806239',
    'http://blog.csdn.net/carolcoral/article/details/78805088',
    'http://blog.csdn.net/carolcoral/article/details/78800717',
    'http://blog.csdn.net/carolcoral/article/details/78798659',
    'http://blog.csdn.net/carolcoral/article/details/78794191',
    'http://blog.csdn.net/carolcoral/article/details/78784467',
    'http://blog.csdn.net/carolcoral/article/details/78774841',
    'http://blog.csdn.net/carolcoral/article/details/78759821',
    'http://blog.csdn.net/carolcoral/article/details/78753593',
    'http://blog.csdn.net/carolcoral/article/details/78753106',
    'http://blog.csdn.net/carolcoral/article/details/78751965'
]

urllist2=[
    'http://blog.csdn.net/carolcoral/article/details/78749019',
    'http://blog.csdn.net/carolcoral/article/details/78745159',
    'http://blog.csdn.net/carolcoral/article/details/78744549',
    'http://blog.csdn.net/carolcoral/article/details/78742338',
    'http://blog.csdn.net/carolcoral/article/details/78733121',
    'http://blog.csdn.net/carolcoral/article/details/78728532',
    'http://blog.csdn.net/carolcoral/article/details/78728503',
    'http://blog.csdn.net/carolcoral/article/details/78728362',
    'http://blog.csdn.net/carolcoral/article/details/78728191',
    'http://blog.csdn.net/carolcoral/article/details/78728132'
]

urllist3=[
    'http://blog.csdn.net/carolcoral/article/details/78728101',
    'http://blog.csdn.net/carolcoral/article/details/78723497',
    'http://blog.csdn.net/carolcoral/article/details/78723492',
    'http://blog.csdn.net/carolcoral/article/details/78722074',
    'http://blog.csdn.net/carolcoral/article/details/78717817',
    'http://blog.csdn.net/carolcoral/article/details/78712050',
    'http://blog.csdn.net/carolcoral/article/details/78711141',
    'http://blog.csdn.net/carolcoral/article/details/78710447',
    'http://blog.csdn.net/carolcoral/article/details/78709321',
    'http://blog.csdn.net/carolcoral/article/details/78708034',
    'http://blog.csdn.net/carolcoral/article/details/78680069',
    'http://blog.csdn.net/carolcoral/article/details/78680045',
    'http://blog.csdn.net/carolcoral/article/details/78680032',
    'http://blog.csdn.net/carolcoral/article/details/78680016',
    'http://blog.csdn.net/carolcoral/article/details/78678984'
]

urllist4=[
    'http://blog.csdn.net/carolcoral/article/details/78678970',
    'http://blog.csdn.net/carolcoral/article/details/78674588',
    'http://blog.csdn.net/carolcoral/article/details/78674571',
    'http://blog.csdn.net/carolcoral/article/details/78674551',
    'http://blog.csdn.net/carolcoral/article/details/77857346'
]



for j in range(0,100000):#设置循环的总次数   
    i=0    
    while i<1 :  #一次打开浏览器访问的循环次数
        #s.get('http://blog.csdn.net')  
        for url in urllist:
            web.open(url)  #访问网址地址，语法 .open(url,new=0,Autorasise=True),设置 new 的值不同有不同的效果0、1、2  
            i=i+1    
            time.sleep(3)  #设置每次打开新页面的等待时间
    else:    
        time.sleep(10) #设置每次等待关闭浏览器的时间  
        os.system('taskkill /F /IM firefox.app')  #你设置的默认使用浏览器，其他的更换下就行
        #/F强制关闭进程  /T关闭的进程树及子树  /IM进程的映像名称
        #print 'time webbrower closed'    
