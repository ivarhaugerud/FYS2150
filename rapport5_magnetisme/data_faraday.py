import numpy as np
import matplotlib.pyplot as plt

def linear_regresion(x, y):
    n = len(x)
    D = np.sum(np.square(x)) - (np.sum(x)**2)/n
    E = np.sum(x*y) - np.sum(x)*np.sum(y)/n
    F = np.sum(np.square(y)) - (np.sum(y)**2)/n

    delta_m = np.sqrt((1/(n-2))*(D*F-E**2)/(D**2))
    delta_c = np.sqrt(1/(n-2)*(D/n+np.mean(x)**2)*(D*F-E**2)/(D**2))
    m = E/D
    c = np.mean(y)-m*np.mean(x)

    return m, c, delta_m, delta_c

L = 30*1e-3 #M
delta_L = 0.1*L/100

theta_440_p = np.array([1.8, 2.8, 3.8, 4.2, 5.2])#*2*np.pi/360
theta_440_m = np.array([1.4, 2.2, 2.8, 4.0, 4.8])#*2*np.pi/360

theta_595_p = np.array([1.8, 2.6, 3.0, 4.0, 4.4])#*2*np.pi/360
theta_595_m = np.array([1.4, 2.0, 2.8, 3.4, 4.0])#*2*np.pi/360

theta_580_p = np.array([2.0, 2.8, 3.6, 4.4, 5.2])#*2*np.pi/360
theta_580_m = np.array([1.6, 2.6, 3.2, 4.2, 4.8])#*2*np.pi/360

uncertenty_theta = np.array([0.3, 0.3, 0.3, 0.3, 0.3])#*2*np.pi/360
"""
delta_m = 1.9804
m = 36.5363
c = 1.1986e-04
delta_c = 0.0034
"""

B = np.array([43, 63, 83, 102, 119])*1e-3/1.5 #Tesla
uncertenty_B = B*0.002 + 0.001*1e-3
"""
plt.plot(B, theta_580_p, "ro")
plt.plot(B, theta_580_m, "bo")
plt.show()

B_both = np.zeros(len(B)*2)
unc_BL_both = np.zeros(len(B)*2)
theta_both = np.zeros(len(B_both))

for i in range(len(B)):
    B_both[i] = B[i]
    unc_BL_both[i] = B_both[i]*L*np.sqrt((uncertenty_B[i]/B_both[i])**2 + (delta_L/L)**2)

for i in range(len(B)):
    B_both[i+len(B)] = B[i]
    unc_BL_both[i+len(B)] = unc_BL_both[i]

for i in range(len(B)):
    theta_both[i] = theta_595_m[i]
for i in range(len(B)):
    theta_both[i+len(B)] = theta_595_p[i]

m, c, delta_m, delta_c = linear_regresion(B_both*L, theta_both)
plt.plot(B_both*L, theta_both, "ro")
plt.plot(B_both*L, c + m*B_both*L)
print(m, delta_m)
plt.show()


"""
theta_both = np.zeros(len(B)*2)
B_both = np.zeros(len(B)*2)
unc_BL_both = np.zeros(len(B_both))
for i in range(len(B)):
    B_both[i] = -B[i]
    unc_BL_both[i] = B_both[i]*L*np.sqrt((uncertenty_B[i]/B_both[i])**2 + (delta_L/L)**2)

for i in range(len(B)):
    B_both[i+len(B)] = B[i]
    unc_BL_both[i+len(B)] = unc_BL_both[i]


"""
fig = plt.figure(figsize=(7.6, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
plt.errorbar(B*L, theta_580_m, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='o', markersize='3.5', label=r"$I_{negativ}$")
plt.errorbar(B*L, theta_580_p, yerr=uncertenty_theta, xerr=uncertenty_B, fmt='o', markersize='3.5', label=r"$I_{positiv}$")
plt.plot(B*L, c+m*B*L, "-", label="Lineærtilpasning")
#plt.fill_between(x=B_both*L, y1=(c-delta_c) + B_both*L*(m-delta_m), y2=(c+delta_c)+B_both*L*(m+delta_m), edgecolor='black', alpha=0.175, color="green")
plt.fill_between(x=B*L, y1=(c-delta_c) + B*L*(m-delta_m), y2=(c+delta_c)+B*L*(m+delta_m), edgecolor='black', alpha=0.175, color="green")

plt.tick_params(labelsize=18)
plt.legend(loc="best")
ax.set_xlabel(r"$|L\cdot B|$ [Tm]", fontsize=18)
ax.set_ylabel(r"Vinkel  |$\theta$|  [radianer]", fontsize=18)
plt.savefig("latex/faraday_effekt.pdf", fontsize=18)
plt.show()
"""

fig = plt.figure(figsize=(7.6, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)

for i in range(len(B)):
    theta_both[i] = -theta_440_m[i]
for i in range(len(B)):
    theta_both[i+len(B)] = theta_440_p[i]

theta_both = np.sort(theta_both)
print(theta_both)
m, c, delta_m, delta_c = linear_regresion(np.sort(B_both*L), np.sort(theta_both))
plt.errorbar(np.sort(B_both*L), theta_both, yerr=0.3*np.ones(len(B_both)), xerr=unc_BL_both, fmt='ro', markersize='3.5')
plt.plot(B_both*L, c+m*B_both*L, "r-", label=r"$\lambda = 440$nm", linewidth=0.85)
print(m, delta_m, 440)

for i in range(len(B)):
    theta_both[i] = -theta_580_m[i]
for i in range(len(B)):
    theta_both[i+len(B)] = theta_580_p[i]

m, c, delta_m, delta_c = linear_regresion(np.sort(B_both*L), np.sort(theta_both))
plt.errorbar(B_both*L, theta_both, yerr=0.3*np.ones(len(B_both)), xerr=unc_BL_both, fmt='bo', markersize='3.5',)
plt.plot(B_both*L, c+m*B_both*L, "b-", label=r"$\lambda = 580$nm", linewidth=0.85)
print(m, delta_m, 580)
for i in range(len(B)):
    theta_both[i] = -theta_595_m[i]
for i in range(len(B)):
    theta_both[i+len(B)] = theta_595_p[i]
m, c, delta_m, delta_c = linear_regresion(np.sort(B_both*L), np.sort(theta_both))
plt.errorbar(B_both*L, theta_both, yerr=0.3*np.ones(len(B_both)), xerr=unc_BL_both, fmt='go', markersize='3.5')
plt.plot(B_both*L, c+m*B_both*L, "g-", label=r"$\lambda = 595$nm", linewidth=0.85)
print(m, delta_m, 595)

plt.tick_params(labelsize=18)
plt.legend(loc="best", fontsize=18)
ax.set_xlabel(r"$L\cdot B$ [Tm]", fontsize=18)
ax.set_ylabel(r"Vinkel  $\theta$   [radianer]", fontsize=18)
plt.savefig("latex/faraday_effekt.pdf", fontsize=18)
plt.show()
