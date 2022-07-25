"""
Author: Dr. Hui CHeng
Any questions about this code,
please email: hui.cheng@uis.no \n

"""

import numpy as np

# default global values, can be changed.
cr_top = 1.75/2.0  # [m]
cage_height = 1.5  # [m]
NT = 32  # 64
NN = 8  # 17

number_of_horizontal_line=0
# private function


def __gen_points():
    point_one_cage = []
    for j in range(NN+1):
        for i in range(0, NT):
            point_one_cage.append(
                [cr_top * np.cos(i * 2 * np.pi / float(NT)),
                 cr_top * np.sin(i * 2 * np.pi / float(NT)),
                 - j * cage_height / float(NN)])
    return point_one_cage


def __gen_lines():
    global number_of_horizontal_line
    line_element = []
    # for horizontal lines
    for j in range(NN+1):
        for i in range(NT-1):
            line_element.append([i+j*NT, 1+i+j*NT])
        line_element.append([(j+1)*NT-1,j*NT])
    number_of_horizontal_line=len(line_element)        
    # vertical con for netting
    for j in range(NN):
        for i in range(NT):
            line_element.append([i+j*NT, i+(1+j)*NT])
    return line_element


def __gen_surfs():
    surf_element = []
    for j in range(NN):
        for i in range(NT-1):
            surf_element.append([i+j*NT, i+(1+j)*NT,
                               1+i+j*NT, 1+i+(1+j)*NT])
            
        surf_element.append([1+i+j*NT, 1+i+(1+j)*NT,
                                 j*NT, 1+1+i+j*NT])
    return surf_element

# public function


def gen_cage():
    points = __gen_points()
    lines = __gen_lines()
    surfs = __gen_surfs()
    return points, lines, surfs
