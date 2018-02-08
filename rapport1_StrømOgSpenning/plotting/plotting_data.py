import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
blue, = sns.color_palette("muted", 1)

def function(x,y):
    n=len(x)
    D=(sum(x**2))-(1/n)*(((sum(x)))**2)
    E=np.sum((x*y)) - (1/n)*np.sum(x)*np.sum(y)
    
    F=sum(y**2)-(1/n)*sum(y**2)**2
    m=E/D
    c=np.mean(y)-m*np.mean(x);
    delta_m= np.sqrt((1/(n-2))*(D*F-E**2)/(D**2))
    print(D)
    delta_c= np.sqrt((1/(n-2))*((D/n)+np.mean(x)**2)*(D*F-E**2)/(D**2))
    return m,c,delta_m,delta_c

freq_A = np.array([10, 100, 1000, 10000, 100000, int(1e6)  , 500, 5000, 50000]) #Hz
freq_B =np.array([10, 100, 1000, 10000, 100000, int(6*1e6), 500, 5000, 50000]) #Hz
amplitude_A = np.array([706.5, 695.5, 667.2, 664.9, 657.6, 603, 669.9, 665, 664.5])*1e-3 #volt
amplitude_B = np.array([698.4, 585.7, 107.3, 10.93, 1.02, 630*1e-3, 207.3, 21.79, 2.169])*1e-3 #volt
sigma_fa = np.array([500*1e-3, 6, 40, 600, 4*1e3, 200*1e3, 24.62, 0, 3.141])*1e-3
sigma_fb = np.array([500*1e-3, 5, 40, 600, 15*1e3, 1*1e9, 31.89, 400.3, 24.3*1e3])*1e-3
sigma_av = np.array([20, 30, 20, 20, 30, 50, 22, 23.22, 47.76])*1e-6
sigma_bv = np.array([17, 28, 3, 1.1, 2, 10,  14.85, 1.493, 2.086])*1e-6
measurments_number = np.linspace(1, len(freq_A), len(freq_A))

log_y = np.log10(amplitude_B[-8:]/amplitude_A[-8:])
log_x = np.log10(freq_A[-8:])

[a, b, delta_a, delta_b] = function(log_x, log_y)
poly_foo = 10**(b)* 10**(a*log_x)
print(a, b, delta_a, delta_b)
fig = plt.figure(figsize=(7.2, 7.2), dpi=100)
font = {"size"  : 14}
plt.rc('font', **font)
ax = fig.add_subplot(111)
ax.set_yscale('log')
ax.set_xscale('log')
ax.plot(10**(log_x), poly_foo, "--")
ax.plot(freq_A, amplitude_B/amplitude_A, "bo")
plt.show()
y_0 = -b/a
print(y_0)
"""
def uncertenty_F75(x):
    error = np.zeros(len(x))
    for i in range(len(x)):
        error[i] = (1.5/100)*x[i] + 0.1
    return error

def uncertenty_F45(x):
    error = np.zeros(len(x))
    for i in range(len(x)):
        error[i] = (0.05/100)*x[i] + 0.0015
    return error

vr_10 = np.array([121.3, 102.1, 79])*1e-3
vr_10_V =np.array([1.246, 1.0508, 0.81265])

vr_1M = np.array([0.0046, 0.0066, 0.0089])*1e-3
vr_1M_V =np.array([4.25, 6.04, 8.22])

vi_10 = np.array([121.3, 102.0, 78.4])*1e-3
vi_10_V =np.array([1.956, 1.6462, 1.2685])

vi_1M = np.array([0.0042, 0.0060, 0.0081])*1e-3
vi_1M_V =np.array([4.22, 6.04, 8.22])

#print(uncertenty_F75(vr_10))
print(uncertenty_F45(vr_1M))

plt.plot(vr_10, vr_10_V)
plt.plot(vi_10, vi_10_V)
plt.plot(vr_10, vr_10_V, "ro")
plt.plot(vi_10, vi_10_V, "bo")
plt.show()

plt.plot(vr_1M, vr_1M_V, "ro")
plt.plot(vi_1M, vi_1M_V, "bo")
plt.plot(vr_1M, vr_1M_V)
plt.plot(vi_1M, vi_1M_V)
plt.show()

(a, b) = np.polyfit(vr_1M, vr_1M_V, 1)
(a1, b1) = np.polyfit(vi_1M, vi_1M_V, 1)
(a2, b2) = np.polyfit(vi_10, vi_10_V, 1)
(a3, b3) = np.polyfit(vr_10, vr_10_V, 1)
print(a, b, a1, b1)
print(a2, b2, a3, b3)
"""
