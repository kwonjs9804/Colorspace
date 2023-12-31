import numpy as np

# 471 points per curves
# 360 nm to 830 nm

NumOfWavelengths = 471
StartWavelength = 360
EndWavelength = 830
RangeWavelength = list(range(StartWavelength, EndWavelength+1))

Blue_CF = [
    # Blue_CF  values
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.44,
    0.449,
    0.458,
    0.467,
    0.476,
    0.485,
    0.494,
    0.503,
    0.512,
    0.521,
    0.53,
    0.542,
    0.554,
    0.566,
    0.578,
    0.59,
    0.602,
    0.614,
    0.626,
    0.638,
    0.65,
    0.658,
    0.666,
    0.674,
    0.682,
    0.69,
    0.698,
    0.706,
    0.714,
    0.722,
    0.73,
    0.735,
    0.74,
    0.745,
    0.75,
    0.755,
    0.76,
    0.765,
    0.77,
    0.775,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.78,
    0.774,
    0.768,
    0.762,
    0.756,
    0.75,
    0.744,
    0.738,
    0.732,
    0.726,
    0.72,
    0.711,
    0.702,
    0.693,
    0.684,
    0.675,
    0.666,
    0.657,
    0.648,
    0.639,
    0.63,
    0.617,
    0.604,
    0.591,
    0.578,
    0.565,
    0.552,
    0.539,
    0.526,
    0.513,
    0.5,
    0.488,
    0.476,
    0.464,
    0.452,
    0.44,
    0.428,
    0.416,
    0.404,
    0.392,
    0.38,
    0.371,
    0.362,
    0.353,
    0.344,
    0.335,
    0.326,
    0.317,
    0.308,
    0.299,
    0.29,
    0.286,
    0.282,
    0.278,
    0.274,
    0.27,
    0.266,
    0.262,
    0.258,
    0.254,
    0.25,
    0.24,
    0.23,
    0.22,
    0.21,
    0.2,
    0.19,
    0.18,
    0.17,
    0.16,
    0.15,
    0.145,
    0.14,
    0.135,
    0.13,
    0.125,
    0.12,
    0.115,
    0.11,
    0.105,
    0.1,
    0.0999,
    0.0998,
    0.0997,
    0.0996,
    0.0995,
    0.0994,
    0.0993,
    0.0992,
    0.0991,
    0.099,
    0.0988,
    0.0986,
    0.0984,
    0.0982,
    0.098,
    0.0978,
    0.0976,
    0.0974,
    0.0972,
    0.097,
    0.0971,
    0.0972,
    0.0973,
    0.0974,
    0.0975,
    0.0976,
    0.0977,
    0.0978,
    0.0979,
    0.098,
    0.0982,
    0.0984,
    0.0986,
    0.0988,
    0.099,
    0.0992,
    0.0994,
    0.0996,
    0.0998,
    0.1,
    0.101,
    0.102,
    0.103,
    0.104,
    0.105,
    0.106,
    0.107,
    0.108,
    0.109,
    0.11,
    0.112,
    0.114,
    0.116,
    0.118,
    0.12,
    0.122,
    0.124,
    0.126,
    0.128,
    0.13,
    0.1315,
    0.133,
    0.1345,
    0.136,
    0.1375,
    0.139,
    0.1405,
    0.142,
    0.1435,
    0.145,
    0.1445,
    0.144,
    0.1435,
    0.143,
    0.1425,
    0.142,
    0.1415,
    0.141,
    0.1405,
    0.14,
    0.139,
    0.138,
    0.137,
    0.136,
    0.135,
    0.134,
    0.133,
    0.132,
    0.131,
    0.13,
    0.129,
    0.128,
    0.127,
    0.126,
    0.125,
    0.124,
    0.123,
    0.122,
    0.121,
    0.12,
    0.1195,
    0.119,
    0.1185,
    0.118,
    0.1175,
    0.117,
    0.1165,
    0.116,
    0.1155,
    0.115,
    0.1142,
    0.1134,
    0.1126,
    0.1118,
    0.111,
    0.1102,
    0.1094,
    0.1086,
    0.1078,
    0.107,
    0.1058,
    0.1046,
    0.1034,
    0.1022,
    0.101,
    0.0998,
    0.0986,
    0.0974,
    0.0962,
    0.095,
    0.0933,
    0.0916,
    0.0899,
    0.0882,
    0.0865,
    0.0848,
    0.0831,
    0.0814,
    0.0797,
    0.078,
    0.076,
    0.074,
    0.072,
    0.07,
    0.068,
    0.066,
    0.064,
    0.062,
    0.06,
    0.058,
    0.056,
    0.054,
    0.052,
    0.05,
    0.048,
    0.046,
    0.044,
    0.042,
    0.04,
    0.038,
    0.0352,
    0.0324,
    0.0296,
    0.0268,
    0.024,
    0.0212,
    0.0184,
    0.0156,
    0.0128,
    0.01,
    0.0105,
    0.011,
    0.0115,
    0.012,
    0.0125,
    0.013,
    0.0135,
    0.014,
    0.0145,
    0.015,
    0.0155,
    0.016,
    0.0165,
    0.017,
    0.0175,
    0.018,
    0.0185,
    0.019,
    0.0195,
    0.02,
    0.023,
    0.026,
    0.029,
    0.032,
    0.035,
    0.038,
    0.041,
    0.044,
    0.047,
    0.05,
    0.055,
    0.06,
    0.065,
    0.07,
    0.075,
    0.08,
    0.085,
    0.09,
    0.095,
    0.1,
    0.106,
    0.112,
    0.118,
    0.124,
    0.13,
    0.136,
    0.142,
    0.148,
    0.154,
    0.16,
    0.166,
    0.172,
    0.178,
    0.184,
    0.19,
    0.196,
    0.202,
    0.208,
    0.214,
    0.22,
    0.224,
    0.228,
    0.232,
    0.236,
    0.24,
    0.244,
    0.248,
    0.252,
    0.256,
    0.26,
    0.261,
    0.262,
    0.263,
    0.264,
    0.265,
    0.266,
    0.267,
    0.268,
    0.269,
    0.27,
    0.2705,
    0.271,
    0.2715,
    0.272,
    0.2725,
    0.273,
    0.2735,
    0.274,
    0.2745,
    0.275,
    0.2755,
    0.276,
    0.2765,
    0.277,
    0.2775,
    0.278,
    0.2785,
    0.279,
    0.2795,
    0.28,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

Green_CF = [
    # Green_CF  values
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.045,
    0.0451,
    0.0452,
    0.0453,
    0.0454,
    0.0455,
    0.0456,
    0.0457,
    0.0458,
    0.0459,
    0.046,
    0.0462,
    0.0464,
    0.0466,
    0.0468,
    0.047,
    0.0472,
    0.0474,
    0.0476,
    0.0478,
    0.048,
    0.0482,
    0.0484,
    0.0486,
    0.0488,
    0.049,
    0.0492,
    0.0494,
    0.0496,
    0.0498,
    0.05,
    0.0502,
    0.0504,
    0.0506,
    0.0508,
    0.051,
    0.0512,
    0.0514,
    0.0516,
    0.0518,
    0.052,
    0.0523,
    0.0526,
    0.0529,
    0.0532,
    0.0535,
    0.0538,
    0.0541,
    0.0544,
    0.0547,
    0.055,
    0.0555,
    0.056,
    0.0565,
    0.057,
    0.0575,
    0.058,
    0.0585,
    0.059,
    0.0595,
    0.06,
    0.07,
    0.08,
    0.09,
    0.1,
    0.11,
    0.12,
    0.13,
    0.14,
    0.15,
    0.16,
    0.174,
    0.188,
    0.202,
    0.216,
    0.23,
    0.244,
    0.258,
    0.272,
    0.286,
    0.3,
    0.316,
    0.332,
    0.348,
    0.364,
    0.38,
    0.396,
    0.412,
    0.428,
    0.444,
    0.46,
    0.4755,
    0.491,
    0.5065,
    0.522,
    0.5375,
    0.553,
    0.5685,
    0.584,
    0.5995,
    0.615,
    0.6275,
    0.64,
    0.6525,
    0.665,
    0.6775,
    0.69,
    0.7025,
    0.715,
    0.7275,
    0.74,
    0.751,
    0.762,
    0.773,
    0.784,
    0.795,
    0.806,
    0.817,
    0.828,
    0.839,
    0.85,
    0.8575,
    0.865,
    0.8725,
    0.88,
    0.8875,
    0.895,
    0.9025,
    0.91,
    0.9175,
    0.925,
    0.9285,
    0.932,
    0.9355,
    0.939,
    0.9425,
    0.946,
    0.9495,
    0.953,
    0.9565,
    0.96,
    0.962,
    0.964,
    0.966,
    0.968,
    0.97,
    0.972,
    0.974,
    0.976,
    0.978,
    0.98,
    0.977,
    0.974,
    0.971,
    0.968,
    0.965,
    0.962,
    0.959,
    0.956,
    0.953,
    0.95,
    0.935,
    0.92,
    0.905,
    0.89,
    0.875,
    0.86,
    0.845,
    0.83,
    0.815,
    0.8,
    0.78,
    0.76,
    0.74,
    0.72,
    0.7,
    0.68,
    0.66,
    0.64,
    0.62,
    0.6,
    0.58,
    0.56,
    0.54,
    0.52,
    0.5,
    0.48,
    0.46,
    0.44,
    0.42,
    0.4,
    0.39,
    0.38,
    0.37,
    0.36,
    0.35,
    0.34,
    0.33,
    0.32,
    0.31,
    0.3,
    0.293,
    0.286,
    0.279,
    0.272,
    0.265,
    0.258,
    0.251,
    0.244,
    0.237,
    0.23,
    0.226,
    0.222,
    0.218,
    0.214,
    0.21,
    0.206,
    0.202,
    0.198,
    0.194,
    0.19,
    0.187,
    0.184,
    0.181,
    0.178,
    0.175,
    0.172,
    0.169,
    0.166,
    0.163,
    0.16,
    0.158,
    0.156,
    0.154,
    0.152,
    0.15,
    0.148,
    0.146,
    0.144,
    0.142,
    0.14,
    0.1385,
    0.137,
    0.1355,
    0.134,
    0.1325,
    0.131,
    0.1295,
    0.128,
    0.1265,
    0.125,
    0.1225,
    0.12,
    0.1175,
    0.115,
    0.1125,
    0.11,
    0.1075,
    0.105,
    0.1025,
    0.1,
    0.098,
    0.096,
    0.094,
    0.092,
    0.09,
    0.088,
    0.086,
    0.084,
    0.082,
    0.08,
    0.078,
    0.076,
    0.074,
    0.072,
    0.07,
    0.068,
    0.066,
    0.064,
    0.062,
    0.06,
    0.058,
    0.056,
    0.054,
    0.052,
    0.05,
    0.048,
    0.046,
    0.044,
    0.042,
    0.04,
    0.037,
    0.034,
    0.031,
    0.028,
    0.025,
    0.022,
    0.019,
    0.016,
    0.013,
    0.01,
    0.0105,
    0.011,
    0.0115,
    0.012,
    0.0125,
    0.013,
    0.0135,
    0.014,
    0.0145,
    0.015,
    0.0155,
    0.016,
    0.0165,
    0.017,
    0.0175,
    0.018,
    0.0185,
    0.019,
    0.0195,
    0.02,
    0.023,
    0.026,
    0.029,
    0.032,
    0.035,
    0.038,
    0.041,
    0.044,
    0.047,
    0.05,
    0.055,
    0.06,
    0.065,
    0.07,
    0.075,
    0.08,
    0.085,
    0.09,
    0.095,
    0.1,
    0.105,
    0.11,
    0.115,
    0.12,
    0.125,
    0.13,
    0.135,
    0.14,
    0.145,
    0.15,
    0.155,
    0.16,
    0.165,
    0.17,
    0.175,
    0.18,
    0.185,
    0.19,
    0.195,
    0.2,
    0.205,
    0.21,
    0.215,
    0.22,
    0.225,
    0.23,
    0.235,
    0.24,
    0.245,
    0.25,
    0.251,
    0.252,
    0.253,
    0.254,
    0.255,
    0.256,
    0.257,
    0.258,
    0.259,
    0.26,
    0.2605,
    0.261,
    0.2615,
    0.262,
    0.2625,
    0.263,
    0.2635,
    0.264,
    0.2645,
    0.265,
    0.2655,
    0.266,
    0.2665,
    0.267,
    0.2675,
    0.268,
    0.2685,
    0.269,
    0.2695,
    0.27,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]

Red_CF = [
    # Red_CF Values
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.02,
    0.022,
    0.024,
    0.026,
    0.028,
    0.03,
    0.032,
    0.034,
    0.036,
    0.038,
    0.04,
    0.042,
    0.044,
    0.046,
    0.048,
    0.05,
    0.052,
    0.054,
    0.056,
    0.058,
    0.06,
    0.061,
    0.062,
    0.063,
    0.064,
    0.065,
    0.066,
    0.067,
    0.068,
    0.069,
    0.07,
    0.071,
    0.072,
    0.073,
    0.074,
    0.075,
    0.076,
    0.077,
    0.078,
    0.079,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.08,
    0.079,
    0.078,
    0.077,
    0.076,
    0.075,
    0.074,
    0.073,
    0.072,
    0.071,
    0.07,
    0.072,
    0.074,
    0.076,
    0.078,
    0.08,
    0.082,
    0.084,
    0.086,
    0.088,
    0.09,
    0.091,
    0.092,
    0.093,
    0.094,
    0.095,
    0.096,
    0.097,
    0.098,
    0.099,
    0.1,
    0.101,
    0.102,
    0.103,
    0.104,
    0.105,
    0.106,
    0.107,
    0.108,
    0.109,
    0.11,
    0.1115,
    0.113,
    0.1145,
    0.116,
    0.1175,
    0.119,
    0.1205,
    0.122,
    0.1235,
    0.125,
    0.1325,
    0.14,
    0.1475,
    0.155,
    0.1625,
    0.17,
    0.1775,
    0.185,
    0.1925,
    0.2,
    0.221,
    0.242,
    0.263,
    0.284,
    0.305,
    0.326,
    0.347,
    0.368,
    0.389,
    0.41,
    0.429,
    0.448,
    0.467,
    0.486,
    0.505,
    0.524,
    0.543,
    0.562,
    0.581,
    0.6,
    0.6075,
    0.615,
    0.6225,
    0.63,
    0.6375,
    0.645,
    0.6525,
    0.66,
    0.6675,
    0.675,
    0.6875,
    0.7,
    0.7125,
    0.725,
    0.7375,
    0.75,
    0.7625,
    0.775,
    0.7875,
    0.8,
    0.8017,
    0.8034,
    0.8051,
    0.8068,
    0.8085,
    0.8102,
    0.8119,
    0.8136,
    0.8153,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.817,
    0.8178,
    0.8186,
    0.8194,
    0.8202,
    0.821,
    0.8218,
    0.8226,
    0.8234,
    0.8242,
    0.825,
    0.8235,
    0.822,
    0.8205,
    0.819,
    0.8175,
    0.816,
    0.8145,
    0.813,
    0.8115,
    0.81,
    0.809,
    0.808,
    0.807,
    0.806,
    0.805,
    0.804,
    0.803,
    0.802,
    0.801,
    0.8,
    0.798,
    0.796,
    0.794,
    0.792,
    0.79,
    0.788,
    0.786,
    0.784,
    0.782,
    0.78,
    0.778,
    0.776,
    0.774,
    0.772,
    0.77,
    0.768,
    0.766,
    0.764,
    0.762,
    0.76,
    0.755,
    0.75,
    0.745,
    0.74,
    0.735,
    0.73,
    0.725,
    0.72,
    0.715,
    0.71,
    0.707,
    0.704,
    0.701,
    0.698,
    0.695,
    0.692,
    0.689,
    0.686,
    0.683,
    0.68,
    0.676,
    0.672,
    0.668,
    0.664,
    0.66,
    0.656,
    0.652,
    0.648,
    0.644,
    0.64,
    0.634,
    0.628,
    0.622,
    0.616,
    0.61,
    0.604,
    0.598,
    0.592,
    0.586,
    0.58,
    0.577,
    0.574,
    0.571,
    0.568,
    0.565,
    0.562,
    0.559,
    0.556,
    0.553,
    0.55,
    0.545,
    0.54,
    0.535,
    0.53,
    0.525,
    0.52,
    0.515,
    0.51,
    0.505,
    0.5,
    0.497,
    0.494,
    0.491,
    0.488,
    0.485,
    0.482,
    0.479,
    0.476,
    0.473,
    0.47,
    0.465,
    0.46,
    0.455,
    0.45,
    0.445,
    0.44,
    0.435,
    0.43,
    0.425,
    0.42,
    0.418,
    0.416,
    0.414,
    0.412,
    0.41,
    0.408,
    0.406,
    0.404,
    0.402,
    0.4,
    0.398,
    0.396,
    0.394,
    0.392,
    0.39,
    0.388,
    0.386,
    0.384,
    0.382,
    0.38,
    0.378,
    0.376,
    0.374,
    0.372,
    0.37,
    0.368,
    0.366,
    0.364,
    0.362,
    0.36,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0
]
