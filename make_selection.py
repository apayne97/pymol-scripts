#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:34:28 2020

@author: alexpayne
"""

import yaml
from pymol import cmd, stored

## Very useful script
def make_selection(label = 'chainA', selection = 'chain A', structure_list = 'all', delete = False):
    ## Assume that selections should be made on all available objects
    if structure_list == 'all':
        structure_list = cmd.get_object_list()

    ## If this is not the case,
    else:
        ## Expects a space separated list of structures
        structure_list = structure_list.split(' ')
        
    for structure in structure_list:
        selname = f'{structure}_{label}'
        full_selection = f'{structure} and {selection}'
        print(f'Making {selname}: {full_selection}')
        cmd.select(selname, full_selection)
        
        ## Nifty way to get rid of a bunch of selections I just made if made by accident
        if delete:
            cmd.delete(selname)
            print(f'############ Deleted {selname}#############')


def sel_from_file(file_name, structure_list = 'all', delete = False):
    """
    This is a script that takes a yaml file and makes selections based on the file.

    :param file_name:
    :param structure_list:
    :param delete:
    :return:
    """

    ## Load in the yaml file as a dictionary
    with open(file_name) as file: seldict = yaml.full_load(file)

    print(f'Making selections for {structure_list}')
    for label, selection in seldict.items():
        make_selection(label, selection, structure_list, delete)

## This part is required to add to pymol
## First run `run make_selection.py`, and then you can run either `make_selection` or `sel_from_file`
cmd.extend('make_selection', make_selection)
cmd.extend('sel_from_file', sel_from_file)