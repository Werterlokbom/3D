#-*-coding:utf-8-*-#

# 构建几何体的方法

from math import *
from threading import *
from getting import *
from random import randint
import sys
import os


# 对象关系：基本=>point, vector
# 全部都为 graphics_CLASS,但是point, vector没有子对象
# 加'\'的为关键属性
# 点举例
'''   A point :
           {
               "coordinate"(坐标) : list,
               "attribute"(属性) : "base"(标准)&"none"(自定义),
               "root"(父图形) : graphics_CLASS,
               "cl" : "point"
            }
'''


class Point():
    '''定义点类'''

    def __init__(self, coordinate, attribute, root):
        self.coordinate = coordinate
        self.attribute = attribute
        self.root = root
        self.cl = 'point'
        self.checking()
        self.point = {
            "coordinate": self.coordinate,
            "attribute": self.attribute,
            "root": self.root,
            "cl": "point"
        }
        self.get_cl()

    def checking(self):

        if len(self.coordinate) != 3:
            raise Exception(
                'Invaild coordinate')
        if self.attribute not in ['base', 'none']:
            raise Exception(
                'Invalid attribute')

    def get_cl(self):

        simple = self.point
        self.simple = simple
        return simple


# ===================================================================
# 向量举例：
'''   A vector :
           {
               
               \"coordinate"(坐标) : a point class,
               \"attribute"(属性) : "base"(标准)&"none"(自定义),
               \"root"(父图形) : graphics_CLASS,
            if attribute == "base":
               \"head_point" : a point class,
            else:                               
               "head_point" : None, 
               \"cl": "vectro"
           }
'''


class Vector():
    '''定义向量类'''

    def __init__(self, coordinate, attribute, root, head_point=None):
        '初始化'
        self.cl = 'vector'
        self.coordinate = coordinate
        self.attribute = attribute
        self.root = root
        self.head_point = head_point
        self.checking()
        self.vector = {
            'coordinate': self.coordinate,
            'attribute': self.attribute,
            'root': self.root,
            'head_point': self.head_point,
            'cl': self.cl
        }
        self.get_cl()

    def checking(self):
        '检测异常'
        try:
            self.coordinate.cl
        except AttributeError:
            raise Exception(
                'Invalid object: coordinate must be point_CLASS')
        
        if self.attribute == 'base':
            try:
                self.head_point.cl
            except AttributeError:
                raise Exception(
                    'Invalid object: head_point must be point_CLASS')
        
        if len(self.coordinate.coordinate) != 3:
            raise Exception(
                'Invalid list: the list is wrong')
        
        if self.attribute not in ['base', 'none']:
            raise Exception(
                'Invalid attribute: the attribute is wrong')

    def get_cl(self):

        simple = self.vector.copy()
        simple['coordinate'] = self.coordinate.get_cl()['coordinate']
        simple['head_point'] = self.head_point.get_cl()['coordinate']
        self.simple = simple
        return simple


# ====================================================================================
# 直线举例
'''
A line: 
        {
    \'cl': 'line',
    \'attribute': 'base' or 'none',\\base:3d; none:2d\\
    \'Straight-line_equ': a_dic=>{\'equ1':'a1X+b1Y+c1Z+d1=0', 'equ2':'a2X+b2Y+c2Z+d2=0'}\\'attribute'='base',
                                 {\'equ1':'a1M+b1N=0'}\\'attribute'='none',
    \'root': graphics_CLASS,
    'child': None or [graphics_CLASS] 
}
'''


class Line():
    def __init__(self, attribute, straight_line_equ, root, child=None):
        '定义直线类'
        self.cl = 'line'
        self.attribute = attribute
        self.root = root
        self.straight_line_equ = straight_line_equ
        self.child = child
        self.checking()
        self.line = {
            'cl': 'line',
            'attribute': self.attribute,
            'Straight-line_equ': self.straight_line_equ,
            'root': self.root,
            'child': self.child
        }
        self.get_cl()

    def checking(self):
        '检查Straight_line_equ'
        if self.attribute not in ['base', 'none']:
            raise Exception(
                'Invalid attribute: the attribute is wrong')
        
        if self.attribute == 'base' and len(self.straight_line_equ) != 2:
            raise Exception(
                'Invalid Straight_line_equ: the Straight_line_equ is wrong')
        
        if self.attribute == 'none' and len(self.straight_line_equ) != 1:
            raise Exception(
                'Invalid Straight_line_equ: the Straight_line_equ is wrong')
        
        try:
            self.straight_line_equ['equ1']
        
        except TypeError:
            raise Exception(
                'Invalid straight_line_equ')

    def get_cl(self):
        simple = self.line
        self.simple = simple
        return self.line


