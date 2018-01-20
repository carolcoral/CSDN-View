# CSDN-

* 用 python 实现 增加 CSDN 的访问量

>前言：才开的一个 CSDN 的博客，感觉访问量好低，才几千，看到别人百万访问量感觉好爽，本着娱乐精神并且刚好最近也在学习 Python，就考虑用 python 做了一个自动访问 csdn 博客实现无限刷访问量的功能。

>我们应当具有的条件：成功安装了 python 运行环境，安装了 requests 模块包

1. 首先我们需要知道 csdn 访问量是基于什么原理来产生的，一般实现自增长的访问记录我们通常采用两种方式，一种是记录在 cookie值里面，一种是记录在 session 值中。

2. 我们需要设置休眠时间来控制访问的情况，这个可以根据自己的实际情况控制；

3. 因为我们使用了获取 cookie 的技术，因此需要在 python 中安装 requests 模块才能正常获取，下面会说到怎么安装这个模块；

4. 在我们电脑的控制台运行下载的 count.py 文件即可，mac 电脑在 terminal 中使用 <code>python count.py</code>，Windows 中使用 cmd 运行 <code>python count.py</code>；


* 安装 requests 模块：

1. 首先下载 requests 模块包，下载地址：[requests for python](https://pypi.python.org/packages/b0/e1/eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a329aa8d09/requests-2.18.4.tar.gz#md5=081412b2ef79bdc48229891af13f4d82)

2. 解压下载好的文件夹到你安装 python 的根目录下

3. 打开控制台，使用 cd 命令切换到 requests 解压后的路径下

4. 运行命令<code>python setup.py install</code>

5. 在 python shell 中使用<code>import requests</code> 查看是否成功安装导入
