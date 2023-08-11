import sys
import matplotlib.pyplot as plt
import numpy as np
import Color_Filter

# 471 points per curves
# 360 nm to 830 nm

# declare functions
def SetWaveLengthGraph():
    major_xticks = list(range(400,800+100,100))
    minor_xticks = list(range(360-10,830+10,20))
    fig, ax = plt.subplots(figsize=(14,7))
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_xlim([360-10, 830+10]);
    #ax.tick_params(axis='x', labelsize=20, length=10, width=3, rotation=30)
    #ax.tick_params(axis='x', which='minor', length=5, width=2 )

def DrawColor_Filter():
    SetWaveLengthGraph()
    plt.title('Color Filter Curve')
    Color_Filter.Blue_CF_ndarray = np.array(Color_Filter.Blue_CF, float)
    Color_Filter.Green_CF_ndarray = np.array(Color_Filter.Green_CF, float)
    Color_Filter.Red_CF_ndarray = np.array(Color_Filter.Red_CF, float)
    A = 0.2*Color_Filter.Blue_CF_ndarray + 0.5*Color_Filter.Green_CF_ndarray + 0.7*Color_Filter.Red_CF_ndarray
    A_ndarray = np.array(A,float)
    plt.plot(Color_Filter.RangeWavelength, 0.2*Color_Filter.Blue_CF_ndarray, 'b', label='B')
    plt.plot(Color_Filter.RangeWavelength, 0.5*Color_Filter.Green_CF_ndarray, 'g', label='G')
    plt.plot(Color_Filter.RangeWavelength, 0.7*Color_Filter.Red_CF_ndarray, 'r', label='R')
    plt.plot(Color_Filter.RangeWavelength, A_ndarray , 'k', label='I(ramda)')
    plt.legend()
    plt.show()

# main

print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

DrawColor_Filter()