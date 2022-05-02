#-*-coding:utf-8-*-#

#构建几何体的方法

from math import *
from threading import *
from getting import *
from random import randint
import sys
import os


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
               \"cl": "vec"
           }
'''

class Vector():
    """定义向量类"""

    def __init__(self, coordinate, attribute, root, head_point=None):
        '初始化'
        self.cl = 'vec'
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
        print(self.vector)
        try: 
            self.coordinate += []
        except TypeError as e:
            raise Exception(str(e)) from None           
        if len(self.coordinate) != 3:
            raise Exception('Invalid list: the list is wrong')
        if self.attribute not in ['base', 'none']:    
            raise Exception('Invalid attribute: the attribute is wrong')


#====================================================================================
            
class line():
    pass



