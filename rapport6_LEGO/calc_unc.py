import numpy as np
import matplotlib.pyplot as plt


V_on_v = 0.250
dV_on_v = 0.002

g = 9.819
dg = 0.003

I1 = 0.253
dI1 = 0.001

I2 = 0.0489
dI2 = 0.0002

I3 = 0.0489
dI3 = 0.0002


m1 = ((I1/g)*V_on_v*1e3)
m2 = ((I2/g)*V_on_v*1e3)
m3 = ((I3/g)*V_on_v*1e3)
delta_m1 = m1*np.sqrt((dV_on_v/V_on_v)**2 + (dg/g)**2 + (dI1/I1)**2)
delta_m2 = m2*np.sqrt((dV_on_v/V_on_v)**2 + (dg/g)**2 + (dI2/I2)**2)
delta_m3 = m3*np.sqrt((dV_on_v/V_on_v)**2 + (dg/g)**2 + (dI3/I3)**2)

print(100*delta_m1/m1, 100*delta_m2/m2, 100*delta_m3/m3)
