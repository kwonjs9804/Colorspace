import sys
import matplotlib.pyplot as plt
import numpy as np
import Color_Filter
import CIE_XYZ_Curve
import CF_Cal


def SetWaveLengthGraph():
    major_xticks = list(range(400, 800+100, 100))
    minor_xticks = list(range(360-10, 830+10, 20))
    fig, ax = plt.subplots(figsize=(14, 7))
    ax.set_xticks(major_xticks)
    ax.set_xticks(minor_xticks, minor=True)
    ax.set_xlim([360-10, 830+10])
    # ax.tick_params(axis='x', labelsize=20, length=10, width=3, rotation=30)
    # ax.tick_params(axis='x', which='minor', length=5, width=2 )-


def Draw_Calculate():
    SetWaveLengthGraph()
    plt.title('Coordinate Calculate')
    CIE_XYZ_Curve.CIE_X_ndarray = np.array(CIE_XYZ_Curve.CIE_X, float)
    CIE_XYZ_Curve.CIE_Y_ndarray = np.array(CIE_XYZ_Curve.CIE_Y, float)
    CIE_XYZ_Curve.CIE_Z_ndarray = np.array(CIE_XYZ_Curve.CIE_Z, float)
    X = CF_Cal.All_ndarray * CIE_XYZ_Curve.CIE_X_ndarray
    Y = CF_Cal.All_ndarray * CIE_XYZ_Curve.CIE_Y_ndarray
    Z = CF_Cal.All_ndarray * CIE_XYZ_Curve.CIE_Z_ndarray
    X_ndarray = np.array(X, float)
    Y_ndarray = np.array(Y, float)
    Z_ndarray = np.array(Z, float)
    plt.plot(Color_Filter.RangeWavelength,
             X_ndarray, 'r', label='coordinate_X')
    plt.plot(Color_Filter.RangeWavelength,
             Y_ndarray, 'g', label='coordinate_Y')
    plt.plot(Color_Filter.RangeWavelength,
             Z_ndarray, 'b', label='coordinate_Z')
    plt.legend()
    plt.show()


print('Number of arguments: {}'.format(len(sys.argv)))
print('Argument(s) passed: {}'.format(str(sys.argv)))

# Draw_Calculate()

CIE_XYZ_Curve.CIE_X_ndarray = np.array(CIE_XYZ_Curve.CIE_X, float)
CIE_XYZ_Curve.CIE_Y_ndarray = np.array(CIE_XYZ_Curve.CIE_Y, float)
CIE_XYZ_Curve.CIE_Z_ndarray = np.array(CIE_XYZ_Curve.CIE_Z, float)
X = CF_Cal.All_ndarray * CIE_XYZ_Curve.CIE_X_ndarray
Y = CF_Cal.All_ndarray * CIE_XYZ_Curve.CIE_Y_ndarray
Z = CF_Cal.All_ndarray * CIE_XYZ_Curve.CIE_Z_ndarray
X_ndarray = np.array(X, float)
Y_ndarray = np.array(Y, float)
Z_ndarray = np.array(Z, float)


X_cor = X_ndarray.sum()
Y_cor = Y_ndarray.sum()
Z_cor = Z_ndarray.sum()

print(X_cor)
print(Y_cor)
print(Z_cor)

x = X_cor/(X_cor + Y_cor + Z_cor)
y = Y_cor/(X_cor + Y_cor + Z_cor)

print(x)
print(y)
