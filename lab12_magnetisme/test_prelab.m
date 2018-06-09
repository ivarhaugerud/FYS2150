
a_para = [0.67, 21.8, 6.45, 6.3201]
delta_a_para = [0.01, 0.2, 0.02, 0.02]
a_tang = [5.99, 0.96, 0.98, 6.32]
delta_a_tang = [0.02, 0.01, 0.01, 0.02]

f = a_para./a_tang
delta_f = f.*sqrt((delta_a_tang/a_tang).^2+(delta_a_para/a_para).^2)
[D_par,D_tang, epsilon] = calc_D(f)
delta_epsilon = 4*epsilon.*delta_f./f

delta_D_par = D_par.*(delta_epsilon./epsilon).*sqrt(5 + 2*((1+epsilon)/(1-epsilon)).^2/((abs(log((1+epsilon)/(1-epsilon)))).^2))
delta_D_tang = D_tang.*delta_D_par./D_par

delta_B0 = 0.04
B0 = 5.04
limit_par = B0./D_par 
unc_limir_par = limit_par.*sqrt( (delta_B0/B0)^2 + (delta_D_par./D_par).^2 )
limit_tan = B0./D_tang 
unc_limir_tan = limit_tan.*sqrt( (delta_B0/B0)^2 + (delta_D_tang./D_tang).^2 )



%plot(f, D_par)
%f=1.75
%[D_par,D_tang, epsilon] = calc_D(f)

%L = 30e-3          %m
%delta_L = 1e-3     %m
%theta2 = theta*360/(2*pi)
%V = theta./(L*B)
%mean(V(3:end))
%plot(V, 'ro')
