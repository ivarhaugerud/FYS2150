dU=[-0.039 -0.077 -0.116 -0.154 -0.193 -0.231 -0.269 -0.307 -0.345 -0.383...
   0.000  0.039  0.078  0.117  0.156  0.195  0.234  0.273  0.312  0.352 ...
   0.391  0.431  0.470  0.510  0.549  0.589  0.629  0.669  0.709  0.749  ...
   0.790  0.830  0.870  0.911  0.951  0.992  1.033  1.074  1.114  1.155  ...
   1.196  1.238  1.279  1.320  1.362  1.403  1.445  1.486  1.528  1.570  ...
   1.612  1.654  1.696  1.738  1.780  1.823  1.865  1.908  1.950  1.993 ];
T=[-1:-1:-10 0:49];
[m, c, delta_c, delta_m] = function1(T, dU)

figure; hold on
set(gca,'fontsize',15)
h1 = plot(T, c+m*T); M1='Lineaer regresjon av data';
h2 = plot(T,dU,'*'); M2='Maalepunkter';
legend([h1; h2], M1, M2, 'Location','southeast');
set(h1(1),'linewidth',2);
xlabel('Temperatur [$^{\circ}$C]', 'Interpreter','latex')
ylabel('Termospenning $\Delta U$ [mV]', 'Interpreter','latex')



