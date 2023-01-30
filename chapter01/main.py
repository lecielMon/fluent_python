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
# TODO 创建字典
# TODO 创建列表
# TODO 通过内置函数使用特殊方法，例子：二维向量的加法
# TODO 83个特殊方法
