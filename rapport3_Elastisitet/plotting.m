vekt = linspace(0, 3.5, 8);
utslag = [8.18, 7.45, 6.71, 6.03, 5.23, 4.49, 3.75, 2.99]-8.18;
[m, c, delta_c, delta_m] = function1(vekt, utslag)

figure(1)
plot(vekt, utslag, 'ro');
hold on
xlabel('vekt [kg]')
ylabel('utslag [mm]')
plot(vekt, c+m*vekt)