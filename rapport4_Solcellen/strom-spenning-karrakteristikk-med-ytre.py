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

fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
fig.suptitle(r"Strøm-spenning karakteristikk med yte spenning på 5V", fontsize=17, fontweight='bold')

plt.errorbar(Vp/1000, Ip/1000, yerr=Vp_unc/1000, xerr=Ip_unc/1000, fmt='bo', markersize='3.5', label="positive lederretning")
plt.plot(Vp/1000, Ip/1000, "b--", linewidth=0.75)

#NEGATIV RETNIGN
Rn = np.array([1, 3, 10, 30, 100, 300, 1000])
R_uncn = uncertenty_resistance(Rn)

Vln = np.array([-153.29, -452.81, -1407.6, -4192.2, -5554.6, -5578.7, -5586.5])
Vln_unc = np.sqrt(uncertenty_volt(Vln) + (0.1862*1.5)**2)

Vn = np.array([-4932.6, -4634.0, -3617.3, -887.65, 463.82, 486.0, 493.27])
Vn_unc = np.sqrt(uncertenty_volt(Vn) + (0.1862*1.5)**2)
In = Vln/Rn
In_unc = In*np.sqrt(np.square(Vln_unc/Vln)+np.square(R_uncn/Rn))

plt.errorbar(Vn/1000, In/1000, yerr=Vn_unc/1000, xerr=In_unc/1000, fmt='ro', markersize='3.5', label="negativ lederretning")
plt.plot(Vn/1000, In/1000, "r--", linewidth=0.75)
ax.set_xlabel("Spenning [V]", fontsize=14)
ax.set_ylabel("Strøm    [A]", fontsize=14)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
plt.legend(loc="best")
plt.savefig("latex/ytre_spenning.pdf")
plt.show()
