### 环境要求

```
python3.6.X

mysql 5.6/5.7

开发工具：pycharm 2019
```

### 安装依赖包

```
在项目根目录下执行：pip install -r requirements.txt
注：requirements.txt放在项目根目录下
这个安装过程要多等待一会
若这步骤出错，直接进行后续步骤就行，提示你安装什么包你就装什么包。

比如提示你 no model captcha  ，你就安装captcha这个，但是你可能不知道包名全称，不知道的去requirements.txt 查询就行了。


注：如执行完，执行后续步骤提示缺少某个包，则执行 pip  install 包名



```



### 导入数据库：

```
打开settings.py ，保证数据密码和自己本地的对应。
```

```python
同步数据库:
    1.在自己的mysql数据库新建一个名为xxx（就是settings.py中写的数据库名）的数据库，编码格式utf-8

	2.在项目根目录下执行： （1）    python manage.py makemigrations

				 	   （2）     python manage.py migrate
```



### 超级管理员用户

```python

python manage.py createsuperuser  可以创建超级管理员用户
```

###  运行

```python
pycharm 运行django项目，注意看自己的pycharm是否有python  interpreter

如自己有多个python 则注意好，当前项目用的是哪个python。
```

