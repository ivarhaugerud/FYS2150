import numpy as np
import matplotlib.pyplot as plt

def get_B(deltaS):
    kappa = 1.01*1e-6 #weber
    n = 130 #vindinger
    A = 33*1e-6 #m^2
    D = 10 #dempningskonstant
    return kappa*D*deltaS/(2*A*n)

def get_H0(I):
    L = 315*1e-3 #meter
    N = 344
    return I*N/L

I_primary = np.linspace(4.5, 0.0, 10)
I_min = -np.array([4.55, 4.06, 3.65, 3.12, 2.69, 2.27, 1.86, 1.45, 0.96, 0.69])
I_max =  np.array([4.48, 3.99, 3.51, 3.03, 2.62, 2.20, 1.79, 1.31, 0.90, 0.62])
I_secondary = ((I_max-I_min)/2)

S_max = np.array([810.53, 826.02, 810.53, 779.56, 738.26, 671.14, 588.54, 500.77, 423.34, 413.01])
S_min = -np.array([366.55, 299.43, 237.48, 180.69, 103.25, 20.65, -82.60, -201.34, -283.94, -340.73])
delta_S = S_max-S_min
mu_0 = 4*np.pi*1e-7

B = get_B(delta_S)
H0_p = get_H0(I_primary)
H0_s = get_H0(I_secondary)

Mp = B/mu_0 - H0_p
Ms = B/mu_0 - H0_s

plt.plot(I_primary, B, "ro")
plt.show()

#A = np.polyfit(H0, M, 1)
#M_num = np.polyval(A, H0)
#plt.plot(H0, M_num, "--")
plt.plot(H0_p, Mp, "bo")
plt.plot(H0_p, B/mu_0)
plt.plot(H0_s, Ms, "ro")
plt.show()
