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

#filtered_y = scipy.signal.medfilt(experiment_values_float_df["Force"], kernel_size = 11)
#peaks_filt, _ = find_peaks(filtered_y)
#
#filt_time = np.linspace(0,7.98,len(filtered_y))
#plt.plot(filt_time, filtered_y)


force_vals = experiment_values_float_df[["Force"]].to_numpy()
one_d = force_vals.flatten()

#Obtain peaks
peaks, properties = find_peaks(one_d, height = 35, distance = 50)
prominences = peak_prominences(one_d, peaks)[0]

pressure_forces = properties["peak_heights"]



###########   Repeat for EMG data     ###########

squat_force_data_EMG_df = pd.read_csv("pressure_trials_squats_only.csv")

j_weight_newtons = 70

squat_force_data_EMG_float_df = squat_force_data_EMG_df.astype(float)
#squat_force_data_EMG_float_df.plot(x = "Index", y =" tibAnterior")

plt.figure()
plt.plot(np.linspace(0,7.98,len(squat_force_data_EMG_float_df[[' tibAnterior']])), squat_force_data_EMG_float_df[[' tibAnterior']] )

EMG_force_vals = squat_force_data_EMG_df[[' tibAnterior']].to_numpy()
EMG_one_d = EMG_force_vals.flatten()

#Obtain peaks
EMG_peaks, EMG_properties = find_peaks(EMG_one_d, height = 10, distance = 30)
#EMG_prominences = peak_prominences(EMG_one_d, peaks)[0]

EMG_fractions = EMG_properties["peak_heights"]/100

EMG_forces = EMG_fractions * j_weight_newtons


def cod_plot(x,y,xl,yl,t):
    plt.figure(figsize=(6.5,6),dpi=100)
    plt.scatter(x,y,s=40,c=[(0.81, 0.81, 0.81)],marker='o',edgecolors=[(0.3, 0.3, 0.3)],alpha=0.7)
    plt.plot([0,np.max(x)],[0,np.max(x)],c='k',linewidth=2)
    plt.xlabel(xl,fontsize=14)
    plt.ylabel(yl,fontsize=14)
    plt.title(t,fontsize=16)
    plt.xlim([0,np.max(x)])
    plt.ylim([0,np.max(x)])
    plt.tight_layout()
    plt.show()


cod_plot(EMG_forces, pressure_forces[:5], "EMG", "Pressure Mat", "One V One")

