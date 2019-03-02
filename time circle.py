#连接字符串符号+与join在循环中的时间效率检验
import time
time01=time.time()#起始时刻
a=""
for i in range(1000000):
    a+="sxt"#每次连接符都会形成一个新的对象
time02=time.time()#终止时刻
print("运行时间1是："+str(time02-time01))

#join语句
li=[]#创建一个列表
time03=time.time()#起始时刻
for i in range(10):
    li.append("sxt")#列表后加后缀
b="".join(li)#join不要放在循环体中，不然数值太大了，运行存储值会很多
time04=time.time()#终止时刻
print("运行时间2是："+str(time04-time03))
