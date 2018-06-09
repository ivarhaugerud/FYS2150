
diode2 = data(7000:1000:end, 3)*1e3;
coil2 = data(7000:1000:end, 2)*1e3;
t2 = data(700:1000:end, 1);
t2 = t2(1:14994,1);
coil2 = coil2-mean(coil2);
diode2 = diode2-mean(diode2);

size(t2)
size(coil2)
size(diode2)

x = diode2;
y = coil2;
cdata = t2;


scatter(x,y, 6.5 ,cdata, 'filled')
grid(gca,'minor')
grid on
hAx=gca;
xlabel('diode voltage [mV]', 'FontSize', 17)
ylabel('coil voltage [mV]',  'FontSize', 17)
colormap('parula');
hcb = colorbar;
colorTitleHandle = get(hcb,'title');
titleString = 'Time [s]';
set(colorTitleHandle ,'string', titleString, 'FontSize', 15, 'FontSize', 15);
saveas(gcf,'phasespace.png')
hold off