# =========================================================================================
# 射线举例
'''A ray :
        {
    \'cl': 'ray',
    \'dire_vector'(方向向量): A vectro class and the attribute must be 'base',
    \'ray_line_equ': a_dic=>{\'equ1':'a1X+b1Y+c1Z+d1=0', 'equ2':'a2X+b2Y+c2Z+d2=0'}\\'attribute'='base',
                                 {\'equ1':'a1M+b1N=0'}\\'attribute'='none',
    \'attribute': 'base' or 'none',\\base:3d; none:2d\\
    \'root': root,
    'child': None or [graphics_CLASS]
        }
'''


class Ray():
    '定义射线类'

    def __init__(self, dire_vector, attribute, straight_line_equ, root, child=None):
        self.cl = 'ray'
        self.dire_vector = dire_vector
        self.attribute = attribute
        self.straight_line_equ = straight_line_equ
        self.root = root
        self.child = child
        self.checking()
        self.ray = {
            'cl': 'ray',
            'dire_vector': self.dire_vector,
            'ray_line_equ': self.straight_line_equ,
            'attribute': 'base' or 'none',
            'root': root,
            'child': self.child
        }
        self.get_cl()

    def checking(self):
        '检查'
        if self.attribute not in ['base', 'none']:
            raise Exception(
                'Invalid attribute: the attribute is wrong')
        
        if self.dire_vector.cl != 'vector':
            raise Exception(
                'Invalid dire_vector')
        
        if self.dire_vector.attribute != 'base':
            raise Exception(
                'Invalid attribute: the deir_vector attribute is wrong')
        
        try:
            self.straight_line_equ['equ1']
        
        except TypeError:
            raise Exception(
                'Invalid straight_line_equ')
        
        if len(self.straight_line_equ) != 1:
            raise Exception(
                'Invalid Straight_line_equ: the Straight_line_equ is wrong')

    def get_cl(self):

        simple = self.ray.copy()
        simple['dire_vector'] = self.dire_vector.simple['coordinate']
        self.simple = simple
        return simple


# ===========================================================================
# 线段举例
'''A line_seg :
        {
    \'cl': 'line_seg'.
    \'attribute': 'base' or 'none',\\base:3d; none:2d\\,
    \'root': root.
    \'child': None or [graphics_CLASS]
    \'key_point': point class list,
        }
'''


class Line_seg():
    '定义线段'

    def __init__(self, attribute, root, key_point, child=None):
        self.cl = 'line_seg'
        self.attribute = attribute
        self.root = root
        self.key_point = key_point
        self.child = child
        self.checking()
        self.line_seg = {
            'cl': self.cl,
            'attribute': self.attribute,
            'root': self.root,
            'key_point': self.key_point,
            'child': self.child
        }
        self.get_cl()

    def checking(self):
        '检查'
        if self.attribute not in ['base', 'none']:
            raise Exception(
                'Invalid attribute: the attribute is wrong')
        
        if len(self.key_point) != 2:
            raise Exception(
                'Invalid key_point: the key_point is wrong')
        
        else:
            cl1, cl2 = self.key_point
            if [cl1['cl'], cl2['cl']] != ['point']:
                raise Exception(
                    'Invalid key_point: the key_point is wrong')

    def get_cl(self):

        simple = self.line_seg.copy()
        self.simple = simple
        return self.simple


# ======================================================================================
x1 = randint(1, 20)
y1 = randint(1, 20)
z1 = randint(1, 20)
x2 = randint(1, 20)
y2 = randint(1, 20)
z2 = randint(1, 20)
f = []

p1 = Point(coordinate=[x1, y1, z1], attribute='base', root=None)
p2 = Point(coordinate=[x2, y2, z2], attribute='base', root=None)

d1 = Vector(attribute='base', coordinate=p1, head_point=p2, root=None)
d2 = Vector(attribute='base', coordinate=p2, head_point=p1, root=None)


f = [p1, p2, d1, d2]
for i in f:
    print(i.get_cl())

print(getting_angle(d1, d2))
l = Line(attribute='base', root=None,
         straight_line_equ={'equ1': 'd', 'equ2': 'f'})
print(l.simple)
print(getting_angle(d1, d2))
input()