%{
vekt = linspace(0, 3.5, 8);
utslag = [8.18, 7.45, 6.71, 6.03, 5.23, 4.49, 3.75, 2.99]-8.18;
[m, c, delta_c, delta_m] = function1(vekt, utslag)

figure(1)
plot(vekt, utslag, 'ro');
hold on
xlabel('vekt [kg]')
ylabel('utslag [mm]')
plot(vekt, c+m*vekt)
%}

figure(1)
scatter(fut, energi/max(energi), 15, 'filled')
hold on
xlabel('Frekvens [hz]','fontsize',16)
ylabel('Relativ energi','fontsize',16)
title('Fouriertransformerte av signalet','fontsize',16)
box on
axis([0 1500 -0.05 1.05])
grid on
plot(fut, energi/max(energi))

%figure(2)
%plot(t, data)



[c index] = min(abs(fut-1207.2))
%figure(3)
index = index -1 ;
intervall= 3;
x2 = fut(1, index-intervall:index+intervall);
y2 = energi(index-intervall:index+intervall, 1);

figure(1)
% create smaller axes in top right, and plot on it
axes('Position',[0.39 0.37 0.26 0.445])
box on
scatter(x2, y2/max(y2), 15, 'filled')
ax = gca;
axis([min(x2) max(x2) -0.05 1.05])
hold on
box on
plot(x2, y2/max(y2))


