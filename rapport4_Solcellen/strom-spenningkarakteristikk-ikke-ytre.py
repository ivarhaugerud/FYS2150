import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)

def uncertenty(matrix):
    N = len(matrix[:, 0])
    average = np.zeros(N)
    uncertenty = np.zeros(N)
    for i in range(N):
        n = len(np.trim_zeros(matrix[i, :]))
        average[i] = np.mean(np.trim_zeros(matrix[i, :]))
        uncertenty[i] = np.std(np.trim_zeros(matrix[i, :]))**2
    return average, uncertenty

def uncertenty_resistance(R):
    return (0.1/100)*R + 5*1e-3

def uncertenty_volt(V1):
    return (0.025*V1/100 + 60*1e-3)**2

#UTEN YTRE SPENNING
R = np.array([0.3, 0.5, 0.7, 1, 1.5, 2, 3, 4, 5, 1000]) #Ohm
R_unc = uncertenty_resistance(R)
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

VL, VL_unc = uncertenty(VL)
V, V_unc   = uncertenty(V)
V_unc  += uncertenty_volt(V)
VL_unc += uncertenty_volt(VL)
V_unc  = np.power(V_unc, 0.5)
VL_unc = np.power(VL_unc, 0.5)

I = VL/R
I_unc = I*np.sqrt(np.square(VL_unc/VL) + np.square(R_unc/R))
Voc = np.array([497.85, 497.86, 497.88])
Voc_unc = np.sqrt(uncertenty_volt(np.mean(Voc)) + np.std(Voc)**2)

V2 = np.zeros(len(VL)+1)
I2 = np.zeros(len(VL)+1)
V2_unc = np.zeros(len(VL)+1)
I2_unc = np.zeros(len(VL)+1)

V2[:-1] = V
V2[-1] = np.mean(Voc)
V2_unc[:-1] = V_unc
V2_unc[-1] = Voc_unc

I2[:-1] = I
I2[-1] = 0
I2_unc[:-1] = I_unc
I2_unc[-1] = I2_unc[-2]

print(V2[-1], V2_unc[-1])
print(I2[0], I2_unc[0])
V2 = V2/1000
I2 = I2/1000
I2_unc = I2_unc/1000
V2_unc = V2_unc/1000

fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
fig.suptitle(r"Strøm-spenning-karakteristikk for solcelle uten ytre spenning", fontsize=17, fontweight='bold')
plt.errorbar(V2, I2, yerr=I2_unc, xerr=V2_unc, fmt='o', markersize='2', label="målepunkter")
plt.plot(V2[:-1], I2[:-1], "--", linewidth=0.75)
plt.scatter(V2[-1], I2[-1], s=120, facecolors='none', edgecolors='r', label="$V_{oc}=0.4979(2)$V")
plt.scatter(V2[0],  I2[0], s=120, facecolors='none', edgecolors='k', label="$I_{sc}=-0.145(3)$A")
ax.set_xlabel("Spenning [V]", fontsize=14)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_ylabel("Strøm    [A]", fontsize=14)
plt.legend(loc='center left')
plt.savefig("latex/strom_spenning_karr.pdf")
plt.show()

#NOT TILTED

I2 = I2*1000
I2_unc = I2_unc*1000
V2_unc = V2_unc*1000
V2 = V2*1000
P = -I2[:-1]*V2[:-1]
P_unc = P*np.sqrt((I2_unc[:-1]/I2[:-1])**2 + (V2_unc[:-1]/V2[:-1])**2)
R_new = np.zeros(len(P))

#TILTED 60 degree
[R_belast, V_belast] = np.loadtxt("solcelle_optimal_belastning_60_grader.txt")

V_belast_unc = np.zeros(len(V_belast))
V_belast_unc[:-1] = V2_unc
V_belast_unc[-1] = V2_unc[-1]
R_belast_unc = uncertenty_resistance(R_belast)
I_belast = V_belast/R_belast
I_belast_unc = I_belast*np.sqrt((V_belast_unc/V_belast)**2 + (R_belast_unc/R_belast)**2)

P_belast = V_belast*I_belast
P_belast_unc = P_belast*np.sqrt((V_belast_unc/V_belast)**2 + (I_belast_unc/I_belast)**2)*5

fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
P_belast_unc = P_belast_unc*1e-3
fig.suptitle(r"Effekt av solcelle som funksjon av motstandslast", fontsize=17, fontweight='bold')
plt.errorbar(R_belast[:-1], P_belast[:-1]*1e-3, xerr=R_belast_unc[:-1]*2, yerr=P_belast_unc[:-1], fmt='ro', markersize='2', label="rotert $60\degree$")
plt.plot(R_belast[:-1], P_belast[:-1]*1e-3, "r--", linewidth=0.75)
plt.scatter(R[6], P[6]*1e-3, s=120, facecolors='none', edgecolors='b', label=r"max $P_{0\degree}=43.6(1)$mW")
plt.scatter(R_belast[6], P_belast[6]*1e-3, s=120, facecolors='none', edgecolors='r', label=r"max $P_{60\degree}=21.33(8)$mW")

print(P_belast[6], R_belast[6], I_belast[6], I_belast_unc[6], "here")
plt.errorbar(R[:-1], P[:-1]*1e-3, xerr=R_unc[:-1]*2, yerr=P_unc[:-1]*1e-3*2, fmt='bo', markersize='2', label="rotert $0\degree$")
plt.plot(R[:-1], P[:-1]*1e-3, "b--", linewidth=0.75)
ax.set_xlabel("Motstand [$\Omega$]", fontsize=14)
ax.set_ylabel("Effekt    [mW]", fontsize=14)
plt.legend(loc="best")
plt.axis([0.1, 10.5, 0.1, 45])
plt.savefig("latex/effekt.pdf")
plt.show()
