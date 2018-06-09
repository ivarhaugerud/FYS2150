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

# old data position y0 = np.sort(np.array([78.6, 19.1+111.7, 111.7, 48.9, 27.6, -43.3, -90.7, -38.9-90.7, -65.5]))/10

#y0 = np.sort(np.array([0, 37.5, 76.0, 76.0+41.6, 76.0+86.9, 76.0+41.6+87.9, 0, -36.7, 81.7+76.0+86.9, 90.8+76.0+41.6+87.9]))
y0 = np.sort(np.array([0, 37.5, 76.0, 76.0+41.6, 76.0+86.9, 76.0+41.6+87.9, 0, 81.7+76.0+86.9, 90.8+76.0+41.6+87.9]))
delta_y0 = np.ones(len(y0))*0.01
delta_y0[1] = np.sqrt(0.01**2+0.01**2)
delta_y0[-1] = delta_y0[1]

#old data voltage diode x0 = np.sort(np.array([-272.9, -260.7, -264.5, -282.3, -289.1, -310.8, -325.4, -335.9, -317.0]))
#x0 = np.sort(np.array([-0.0577, -0.0510, -0.0403, -0.0267, -0.0119, 0.0035, -0.0572, -0.0596, 0.0161, 0.0294]))
x0 = np.sort(np.array([-0.0577, -0.0510, -0.0403, -0.0267, -0.0119, 0.0035, -0.0572, 0.0161, 0.0294]))
delta_x0 = np.ones(len(x0))*0.0001
#x0 = x0-np.mean(x0)
m, c, delta_m, delta_c = linear_regresion(x0, y0)

#delta_x0 *= 10
#delta_y0 *= 10

fig = plt.figure(figsize=(7.6, 7.2), dpi=100)
plt.style.use("bmh")
ax = fig.add_subplot(111)
for tick in ax.xaxis.get_major_ticks():
    tick.label.set_fontsize(16)
for tick in ax.yaxis.get_major_ticks():
    tick.label.set_fontsize(16)
plt.plot(x0, c+m*x0, "--", linewidth=1.5)
plt.errorbar(x0, y0, xerr=delta_x0, yerr=delta_y0, fmt='ko', markersize='4.0')


ax.set_xlabel(r"Voltage shadow sensor [mV]", fontsize=18)
ax.set_ylabel(r"Laser position [cm]", fontsize=18)
plt.savefig("fig/shadow_sensor_result.pdf")
plt.show()

print(m, c, delta_m, delta_c, "m, c, delta_m, delta_c")
print(delta_m/m, "delta_m/m")
