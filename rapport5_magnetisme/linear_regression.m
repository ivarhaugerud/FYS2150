B = [43, 63, 83, 102, 119]*1e-3/1.5;
L = 30*1e-3

B_tot = [B B]*L
theta_440_p =  [1.8, 2.8, 3.8, 4.2, 5.2]*2*pi/360;
theta_440_m =  [1.4, 2.2, 2.8, 4.0, 4.8]*2*pi/360;
theta_440 = [theta_440_p theta_440_m];
[m, c, delta_c, delta_m] = function1(B_tot, theta_440)

delta_m/m

theta_580_p =  [2.0, 2.8, 3.6, 4.4, 5.2]*2*pi/360;
theta_580_m =  [1.6, 2.6, 3.2, 4.2, 4.8]*2*pi/360;
theta_580 = [theta_580_p theta_580_m];
[m, c, delta_c, delta_m] = function1(B_tot, theta_580)
delta_m/m

theta_595_p =  [1.8, 2.6, 3.0, 4.0, 4.4]*2*pi/360;
theta_595_m =  [1.4, 2.0, 2.8, 3.4, 4.0]*2*pi/360;
theta_595 = [theta_595_p theta_595_m];
[m, c, delta_c, delta_m] = function1(B_tot, theta_595)
delta_m/m




