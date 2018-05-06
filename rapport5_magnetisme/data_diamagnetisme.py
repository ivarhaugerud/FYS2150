import numpy as np
import matplotlib.pyplot as plt
plt.minorticks_on()
plt.style.use("bmh")

def Chi(B1, B2, Fz, A):
    mu0 = 4*np.pi*1e-7
    return -2*mu0*Fz/(A*(B1**2-B2**2))

def Chi_B1(B1, Fz, A):
    mu0 = 4*np.pi*1e-7
    return -2*mu0*Fz/(A*B1**2)

def uncertenty_chi(delta_b1, b, delta_fz, fz, delta_A, A):
    chi*np.sqrt((delta_b1/b)**2 + (delta_fz/fz)**2 + (delta_A/A)**2)

I = np.linspace(0, 2.40, 13) #Ampere
B1 = np.array([18., 96.4, 185.5, 280.5, 356.4, 433.7, 505.3, 570.9, 628.8, 677.9, 719.6, 755.6, 788.5])*1e-3 # Tesla
B2 = np.array([0.43, 0.70, 1.16, 1.60, 1.96, 2.29, 2.32, 2.45, 2.45, 2.36, 2.45, 2.36, 2.30])*1e-3 #Tesla
Fz = np.array([0.0, 0.0, 0.02, 0.03, 0.06, 0.10, 0.13, 0.16, 0.20, 0.24, 0.26, 0.28, 0.31])*9.81*1e-3 #newton

D = 10.03*1e-3 #M
A = np.pi*(D/2)**2
chi = Chi(B1, B2, Fz, A)

plt.plot(B1, Fz, "ro")
plt.show()

plt.plot(I, chi, "ro")
plt.show()
