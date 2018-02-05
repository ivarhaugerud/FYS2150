import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)

freq_A = np.array([10, 100, 1000, 10000, 100000, int(1e6)  , 500, 5000, 50000]) #Hz
freq_B = [10, 100, 1000, 10000, 100000, int(6*1e6), 500, 5000, 50000] #Hz
amplitude_A = np.array([706.5, 695.5, 667.2, 664.9, 657.6, 603, 669.9, 665, 664.5])*1e-3 #volt
amplitude_B = np.array([698.4, 585.7, 107.3, 10.93, 1.02, 630*1e-3, 207.3, 21.79, 2.169])*1e-3 #volt
sigma_fa = np.array([500*1e-3, 6, 40, 600, 4*1e3, 200*1e3, 24.62, 0, 3.141])*1e-3
sigma_fb = np.array([500*1e-3, 5, 40, 600, 15*1e3, 1*1e9, 31.89, 400.3, 24.3*1e3])*1e-3
sigma_av = np.array([20, 30, 20, 20, 30, 50, 22, 23.22, 47.76])*1e-6
sigma_bv = np.array([17, 28, 3, 1.1, 2, 10,  14.85, 1.493, 2.086])*1e-6
measurments_number = np.linspace(1, len(freq_A), len(freq_A))

log_y = np.log10(amplitude_B[-8:]/amplitude_A[-8:])
log_x = np.log10(freq_A[-8:])

[b, a] = np.polyfit(log_x, log_y, 1)
poly_foo = 10**(a)* 10**(b*log_x)
print(b)
fig = plt.figure(figsize=(7.2, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
ax.set_yscale('log')
ax.set_xscale('log')
ax.plot(10**(log_x), poly_foo)
ax.errorbar(freq_A, amplitude_B/amplitude_A, yerr=sigma_av+sigma_bv, xerr=sigma_fa, fmt='o', ecolor='g', capthick=2)
plt.show()
