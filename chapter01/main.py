# chapter01 数据模型
# 模块：序列，迭代器，函数，类 上下文管理器
# 迭代 __getitem__
# 集合类
# 属性访问
# 运算符重载
# 函数和方法的调用
# 对象的创建和销毁
# 字符串表现形式和格式化
# 管理上下文
# collections.nametuple:用于构建只有少数属性但没有方法的对象
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
card = Card(suit='A', rank='heart')

# 从序列中随机选出一个元素
import random

attr = random.choice(range(100))

# 反向迭代
for i in reversed(range(10)):
    pass

# __contains__ String类的方法，判断给定子字符串是否是字符串的一部分
ret = 'a' in 'ha'

# 创建字典
ka = {'a': 0, 'b': 1, 'c': 2}
kb = dict(a=0, b=1, c=2)
kc = dict([('a', 0), ('b', 1), ('c', 2)])
kd = dict(zip(['a', 'b', 'c'], [0, 1, 2]))

# 创建列表
la = list('abcde')
lb = ['a', 'b', 'c', 'd', 'e']
lc = [i + 'a' for i in lb]
ld = list(range(5))

# 通过内置函数使用特殊方法，例子：二维向量的加法
from math import hypot


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r,%r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


v1 = Vector(3, 4)
v2 = Vector(3, 4)

# TODO 83个特殊方法
