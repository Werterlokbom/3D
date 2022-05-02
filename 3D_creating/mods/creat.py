#-*-coding:utf-8-*-#

#构建几何体的方法

from array import array
from math import *
from threading import *
from getting import *
from random import randint
import sys
import os


#对象关系：基本=>point, vector
#全部都为 graphics_CLASS,但是point, vector没有子对象
#加'\'的为关键属性
#点举例
'''   A point :
           {
               "coordinate"(坐标) : list,
               "attribute"(属性) : "base"(标准)&"none"(自定义),
               "root"(父图形) : graphics_CLASS,
               "cl" : "point"
            }
'''
class point():
    '''定义点类'''
    
    def __init__(self, coordinate, attribute, root):
        self.coordinate = coordinate
        self.attribute = attribute
        self.root = root
        self.cl = 'point'
        self.point = {
            "coordinate": self.coordinate,
            "attribute": self.attribute,
            "root": self.root,
            "cl": "point"
        }
        
    def get_cl(self):
        return self.point


#===================================================================
#向量举例：
'''   A vector :
           {
               
               \"coordinate"(坐标) : list,
               \"attribute"(属性) : "base"(标准)&"none"(自定义),
               \"root"(父图形) : graphics_CLASS,
            if attribute == "base":
               \"head_point" : dic(字典) = {
               "coo_point_i" : list
                                          }
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
        self.vector = {
            'coordinate': self.coordinate,
            'attribute': self.attribute,
            'root': self.root,
            'head_point': self.head_point,
            'cl': self.cl
        }
#       检测异常
        try: 
            self.coordinate += []
        except TypeError as e:
            raise Exception(str(e)) from None           
        if len(self.coordinate) != 3:
            raise Exception('Invalid list: the list is wrong')
        if self.attribute not in ['base', 'none']:    
            raise Exception('Invalid attribute: the attribute is wrong')
    
    def get_cl(self):
        return self.vector


#====================================================================================
#直线举例
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
class line():
    def __init__(self, attribute, Straight_line_equ, root, child=None):
        '定义直线类'
        self.cl = 'line'
        self.attribute = attribute
        self.root = root
        self.Straight_line_equ = Straight_line_equ
        self.child = child
        self.line = {
            'cl': 'line',
            'attribute': self.attribute,
            'Straight-line_equ': self.Straight_line_equ,                                
            'root': self.root,
            'child': self.child
        }
#       检查Straight_line_equ
        if self.attribute not in ['base', 'none']:    
            raise Exception('Invalid attribute: the attribute is wrong')
        if attribute == 'base' and len(self.Straight_line_equ) != 2:
            raise Exception('Invalid Straight_line_equ: the Straight_line_equ is wrong')
        if attribute == 'none' and len(self.Straight_line_equ) != 1:
            raise Exception('Invalid Straight_line_equ: the Straight_line_equ is wrong')
    
    def get_cl(self):
        return self.line

#=========================================================================================
#射线举例
'''A ray :
        {
        \           
        \
        \
        \
        }
'''