import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)

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
V = np.zeros(len(VL_value)+1)
I = np.zeros(len(VL_value)+1)
V[:-1] = V_value
V[-1] = Voc
I[:-1] = I_value

fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
fig.suptitle(r"Strøm-spenning-karakteristikk for solcelle uten ytre spenning", fontsize=17, fontweight='bold')
plt.scatter(V, I)
plt.scatter(Voc, 0, s=120, facecolors='none', edgecolors='r', label="$V_{oc}$")
plt.scatter(V_value[0], I_value[0], s=120, facecolors='none', edgecolors='k', label="$I_{sc}$")
plt.plot(V, I, "b--")
print(V_value[0], I_value[0], "I")
print(Voc, 0, "V")
ax.set_xlabel("Spenning [mV]", fontsize=14)
ax.set_ylabel("Strøm    [mA]", fontsize=14)
plt.legend(loc="best")
plt.savefig("pic/strøm_spenning_karr.pdf")
plt.show()

#NOT TILTED
P = -I*V*1e-3
R_new = np.zeros(len(P))

#TILTED 60 degree
[R_belast, V_belast] = np.loadtxt("solcelle_optimal_belastning_60_grader.txt")
I_belast = V_belast/R_belast
P_belast = V_belast*I_belast*1e-3

fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
fig.suptitle(r"Effektivitet solcelle", fontsize=17, fontweight='bold')
plt.scatter(R_belast[:-1], P_belast[:-1], s=90)
plt.plot(R_belast[:-1], P_belast[:-1], "b--", label="Effektivitet $60\degree$")
plt.scatter(R[:-1], P[:-2], s=90)
plt.plot(R[:-1], P[:-2], "r--", label="Effektivitet $0\degree$")
ax.set_xlabel("Motstand [$\Omega$]", fontsize=14)
ax.set_ylabel("Effekt    [W]", fontsize=14)
plt.legend(loc="best")
plt.savefig("pic/effekt.pdf")
plt.show()


#POSITIV RETNING
R = np.array([5, 10, 50, 100, 1000])
Vl = np.array([4.3929, 4.4790, 4.563, 4.5786, 4.5933])*1e3
V = np.array([652.21, 590.99, 525.63, 512.69, 500.03])
I = Vl/R



fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
fig.suptitle(r"Strøm-spenning karakteristikk med yte spenning på 5V", fontsize=17, fontweight='bold')

plt.plot(V/1000, I/1000, "ro", label="positiv lederretning")
plt.plot(V/1000, I/1000, "r--")

#NEGATIV RETNIGN
R = np.array([1, 3, 10, 30, 100, 300, 1000])
Vl = np.array([-153.29, -452.81, -1407.6, -4192.2, -5554.6, -5578.7, -5586.5])
V = np.array([-4932.6, -4634.0, -3617.3, -887.65, 463.82, 486.0, 493.27])
I = Vl/R

plt.plot(V/1000, I/1000, "bo", label="negativ lederretning")
plt.plot(V/1000, I/1000, "b--")
ax.set_xlabel("Spenning [V]", fontsize=14)
ax.set_ylabel("Strøm    [A]", fontsize=14)
plt.legend(loc="best")
plt.savefig("latex/ytre_spenning.pdf")
plt.show()
