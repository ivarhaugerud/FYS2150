import numpy as np
import matplotlib.pyplot as plt

B = np.array([43, 63, 83, 102, 119])*1e-3 #Tesla
L = 30*1e-3 #M
theta_440_p = np.array([1.8, 2.8, 3.8, 4.2, 5.2])
theta_440_m = np.array([1.4, 2.2, 2.8, 4.0, 4.8])

theta_595_p = np.array([1.8, 2.6, 3.0, 4.0, 4.4])
theta_595_m = np.array([1.4, 2.0, 2.8, 3.4, 4.0])

theta_580_p = np.array([2.0, 2.8, 3.6, 4.4, 5.2])
theta_580_m = np.array([1.6, 2.6, 3.2, 4.2, 4.8])

uncertenty_theta = np.array([0.3, 0.3, 0.3, 0.3, 0.3])
uncertenty_B = B*0.002 + 0.001*1e-3

fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
plt.errorbar(B*L*1e3, theta_580_m, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='o', markersize='3.5', label=r"$\lambda=440$nm")
plt.errorbar(B*L*1e3, theta_580_p, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='o', markersize='3.5', label=r"$\lambda=440$nm")
plt.plot(B*L*1e3, 0.0069+B*L*1.3956e3, "--")
plt.fill_between(x=B*L*1e3, y1=(0.0069-0.1959)+B*L*(1.3956*1e3-75.6457), y2=(0.0069+0.1959)+B*L*(1.3956*1e3+75.6457), edgecolor='black', alpha=0.175, color="green")
plt.tick_params(labelsize=18)
ax.set_xlabel(r"$|L\cdot B|$ [mTm]", fontsize=16)
ax.set_ylabel(r"Vinkel  $\theta$  [$\degree$]", fontsize=16)
plt.savefig("latex/faraday_effekt.pdf")
plt.show()
