import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)


vekt = np.array([0, 500.15, 1000.30, 1500.2, 2000.1, 2499.7, 3000.5, 3500.65])*1e-3 #kg
utslag  = (np.array([8.18, 7.45, 6.71, 6.03, 5.23, 4.49, 3.75, 2.99])-8.18)*1e-3 #m
usikkerhet = np.array([0, 1, 1, 1, 2, 3, 3, 3])*1e-5
print(utslag)
print(usikkerhet)
[a, b] = np.polyfit(vekt, utslag, 1)
print(a, b)
fig = plt.figure(figsize=(7.0, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
fig.suptitle(r"Nedbøying av messingstav som funksjon av vekt", fontsize=17, fontweight='bold')
plt.plot(vekt, b+vekt*a)
plt.errorbar(vekt, utslag, yerr=usikkerhet)
ax.set_xlabel("Vekt [kg]", fontsize=14)
ax.set_ylabel("Nedbøying [cm]", fontsize=14)
plt.savefig("pic/nedbojing.pdf")
plt.show()
