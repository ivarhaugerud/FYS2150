import numpy as np
import matplotlib.pyplot as plt

def get_B(deltaS):
    kappa = 1.01*1e-6 #weber
    n = 130 #vindinger
    A = 33*1e-6 #m^2
    D = 10 #dempningskonstant
    return kappa*D*deltaS/(A*n)

def get_H0(I):
    L = 315*1e-3 #meter
    N = 344
    return I*N/L

I_primary = np.linspace(4.5, 0.0, 10)
delta_I_prim = 0.001+0.5*I_primary/100

I_min = -np.array([4.55, 4.06, 3.65, 3.12, 2.69, 2.27, 1.86, 1.45, 0.96, 0.69])
I_max =  np.array([4.48, 3.99, 3.51, 3.03, 2.62, 2.20, 1.79, 1.31, 0.90, 0.62])
I_secondary = ((I_max-I_min)/2)
delta_I_secondary = I_secondary*np.sqrt(((I_min*0.1/100+0.01)/(I_min))**2 + ((I_max*0.1/100+0.01)/(I_max))**2)

S_max = np.array([810.53, 826.02, 810.53, 779.56, 738.26, 671.14, 588.54, 500.77, 423.34, 413.01])
S_min = -np.array([366.55, 299.43, 237.48, 180.69, 103.25, 20.65, -82.60, -201.34, -283.94, -340.73])
delta_S = S_max-S_min
delta_S_unc = delta_S*np.sqrt( ((0.1*S_max/100 + 0.01)/S_max) + ((((0.1*S_max/100 + 0.01)/S_max))))

mu_0 = 4*np.pi*1e-7
A = 33*1e-6 #m^2
delta_A = 0.1*A/100

B = get_B(delta_S)
delta_B = B*np.sqrt((delta_A/A)**2 + (delta_S_unc/delta_S)**2)

fig = plt.figure(figsize=(7.6, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 18}
plt.rc('font', **font)
ax = fig.add_subplot(111)
plt.plot(I_secondary, B, "--", linewidth=0.7)
plt.errorbar(I_secondary, B, yerr=delta_I_secondary, xerr=delta_B, fmt='o', markersize='3.5')
plt.tick_params(labelsize=18)
ax.set_xlabel(r"Strøm sekundærspole $I$ [A]", fontsize=18)
ax.set_ylabel(r"Magnetisk flukstetthet i sekundærspole $B$ [T]", fontsize=18)
plt.savefig("latex/magnetic_secondary_hysterese.pdf", fontsize=18)
plt.show()


#A = np.polyfit(H0, M, 1)
#M_num = np.polyval(A, H0)
#plt.plot(H0, M_num, "--")

L = 315*1e-3 #meter
delta_L = L/100
H0 = get_H0(I_primary)
delta_H0 = H0*np.sqrt((delta_L/L)**2 + (delta_I_prim/I_primary)**2)
delta_H0[-1] = delta_H0[-2]
M = B/mu_0 - H0
delta_M = np.sqrt((delta_B/mu_0)**2 + delta_H0**2)

fig = plt.figure(figsize=(7.6, 7.2), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 18}
plt.rc('font', **font)
ax = fig.add_subplot(111)
plt.plot(H0, M*1e-4, "--", linewidth=0.7)
plt.errorbar(H0, M*1e-4, yerr=delta_M*1e-4, xerr=delta_H0, fmt='o', markersize='3.5')
plt.tick_params(labelsize=18)
ax.set_xlabel(r"$H$-felt fra primærspolen $H_0$ [A/m]", fontsize=18)
ax.set_ylabel(r"Magnetisering av jernstang $M \cdot 10^4$ [A/m]", fontsize=18)
plt.savefig("latex/magnetisering.pdf", fontsize=18)
plt.show()
