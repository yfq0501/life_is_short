
################################  变量 #############################################
from cmath import pi
from time import process_time_ns


print("变量字符串初尝试：")
firstring="hello word"
print(firstring[0:7:2]) #最后一位是步长
print(firstring.upper())
print('Hello'.isupper())


firvariate=211
firvariate+=985
print (firvariate)
################################  列表  ############################################
print("\n列表初尝试:像数组")

firlist=[2,'a',1,985]
firlist.append(20)
print(firlist)


secstring= ''.join(str(i) for i in firlist)   #列表转字符串，全字符类型
print(secstring)

################################  字典 ############################################

print("\n字典初尝试:键值对")
firdiction = {'name': 'tom', 'age': '18','add':'1301'}  # 定义一个字典
print("年龄是:",end=" ")
print(firdiction.get('age'))              # 获取age的值
print(firdiction.keys()) 


################################ 分支if ##########################################

print("\nif初尝试:有个冒号(注意英文符)")
print("5是",end="")
num1=5
if num1%2==0 :
    print("偶数")
else :
    print("奇数")


year=2022
if year%4==0 and year%100!=0 :
    print("2022年是闰年")
else :
    print("2022年是平年")

score=61
grade= "过了" if score>=60 else "挂了"
print(grade)


################################ 循环for ##########################################
print("\nfor初尝试:")
whatthef="hell"
for i in whatthef:
    print (i,end="")

print("\n",end="")

for i in range(0,9,2):
    print (i,end="")

print("\n",end="")

for i in range(0,4,2):
    print (whatthef[i],end="")


print("\n斐波那契来10个:")

Fib1=[0,1]
print(Fib1[0],Fib1[1],end=" ")

for i in range(2,10,1):
     num2=Fib1[i-2]+Fib1[i-1]
     Fib1.append(num2)
     print(Fib1[i],end=" ")
   
################################ 循环while ##########################################
print("\nwhile初尝试:")

n=3
while n:
    print(n)
    n-=1
################################ 输入 ##########################################    
a=int(input("input number:")) #数字认成字符串
a+=a
print(a)

b=input("input string:")
print(b)

################################ 格式化输出 ########################################## 
print('试验输出字符串%s以及它的长度%d'%(firstring,len(firstring)))
pi=3.1415926
print('试验宽度5，精度2的小数%5.2f'%pi)




################################## try git #####################################
print("try branches")