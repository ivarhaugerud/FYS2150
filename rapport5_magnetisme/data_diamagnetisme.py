import numpy as np
import matplotlib.pyplot as plt
plt.minorticks_on()

def chi1(B1, B2, Fz, A):
    mu0 = 4*np.pi*1e-7
    return -2*mu0*Fz/(A*(B1**2-B2**2))

def chi1_linear(B1, B2, Fz, A):
    mu0 = 4*np.pi*1e-7
    return -2*mu0*Fz/(A*(B1-B2))

def chi2(B1, Fz, A):
    mu0 = 4*np.pi*1e-7
    return -2*mu0*Fz/(A*B1**2)

def uncertenty_chi1(chi, delta_b1, b, delta_fz, fz, delta_A, A):
    return chi*np.sqrt((2*delta_b1/b)**2 + (delta_fz/fz)**2 + (delta_A/A)**2)

def uncertenty_chi2(chi, delta_b1, b, delta_fz, fz, delta_A, A, delta_b2, b2):
    return chi*np.sqrt((2*delta_b1/b)**2 + (delta_fz/fz)**2 + (delta_A/A)**2 + (2*delta_b2/b2)**2)

def uncertenty_chi1_linear(chi, delta_b1, b, delta_b2, b2, delta_fz, fz, delta_A, A):
    return chi*np.sqrt((delta_b1/b)**2 + (delta_fz/fz)**2 + (delta_A/A)**2 + (delta_b2/b2)**2)

vismut_D = np.array([10.03, 10.06, 10.06, 10.03])*1e-3
vismut_D_unc = np.sqrt(np.std(vismut_D)**2 + (1/20)**2)*1e-3
R = np.mean(vismut_D)/2
R_unc = vismut_D_unc/2

I = np.linspace(0, 2.40, 13) #Ampere
I_unc = 0.01*I+3*1e-3
I_unc[-3:] = I[-3:]*0.01+30*1e-3

B1 = np.array([18., 96.4, 185.5, 280.5, 356.4, 433.7, 505.3, 570.9, 628.8, 677.9, 719.6, 755.6, 788.5])*1e-3 # Tesla
delta_B1 = B1*0.002 + 0.001*1e-3

B2 = np.array([0.43, 0.70, 1.16, 1.60, 1.96, 2.29, 2.32, 2.45, 2.45, 2.36, 2.45, 2.36, 2.30])*1e-3 #Tesla
delta_B2 = B2*0.002 + 0.001*1e-3

Mz = np.array([0.001, 0.001, 0.02, 0.03, 0.06, 0.10, 0.13, 0.16, 0.20, 0.24, 0.26, 0.28, 0.31])*1e-3 #kg
Fz = Mz*9.81 #Newton

delta_M = np.ones(len(Fz))*0.01*1e-3 #kg
#delta_G = np.zeros(len(Fz))*9.81*1e-3 #m/s2
delta_Fz = Fz*np.sqrt((delta_M/Mz)**2)# + (delta_G/9.81)**2)
delta_Fz[0] = delta_Fz[2]
delta_Fz[1] = delta_Fz[2]

print(Fz)
print(delta_Fz/Fz)
A = np.pi*(R)**2
delta_A = A*2*R_unc**2/R
chi_b = chi1(B1, B2, Fz, A)
chi_o = chi2(B1, Fz, A)
chi_lin = chi1_linear(B1, B2, Fz, A)
delta_chi_lin = uncertenty_chi1_linear(chi_lin, delta_B1, B1, delta_B2, B2, delta_Fz, Fz, delta_A, A)
delta_chi_b = uncertenty_chi2(chi_b, delta_B1, B1, delta_Fz, Fz, delta_A, A, delta_B2, B2)
delta_chi_o = uncertenty_chi1(chi_o, delta_B1, B1, delta_Fz, Fz, delta_A, A)

delta_chi_b[0] = delta_chi_b[2]*1.2
delta_chi_b[1] = delta_chi_b[2]*1.1
delta_chi_o[0] = delta_chi_o[2]*1.2
delta_chi_o[1] = delta_chi_o[2]*1.1


