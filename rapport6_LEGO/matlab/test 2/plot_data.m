%%
figure(1)
diode2 = data(100:100:end, 3);%diode(7000:1000:end)*1e3;
coil2 = data(100:100:end-1, 2)*1e3;%coil(7000:1000:end)*1e3;
t2 = time(100:100:end-1, 1);

%size(diode2)
%size(coil2)
%size(t2)

coil2 = coil2-mean(coil2);
diode2 = diode2-mean(diode2);

scatter(diode2, coil2, 6.5 ,t2, 'filled')
grid(gca,'minor')
grid on
hAx=gca;
xlabel('diode voltage [mV]', 'FontSize', 17)
ylabel('coil voltage [mV]',  'FontSize', 17)
colormap('parula');
hcb = colorbar;
colorTitleHandle = get(hcb,'title');
titleString = 'Time [s]';
set(gca, 'FontSize', 16)
set(colorTitleHandle ,'string', titleString, 'FontSize', 15, 'FontSize', 15);
saveas(gcf,'phasespace.png')
hold off

%{
figure(2);
hold on

scatter(v(7000:100:end), coil(7000:100:end-1)*1e3, 6.5 ,time(7000:100:end-1), 'filled')
axis([-16 16 -4 4])
grid(gca,'minor')
grid on
hAx=gca;
xlabel('velocity [mm/s]', 'FontSize', 17)
ylabel('coil voltage [mV]',  'FontSize', 17)
colormap('parula');
hcb = colorbar;
colorTitleHandle = get(hcb,'title');
titleString = 'Time [s]';
set(colorTitleHandle ,'string', titleString, 'FontSize', 15, 'FontSize', 15);
set(gca, 'FontSize', 16)
saveas(gcf,'vel_vs_coil.png')
hold off
%}

%{
period_number = linspace(1, numel(BL)-10-10-10, numel(BL)-10-10-10);

%errorbar(t_BL(k0:end), BL(k0:end), dBL(k0:end), 'or')

figure(3);
hold on
errorbar(period_number, BL(28:end-3), dBL(28:end-3), 'o')
average = mean(BL(28:end-3))*ones(numel(period_number), 1);
S_T_D = std(BL(28:end-3))

plot(period_number, average)
grid(gca,'minor')
grid on
xlabel('period number [#]', 'FontSize', 17)
ylabel('slope coil vs velocity [T/m]',  'FontSize', 17)
set(gca, 'FontSize', 16)
axis([-3 100 0.243 0.258])
saveas(gcf,'slope.png')

S_T_D
average
%}
%{
y = [37.5 76.0 76.0+41.6 76.0+86.9 76.0+41.6+87.9 76.0+86.9+91.7 76.0+41.6+87.9+90.8]*1e-1;
x = [-0.0510 -0.0403 -0.0267 -0.0119 0.0035 0.0161 0.0294]*1e3;
[m, c, delta_c, delta_m] = function1(x, y)

figure(9)
plot(x, y, 'o')
hold on
plot(x, c+m*x)

grid(gca,'minor')
grid on
hAx=gca;
xlabel('diode voltage [mV]', 'FontSize', 17)
ylabel('laser movement [cm]',  'FontSize', 17)
axis([-57 33 3 31.5])

set(gca, 'FontSize', 16)
saveas(gcf,'laser_data.png')
hold off
%}
