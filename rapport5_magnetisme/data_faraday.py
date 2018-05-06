import numpy as np
import matplotlib.pyplot as plt

B = np.array([43, 63, 83, 102, 119])*1e-3 #Tesla
theta_440_p = np.array([1.8, 2.8, 3.8, 4.2, 5.2])
theta_440_m = np.array([1.4, 2.2, 2.8, 4.0, 4.8])

theta_595_p = np.array([1.8, 2.6, 3.0, 4.0, 4.4])
theta_595_m = np.array([1.4, 2.0, 2.8, 3.4, 4.0])

theta_580_p = np.array([2.0, 2.8, 3.6, 4.4, 5.2])
theta_580_m = np.array([1.6, 2.6, 3.2, 4.2, 4.8])

uncertenty_theta = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
uncertenty_B = 0.01*B


fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)

plt.errorbar(B, theta_440_m, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='ko', markersize='3.5', label=r"$\lambda=440$nm")
plt.errorbar(B, theta_440_p, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='ro', markersize='3.5', label=r"$\lambda=440$nm")

"""
plt.errorbar(B, theta_580_m, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='bo', markersize='3.5', label=r"$\lambda=440$nm")
plt.errorbar(B, theta_580_p, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='bx', markersize='3.5', label=r"$\lambda=440$nm")


plt.errorbar(B, theta_595_m, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='ko', markersize='3.5', label=r"$\lambda=440$nm")
plt.errorbar(B, theta_595_p, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='kx', markersize='3.5', label=r"$\lambda=440$nm")
"""

ax.set_xlabel(r"Magnetfelt $B$ [mT]", fontsize=14)
ax.set_ylabel(r"Vinkel  $\theta$  [radianer]", fontsize=14)
plt.legend(loc="best")
plt.savefig("latex/faraday_effekt.pdf")
plt.show()