"""
fig = plt.figure(figsize=(7.2, 7.8), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
plt.errorbar(B1, Fz*1e3, xerr=delta_B1, yerr=delta_Fz*1e3, fmt='ko', markersize='3.5')
ax.set_xlabel(r"Magnetfelt $B$ [T]", fontsize=14)
ax.set_ylabel(r"Magnetisk kraft  $Fz$ [mN]", fontsize=14)
plt.savefig("latex/Fz.pdf")
plt.show()

fig = plt.figure(figsize=(7.2, 7.8), dpi=100)
ax = fig.add_subplot(111)
plt.style.use("bmh")
plt.minorticks_on()
font = {"size"  : 14}
plt.rc('font', **font)
plt.errorbar(I, (chi_o-chi_b)*1e4, xerr=I_unc, yerr=delta_chi_o*1e4, fmt='ko', markersize='3.5')
ax.set_xlabel(r"Strøm $I$ [A]", fontsize=14)
ax.set_ylabel(r"Forskjell i magnetisk susceptibilitet $ \times 10^4$ $\Delta \chi$", fontsize=14)
plt.savefig("latex/difference_b1b2.pdf")
plt.show()
"""
last_elem = 7
mean = -1.5695e-4#np.mean(chi_o[-last_elem:])
std = np.std(chi_o[-last_elem:])
std = np.sqrt(np.mean(delta_chi_o[-last_elem:])**2 + std**2)
print(std, "STD")
print(np.mean(delta_chi_o[-last_elem:]), "average unc")
print(mean*1e4, std*1e4)
fig = plt.figure(figsize=(7.5, 7.5), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
#plt.rc('font', **font)
ax = fig.add_subplot(111)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)
plt.errorbar(I, chi_o*1e4, xerr=I_unc, yerr=delta_chi_o*1e4, fmt='ko', markersize='3.5', label="Kvadratisk")
plt.errorbar(I, chi_lin*1e4, xerr=I_unc, yerr=delta_chi_lin*1e4, fmt='ro', markersize='3.5', label="Lineær")
plt.fill_between(x=I[-last_elem:], y1=np.ones(last_elem)*(mean-std)*1e4, y2=np.ones(last_elem)*(mean+std)*1e4, label=r"$\langle \chi \rangle \pm \sigma$")
plt.axis([0.3, 2.5, -3, 0.8])
plt.legend(loc="best", fontsize=18)

#plt.errorbar(B1, chi1_linear(B1, B2, Fz, A)*1e4, xerr=delta_B1, yerr=uncertenty_chi1_linear(chi1_linear(B1, B2, Fz, A), delta_B1, B1, delta_Fz, Fz, delta_A, A)*1e4, fmt='ro', markersize='3.5')
ax.set_xlabel(r"Strøm $I$ [A]", fontsize=16)
ax.set_ylabel(r"Magnetisk susceptibilitet  $\chi\times 10^{-4}$", fontsize=16)
plt.savefig("latex/chi_effekt.pdf")
plt.show()
print(I)
print(chi_o)
print(chi_b)
delta_chi = chi_o[-last_elem:]*(B2[-last_elem:]**2/B1[-last_elem:]**2)
#print(delta_chi)
print(np.mean(delta_chi_o[-last_elem:]))
print(np.mean(delta_chi_b[-last_elem:]))
unc_delta_chi = delta_chi*np.sqrt((delta_B2[-last_elem:]/B2[-last_elem:])**2 + (delta_B1[-last_elem:]/B1[-last_elem:])**2)

last_elem = 7

fig = plt.figure(figsize=(7.5, 7.5), dpi=100)
plt.style.use("bmh")
plt.minorticks_on()
#plt.rc('font', **font)
ax = fig.add_subplot(111)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)

plt.errorbar(I, chi_b*1e4, xerr=I_unc, yerr=delta_chi_o*1e4, fmt='ko', markersize='3.5', label="quadratic")
plt.errorbar(I, chi_lin*1e4, xerr=I_unc, yerr=delta_chi_lin*1e4, fmt='ro', markersize='3.5', label="linear")
plt.axis([0.3, 2.5, -3, 0.8])
#plt.errorbar(B1, chi1_linear(B1, B2, Fz, A)*1e4, xerr=delta_B1, yerr=uncertenty_chi1_linear(chi1_linear(B1, B2, Fz, A), delta_B1, B1, delta_Fz, Fz, delta_A, A)*1e4, fmt='ro', markersize='3.5')
ax.set_xlabel(r"Strøm $I$ [A]", fontsize=18)
plt.legend(loc="best", fontsize=18)
ax.set_ylabel(r"Magnetisk susceptibilitet  $\chi\times 10^{-4}$", fontsize=18)
plt.savefig("latex/chi_effekt_linear.pdf")
plt.show()
