%{
U = 10.523 %mV
dU = 0.025/100
U*dU+0.002

U = 50.752
dU= 0.025/100
U*dU+0.002

I = 9.234
dI = 0.05/100
I*dI+0.005

I = 97.234
dI = 0.05/100
I*dI+0.005

sqrt(((0.002/10.253)^2 + (0.05/100.15)^2)*(100.15/10.253)^2)
sqrt((0.0893*0.2)^2 + (1.1491*9.81*3/100)^2)/(2*pi*sqrt(126.3/9.81))*100
%}
plot(t, T, 'o')
hold on
plot(t, T)
grid on
xlabel('tid [s]')
ylabel('temperatur [C]')
saveas('fig', 'fig_7.pdf')
fig = gcf;
fig.PaperPositionMode = 'auto'
fig_pos = fig.PaperPosition;
fig.PaperSize = [fig_pos(3) fig_pos(4)];
