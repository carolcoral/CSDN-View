# CSDN-View

# 用 python 实现 增加 CSDN 的访问量

>前言：才开的一个 CSDN 的博客，感觉访问量好低，才几千，看到别人百万访问量感觉好爽，本着娱乐精神并且刚好最近也在学习 Python，就考虑用 python 做了一个自动访问 csdn 博客实现无限刷访问量的功能。

>我们应当具有的条件：成功安装了 python 运行环境，安装了 requests 模块包


### 可能需要的依赖包：

1. [requests](https://pypi.python.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl#md5=eb9be71cc41fd73a51a7c9cd1adde5de)

2. [URLLib3](https://pypi.python.org/packages/63/cb/6965947c13a94236f6d4b8223e21beb4d576dc72e8130bd7880f600839b8/urllib3-1.22-py2.py3-none-any.whl#md5=1c11e1c80371cc4e89911071010a98d1)

3. [chardet](https://pypi.python.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl#md5=0004b00caff7bb543a1d0d0bd0185a03)

4. [certifi](https://pypi.python.org/packages/fa/53/0a5562e2b96749e99a3d55d8c7df91c9e4d8c39a9da1f1a49ac9e4f4b39f/certifi-2018.1.18-py2.py3-none-any.whl#md5=38f1c6a4a5d6b5e8bcb614354d6584c9)

5. [idna](https://pypi.python.org/packages/27/cc/6dd9a3869f15c2edfab863b992838277279ce92663d334df9ecf5106f5c6/idna-2.6-py2.py3-none-any.whl#md5=875c4a7b32b4897537d5ea9247b5c79e)


### 安装和运行步骤：

1. 首先我们需要知道 csdn 访问量是基于什么原理来产生的，一般实现自增长的访问记录我们通常采用两种方式，一种是记录在 cookie值里面，一种是记录在 session 值中。

2. 我们需要设置休眠时间来控制访问的情况，这个可以根据自己的实际情况控制；

3. 因为我们使用了获取 cookie 的技术，因此需要在 python 中安装 requests 模块才能正常获取，下面会说到怎么安装这个模块；

4. 在我们电脑的控制台运行下载的 count.py 文件即可，mac 电脑在 terminal 中使用 <code>python count.py</code>，Windows 中使用 cmd 运行 <code>python count.py</code>；


### 安装 requests 模块：

* 方法一：

1. 首先下载 requests 模块包，下载地址：[requests for python](https://pypi.python.org/packages/49/df/50aa1999ab9bde74656c2919d9c0c085fd2b3775fd3eca826012bef76d8c/requests-2.18.4-py2.py3-none-any.whl#md5=eb9be71cc41fd73a51a7c9cd1adde5de)，下载好后修改后缀名为.zip，解压后把 requests 这个文件夹复制到 python 安装目录下的 lib 目录即可

2. 在 python shell 中使用<code>import requests</code> 查看是否成功安装导入

* 方法二：

1. 下载第二个后缀名为.tar.gz 的压缩包，解压下载好的文件夹到你安装 python 的根目录下

2. 打开控制台，使用 cd 命令切换到 requests 解压后的路径下

3. 运行命令<code>python setup.py install</code>

4. 在 python shell 中使用<code>import requests</code> 查看是否成功安装导入


### [Issus](https://github.com/carolcoral/CSDN-View/issues)

 For Example:
 
 * Q:为什么运行后访问量没有增加？

    >可能是框架的问题，解决方法是在浏览器的设置里面直接搜索 cookie，然后在里面添加一个例外情况，主机名输入:blog.csdn.net，后面设置禁止，然后点击确定后重启浏览器即可
