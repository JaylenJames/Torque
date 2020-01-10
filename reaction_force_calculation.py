#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 13:30:13 2020

Calculation of ground reaction force on the foot.

@author: JaylenJames
"""
import pandas as pd
import numpy as np


#Import CSV as a datafrome
int_list = list(range(1,45))
int_list_str = [str(i) for i in int_list]

int_list_2 = list(range(0,29))
squat_data_df = pd.read_csv("JameJ04_M Trial 1 squat.csv", names =  int_list_str) #int_list)


#Remove rows that aren't neeted
squat_data_drop_df = squat_data_df.drop(axis = 0, index = int_list_2)

#Determine number of cells that are non-zero

#Sum these values and also calculate their surface area.
#   Row Spacing = 0.33 in
#   Col Spaceing = 0.33 in



