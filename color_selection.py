#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:34:28 2020

@author: alexpayne
"""

import yaml
from pymol import cmd, stored


## Very useful script
def color_selection(name='chainA', structure_list='all', color='carbon'):
    if structure_list == 'all':
        structure_list = cmd.get_object_list()
    else:
        ## This is ugly. 
        ## It reminds me that I'm expecting a list, e.g. [7bv1, 7bv2]
        ## The structures should not be in quotes
        structure_list = structure_list.replace('[', '').replace(']', '').split(',')
        print(structure_list)

    for structure in structure_list:
        selname = f'{structure}_{name}'
        sel_list = cmd.get_names('selections')
        if not selname in sel_list:
            print(f'{selname} does not exist!!')
        else:
            cmd.set('cartoon_color', color, selname)
            cmd.set('surface_color', color, selname)


# def color_selection()

def col_from_file(file_name, structure_list='all', delete=False, color=True):
    with open(file_name) as file:
        coldict = yaml.full_load(file)
    for name, color in coldict.items():
        color_selection(name, structure_list, color)


cmd.extend('color_selection', color_selection)
cmd.extend('col_from_file', col_from_file)
