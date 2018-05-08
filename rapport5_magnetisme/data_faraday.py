import numpy as np
import matplotlib.pyplot as plt

B = np.array([43, 63, 83, 102, 119])*1e-3/1.5 #Tesla
L = 30*1e-3 #M

theta_440_p = np.array([1.8, 2.8, 3.8, 4.2, 5.2])*2*np.pi/360
theta_440_m = np.array([1.4, 2.2, 2.8, 4.0, 4.8])*2*np.pi/360

theta_595_p = np.array([1.8, 2.6, 3.0, 4.0, 4.4])*2*np.pi/360
theta_595_m = np.array([1.4, 2.0, 2.8, 3.4, 4.0])*2*np.pi/360

theta_580_p = np.array([2.0, 2.8, 3.6, 4.4, 5.2])*2*np.pi/360
theta_580_m = np.array([1.6, 2.6, 3.2, 4.2, 4.8])*2*np.pi/360

uncertenty_theta = np.array([0.2, 0.2, 0.2, 0.2, 0.2])*2*np.pi/360
uncertenty_B = B*0.002 + 0.001*1e-3

delta_m = 1.9804
m = 36.5363
c = 1.1986e-04
delta_c = 0.0034
fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
plt.errorbar(B*L, theta_580_m, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='o', markersize='3.5', label=r"$I_{negativ}$")
plt.errorbar(B*L, theta_580_p, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='o', markersize='3.5', label=r"$I_{positiv}$")
plt.plot(B*L, c+m*B*L, "--")
plt.fill_between(x=B*L, y1=(c-delta_c)+B*L*(m-delta_m), y2=(c+delta_c)+B*L*(m+delta_m), edgecolor='black', alpha=0.175, color="green")
plt.tick_params(labelsize=18)
plt.legend(loc="best")
ax.set_xlabel(r"$|L\cdot B|$ [Tm]", fontsize=16)
ax.set_ylabel(r"Vinkel  $\theta$  [radianer]", fontsize=16)
plt.savefig("latex/faraday_effekt.pdf")
plt.show()
