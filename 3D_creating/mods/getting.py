# -*- coding: utf-8 -*-
# 各种的运算

import math
import os
import sys
from math import acos


def getting_path(parent_dir, now_dir):
    '添加要导入的目录到sys中,只能作用于当前文件目录树内'
    now = os.getcwd().replace('{}'.format(parent_dir), '{}'.format(now_dir))
    sys.path.append(now)
    return now


def changing_rad(rad):
    '将弧度制转化成角度制'
    try:
        rad*rad
    except TypeError:
        raise Exception(
            'Invalid rad')
    return 180*rad/math.pi


def checking(func):
    '执行检查的函数'
    '''
    只能检查向量运算
    '''
    def return_func(*graphics_CLASS):

        if len(graphics_CLASS) == 0:

            raise Exception(
                'Invalid Argph: not an effective tuple')

        if func.__name__ == 'mold_solving':

            if len(graphics_CLASS) != 1:

                raise Exception(
                    '''Invalid Argph: cann'not get mold to vecs''')

            if graphics_CLASS[0].simple['coordinate'] != 'vector':
                raise Exception(
                    'Invalid Argph')

            else:
                return func(graphics_CLASS[0])    

        checker = []

        for i in range(1, len(graphics_CLASS)+1):
            checker.append(graphics_CLASS[i-1].cl)

        if checker == ['vector', 'vector'] and \
           func.__name__ == 'getting_angle':

            if len(graphics_CLASS[0].simple['coordinate']) != 3:

                raise Exception(
                    '{} Error: wrong graphics_CLASS'.format(func.__name__)
                    + ''''s list''')

            return func(graphics_CLASS[0], graphics_CLASS[1])

        if checker != ['vector', 'vector']:
            raise Exception(
                'Invalid graphics_CLASS: can not do these to a point')

        if graphics_CLASS[0].simple['cl'] == 'vector' and \
           func.__name__ == 'mold_solving':

            return func(graphics_CLASS[0])

        if graphics_CLASS[0].simple['cl'] == 'point' and \
           func.__name__ in ['getting_angle', 'mold_solving']:

            raise Exception(
                'Invalid graphics_CLASS: can not do these to a point')

        else:
            raise Exception('Invalid graphics_CLASS')

    return return_func


def mold_solving(graphics_CLASS):
    '求向量的模'
    x, y, z = graphics_CLASS.simple['coordinate']
    i = x**2 + y**2 + z**2

    return i**0.5


@checking
def getting_angle(graphics_CLASS, Normal_vectors):
    '计算夹角'
    mold = mold_solving(graphics_CLASS)*mold_solving(Normal_vectors)
#   不能为零向量
    if mold == 0:
        raise Exception('Invalid graphics_CLASS: can not do this to 0-vec')

    x1, y1, z1 = graphics_CLASS.simple['coordinate']
    x2, y2, z2 = Normal_vectors.simple['coordinate']

    cos_Angle = (x1*x2 + y1*y2 + z1*z2)/mold
    sin_Angle = (1 - cos_Angle**2)**0.5
    tan_Angle = cos_Angle/sin_Angle
#   Angle_rad:弧度制
    Angle_rad = acos(cos_Angle)

    all_dict = {
        'cos_Angle': cos_Angle,
        'sin_Angle': sin_Angle,
        'tan_Angle': tan_Angle,
        'Angle_rad': Angle_rad,
        'Angle': changing_rad(Angle_rad),
        'vecs': [
            graphics_CLASS, Normal_vectors
        ]
    }

    return all_dict


def getting_Stt_line_equa():
    '由两点确定直线方程'


def getting_Normal_vectors():
    '计算平面的法向量'
