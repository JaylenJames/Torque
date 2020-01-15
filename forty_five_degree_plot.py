#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:00:41 2020

Importing force data to show 45 degree plot


@author: JaylenJames
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, peak_prominences
import scipy.signal

#Import CSV as a datafrome
int_list = list(range(1,6))
int_list_str = [str(i) for i in int_list]

#Rename Columns
squat_force_data_df = pd.read_csv("JameJ04 trial 1 squat_G_Force_from_Dan.csv", names =  ["Frame", "Time", "Absolute Time", "Raw Sum", "Force"])

#Drop first 30 rows
experiment_values_df = squat_force_data_df.drop(squat_force_data_df.index[:30]).drop(squat_force_data_df.index[-1])
experiment_values_no_abs_time_df = experiment_values_df.drop(["Absolute Time"], axis = 1)


experiment_values_float_df = experiment_values_no_abs_time_df.astype(float)


#Plot force vs time
experiment_values_float_df.plot(x = "Time", y = "Force")

filtered_y = scipy.signal.medfilt(experiment_values_float_df["Force"], kernel_size = 11)
peaks_filt, _ = find_peaks(filtered_y)

filt_time = np.linspace(0,7.98,len(filtered_y))
#plt.plot(filt_time, filtered_y)






force_vals = experiment_values_float_df[["Force"]].to_numpy()
one_d = force_vals.flatten()

#Obtain peaks
peaks, properties = find_peaks(one_d, height = 35, distance = 50)
prominences = peak_prominences(one_d, peaks)[0]
#
#contour_heights = one_d[peaks] - prominences
#plt.plot(one_d)
#plt.plot(peaks, one_d[peaks], "x")
#plt.vlines(x=peaks, ymin=contour_heights, ymax=one_d[peaks])
#plt.show()


#Repeat for EMG data



