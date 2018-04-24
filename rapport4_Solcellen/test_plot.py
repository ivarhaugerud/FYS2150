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
    return 0.1/100*R + 5*1e-3

def uncertenty_volt(V1):
    return (0.025*V1/100 + 60*1e-3)**2


#POSITIV RETNING
Rp = np.array([5, 10, 50, 100, 1000])
R_uncp = uncertenty_resistance(Rp)
Vlp = np.array([4.3929, 4.4790, 4.563, 4.5786, 4.5933])*1e3
Vlp_unc = np.sqrt(uncertenty_volt(Vlp) + (0.1862*1.5)**2) #assume same standard deviation as other measurments
Vp = np.array([652.21, 590.99, 525.63, 512.69, 500.03])
Vp_unc = np.sqrt(uncertenty_volt(Vp) + (0.1862*1.5)**2)
Ip = Vlp/Rp
Ip_unc = Ip*np.sqrt(np.square(Vlp_unc/Vlp) + np.square(R_uncp/Rp))


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
fig.suptitle(r"Strøm-spenning karakteristikk med og uten ytre spenning", fontsize=17, fontweight='bold')

#plt.errorbar(Vp/1000, Ip/1000, yerr=Vp_unc/1000, xerr=Ip_unc/1000, fmt='bo', markersize='2', label="positiv lederretnin m/spenning")
#plt.plot(Vp/1000, Ip/1000, "b--", linewidth=0.75)

#NEGATIV RETNIGN
Rn = np.array([1, 3, 10, 30, 100, 300, 1000])
R_uncn = uncertenty_resistance(Rn)

Vln = np.array([-153.29, -452.81, -1407.6, -4192.2, -5554.6, -5578.7, -5586.5])
Vln_unc = np.sqrt(uncertenty_volt(Vln) + (0.1862*1.5)**2)

Vn = np.array([-4932.6, -4634.0, -3617.3, -887.65, 463.82, 486.0, 493.27])
Vn_unc = np.sqrt(uncertenty_volt(Vn) + (0.1862*1.5)**2)
In = Vln/Rn
In_unc = In*np.sqrt(np.square(Vln_unc/Vln)+np.square(R_uncn/Rn))

V_tot = np.zeros(len(Vn)+len(Vp))
I_tot = np.zeros(len(Vn)+len(Vp))
I_tot_unc = np.zeros(len(Vn)+len(Vp))
V_tot_unc = np.zeros(len(Vn)+len(Vp))

V_tot[:len(Vn)] = Vn
V_tot[len(Vn):] = np.sort(Vp)
I_tot[:len(Vn)] = In
I_tot[len(Vn):] = np.sort(Ip)

I_tot_unc[:len(Vn)] = In_unc
I_tot_unc[len(Vn):] = Ip_unc
V_tot_unc[:len(Vn)] = Vn_unc
V_tot_unc[len(Vn):] = Vp_unc


plt.errorbar(V_tot/1000, I_tot/1000, yerr=V_tot_unc/1000, xerr=I_tot_unc/1000, fmt='ro', markersize='2', label="med ytre spenning")
plt.plot(V_tot/1000, I_tot/1000, "r--", linewidth=0.75)
ax.set_xlabel("Spenning [V]", fontsize=14)
ax.set_ylabel("Strøm    [A]", fontsize=14)
plt.errorbar(V2, I2, yerr=I2_unc, xerr=V2_unc, fmt='bo', markersize='2', label="uten ytre spenning")
plt.plot(V2[:-1], I2[:-1], "b--", linewidth=0.75)
#plt.scatter(V2[-1], I2[-1], s=120, facecolors='none', edgecolors='r', label="$V_{oc}=0.4979(2)$V")
#plt.scatter(V2[0],  I2[0], s=120, facecolors='none', edgecolors='k', label="$I_{sc}=-0.145(3)$A")
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.axis([-0.9, 0.6, -0.18, 0.12])
plt.legend(loc="best")
plt.savefig("latex/ytre_spenning_sammen.pdf")
plt.show()
