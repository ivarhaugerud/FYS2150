import numpy as np
import matplotlib.pyplot as plt
plt.minorticks_on()
plt.style.use("bmh")

B = np.array([43, 63, 83, 102, 119])*1e-3 #Tesla
theta_440_p = np.array([1.8, 2.8, 3.8, 4.2, 5.2])
theta_440_m = np.array([1.4, 2.2, 2.8, 4.0, 4.8])

theta_595_p = np.array([1.8, 2.6, 3.0, 4.0, 4.4])
theta_595_m = np.array([1.4, 2.0, 2.8, 3.4, 4.0])

theta_580_p = np.array([2.0, 2.8, 3.6, 4.4, 5.2])
theta_580_m = np.array([1.6, 2.6, 3.2, 4.2, 4.8])
