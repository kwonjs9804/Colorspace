
import numpy as np
import Color_Filter
import hist_mean


B = hist_mean.mean_value_b/255
G = hist_mean.mean_value_g/255
R = hist_mean.mean_value_r/255

print(B, G, R)


Color_Filter.Blue_CF_ndarray = np.array(Color_Filter.Blue_CF, float)
Color_Filter.Green_CF_ndarray = np.array(Color_Filter.Green_CF, float)
Color_Filter.Red_CF_ndarray = np.array(Color_Filter.Red_CF, float)
All = B*Color_Filter.Blue_CF_ndarray + G * \
    Color_Filter.Green_CF_ndarray + R*Color_Filter.Red_CF_ndarray
All_ndarray = np.array(All, float)
