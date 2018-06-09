%{
figure(1)
diode2 = diode(7000:1000:end)*1e3;
coil2 = coil(7000:1000:end)*1e3;
t2 = time(700:1000:end);
t2 = t2(1:10464,1);
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


figure(2);
hold on

vel = x2(7000:end)*1e3;
coi = x(7000:end)*1e3;
tim = t(700:end);
tim = tim(1:97701, 1);

scatter(vel, coi, 6.5 ,tim, 'filled')
grid(gca,'minor')
grid on
hAx=gca;
xlabel('velocity [cm/s]', 'FontSize', 17)
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

period_number = linspace(1, numel(BL)-10, numel(BL)-10);

figure(3);
hold on
errorbar(period_number, -BL(8:end-3), dBL(8:end-3), 'o')
grid(gca,'minor')
grid on
xlabel('period number [#]', 'FontSize', 17)
ylabel('slope coil vs velocity [mVs/cm]',  'FontSize', 17)
set(gca, 'FontSize', 16)
axis([-3 190 0.86 1.04])
saveas(gcf,'slope.png')

%{
scatter(vel, coi, 6.5, 'filled')
grid(gca,'minor')
grid on
hAx=gca;
xlabel('velocity [cm/s]', 'FontSize', 17)
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
