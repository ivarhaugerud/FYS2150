tau=[4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05]
m = 2
mean_tau = mean(tau)
k = 4*pi^2*m*mean_tau^(-2)

%delta_tau = std(tau)
delta_tau = std(tau)/(sqrt(length(tau) - 1))

delta_k = 8*pi^2*m*delta_tau/(mean_tau^3)
%task 5

delta_m_both = mean_tau/(2*pi^2)*sqrt(k^2*delta_tau^2 + (delta_k*mean_tau^2)/4)
delta_m_tau  = delta_tau*mean_tau*k/(2*pi^2)

2*m*delta_tau/mean_tau %m?te brukt p? piazza
k*mean_tau*delta_tau/(2*pi^2)*10^3

delta_m = delta_tau*sqrt(k)/(pi*sqrt(m))
(2*delta_tau*m/mean_tau)*10^2