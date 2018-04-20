import numpy as np
import matplotlib.pyplot as plt
"""
def uncertenty(matrix):
    N = len(matrix[:, 0])
    large = 1000 #mV
    small = 100  #mV
    average = np.zeros(N)
    uncertenty = np.zeros(N)
    for i in range(N):
        n = len(np.trim_zeros(matrix[i, :]))
        average[i] = np.mean(np.trim_zeros(matrix[i, :]))
        if average[i] >= large:
            uncertenty[i] = (average[i]*0.025*1e-2 + 60*1e-6)/np.sqrt(n)
        else:
            uncertenty[i] = (average[i]*0.025*1e-2 + 6*1e-6)/np.sqrt(n)
    return average, uncertenty

#UTEN YTRE SPENNING
R = np.array([0.3, 0.5, 0.7, 1, 1.5, 2, 3, 4, 5, 1000]) #Ohm
VL = np.zeros((10, 11)) #mV
V  = np.zeros((10, 11)) #mV

#R=0.5
VL[1, :8] = -72-np.array([431, 246, 187, 322, 355, 393, 327, 276])*1e-3
V[1, :8]  = 79+np.array([215, 552, 518, 492, 401, 436, 471, 581])*1e-3

#R=1000
VL[9, :] = -497 - np.array([27, 7, 1, 2, 4, 8, 11, 13, 9, 11, 17])*1e-2
V[9, :10]  = 497 + np.array([33, 29, 26, 24, 23, 24, 25, 31, 27, 28])*1e-2

#R=0.3
VL[0, :9]  = -43 - np.array([738, 774, 782, 767, 749, 712, 624, 740, 831])*1e-3
V[0, :9]   = 50  + np.array([822, 834, 671, 690, 715, 730, 780, 803, 731])*1e-3

#R=3
VL[6, :9] = -358 - np.array([15, 71, 84, 115, 106, 121, 117, 91,  75])*1e-2
V[6, :10]  = 364  + np.array([64, 54, 46, 75, 29, 28, 46, 63, 82, 103])*1e-2

#R=1
VL[3, :] = -137 - np.array([9, 7, 5, 12, 16, 14, 33, 39, 38, 6, 11])*1e-2
V[3, :10]  =  144 + np.array([9, 29, 30, 22, 18, 36, 60, 55, 39, 46])*1e-2

#R=5
VL[8, :5] = -434 - np.array([4, 6, 13, 27, 14])*1e-2
V[8, :6]  = 438 + np.array([56, 86, 85, 79, 42, 50])*1e-2

#R=0.7
VL[2, :8] = -97 - np.array([842, 848, 857, 893, 735, 716, 744, 588])*1e-3
V[2, :7]  = 104 + np.array([73, 62, 66, 67, 65, 64, 71])*1e-2

#R=1.5
VL[4, :6] = -202 - np.array([104, 74, 41, 57, 139, 199])*1e-2
V[4, :6]  = 211 + np.array([40, 50, 21, 90, 31, -37])*1e-2

#R=2
VL[5, :6] = -263 - np.array([87, 56, 87, 103, 170, 125])*1e-2
V[5, :8]  = 270 + np.array([81, 5, 53, 80, 76, 44, 20, 16])*1e-2

#R=4
VL[7, :6] = -412 - np.array([65, 110, 85, 94, 69, 72])*1e-2
V[7, :8]  = (0.41 + np.array([89, 83, 81, 77, 76, 79, 79, 80])*1e-4)*1e3

VL_value, VL_unc = uncertenty(VL)
V_value, V_unc = uncertenty(V)
I_value = VL_value/R
Voc = 497.86 #mV

plt.plot(V_value, I_value, "bo")
plt.plot(Voc, 0, "bo")
plt.plot(V_value[0], I_value[0], "ro")
plt.plot(V_value, I_value, "b")
plt.show()

#NOT TILTED
I = VL_value[:-1]/R[:-1]
P = -I*V_value[:-1]
"""

#TILTED 60 degree
[R_belast, V_belast] = np.loadtxt("solcelle_optimal_belastning_60_grader.txt")
I_belast = V_belast/R_belast
P_belast = V_belast*I_belast
plt.plot(R_belast, P_belast, "ro")
plt.plot(R_belast, P_belast, "r")
plt.show()
