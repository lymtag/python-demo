# 年龄 = 18
# print(年龄)
# my_list = [5, 3, 8, 6, 1, 9]
# my_list.sort()
# my_list.append(7)
# my_list.reverse()
# print(my_list)
# weight=float(input('please input your weight(kg):'))
# hight=float(input('please input your hight(cm):'))
# BMI=weight/((hight/100)**2)
# print('your BMI is:%.1f'%BMI)
# if BMI<18.5:
#     print('过轻')
# elif BMI<25:
#     print('正常')
# elif BMI<28:
#     print('过重')
# elif BMI<32:
#     print('肥胖')
# else:
#     print('严重肥胖')
# print("您的正常体重范围为："
# "%.1fkg~%.1fkg"%(18.5*(hight/100)**2,25*(hight/100)**2))
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)

# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)
# n = 1
# while n <= 100:
#     print(n)
#     n = n + 1
# print('END')
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# def my_abs(x):
#     if x>=0:
#       return x
#     else:
#       return -x
# print(my_abs(-99))

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(1.2))

# import math

# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print(move(100,100,2))

# import math

# def quadratic(a, b, c):
#     pass

# 测试:
# print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
# print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

# if quadratic(2, 3, 1) != (-0.5, -1.0):
#     print('测试失败')
# elif quadratic(1, 3, -4) != (1.0, -4.0):
#     print('测试失败')
# else:
#     print('测试成功')


# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# print(enroll('lll',"f"))


# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)
#     print("kw",kw)
# print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

# 递归函数
# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(100))

# 切片
# L = list(range(100))
# print(L[:10])

# print(L[-10:])
# print(L[:10:2])
# print(L[::5])

# def trim(s):
#     return s

# # 测试:
# # 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
# def trim(s):
#     while s[0] == ' ':
#         s = s[1:]
#     while s[-1] == ' ':
#         s = s[:-2]
#     return s
# print(trim(' ABCDEFGHIJK   jack '))

# names = ['foo', 'bar', 'foobar']

# for name in names:
#     print(name)
# class Range7:
#     """生成一段范围内的可被 7 整除或包含 7 的整数

#     :param start: 开始数字
#     :param end: 结束数字
#     """

#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         # 使用 current 保存当前所处的位置
#         self.current = start

#     def __iter__(self):
#         return self

#     def __next__(self):
#         while True:
#             # 当已经到达边界时，抛出异常终止迭代
#             if self.current >= self.end:
#                 raise StopIteration

#             if self.num_is_valid(self.current):
#                 ret = self.current
#                 self.current += 1
#                 return ret
#             self.current += 1

#     def num_is_valid(self, num):
#         """判断数字是否满足要求"""
#         if num == 0:
#             return False
#         return num % 7 == 0 or '7' in str(num)
# r = Range7(0, 100)
# for num in r:
#   print(num)

# 定义函数
# def sayHi():
#     print("雷猴")

# # 调用函数
# sayHi()

# # 输出：雷猴

# def add(x, y):
#     # 因为字符串不能与数字类型直接相加，所以 x + y 的结果要用 str() 转成字符串
# 	print('x + y = ' + str(x + y))


# add(1, 2)
# 输出：3

# import random

# print(random.randint(1, 9))

# import requests 
# import sys 
 
# print(sys.executable)   # 应显示Anaconda路径 
# print(requests.get("https://www.example.com").status_code)   # 输出200则成功 

# from bs4 import BeautifulSoup
# import requests

# # 获取数据
# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}
# res = requests.get("https://movie.douban.com/top250", headers=headers).text

# print(res)

# 炒饭 = 50
# 水饺 = 45
# 点餐 = input("请问你想吃点什么？A:炒饭 B:水饺").upper().strip()
# if 点餐 == "A":
#   print(f"炒饭的价格是{炒饭}元")
# else:
#   print(f"水饺的价格是{水饺}元")

# def outer_function(x):
#   def inner_function(y):
#     return x + y
#     return inner_function

# closure = outer_function(10)
# result = closure(5)
# print(result)
# 正确密码 = "9527"
# for 次数 in range(5):
#   print(f"次数：{次数}")
#   密码 = input('请输入密码：')
#   if 密码 == 正确密码:
#     print("验证通过")
#     break
#   elif 密码 != 正确密码 and 次数 < 4:
#     print("密码错误")
#     print(f"剩余{4 - 次数}次机会")
#   else:
#     print("账号已被锁定")

# 店铺1 = {"地区":"杭州","面积":300,"评分": 5}
# 店铺2 = {"地区":"苏州","面积":200,"评分": 3}
# 店铺3 = {"地区":"宁波","面积":500,"评分": 4}
# 店铺列表 = [店铺1,店铺2,店铺3]
# 查询 = input("请输入地区：")
  
# class 饮料:
#   甜度 = 7
#   温度 = "常温"
#   def __init__(self,名称,杯型):
#     self.名称 = 名称
#     self.杯型 = 杯型

# 饮品 = 饮料('可乐','大杯')
# # 饮品.名称 = "可乐"
# print(饮品.甜度)
# print(饮品.温度)
# print(饮品.名称)
# print(饮品.杯型)


# 创建示例多项集
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # 策略：迭代一个副本
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)
# # 策略：创建一个新多项集
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# for i in range(5):
#     print(i)

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # 循环到底未找到一个因数
        print(n, 'is a prime number')

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 | 404:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"
 

# print(http_error(404))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
# print(where_is(Point(1,2)))

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# i = 5

# def f(arg=i):
#     print(arg)

# i = 6
# f()
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("11",fruits.count('apple'))

print("22",fruits.count('tangerine'))

print("33",fruits.index('banana'))

print("44",fruits.index('banana', 4))  # 从 4 号位开始查找下一个 banana

print("55",fruits.reverse())
print("66",fruits)

print("77",fruits.append('grape'))
print("88",fruits)

print("99",fruits.sort())
print("1010",fruits)

print("1111",fruits.pop())
print("1212",fruits)

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry 到了
queue.append("Graham")          # Graham 到了
queue.popleft()                 # 第一个到的现在走了

queue.popleft()                 # 第二个到的现在走了

print(queue)                         # 按到达顺序排列的剩余队列


squares = []
for x in range(10):
    squares = [x**2 for x in range(10)]
    # squares = list(map(lambda x: x**2, range(10)))
    # squares.append(x**2)

print(squares)

# dict() 构造函数可以直接用键值对序列创建字典：
dd = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dd)

aa = dict(sape=4139, guido=4127, jack=4098)
print(aa)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

basket = set(basket)
print("basket",basket)