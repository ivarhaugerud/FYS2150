
vekt = linspace(0, 3.5, 8)
utslag = [8.18, 7.45, 6.71, 6.02, 5.23, 4.49, 3.75, 2.99]-8.18;%mm
usikker = [1, 1, 1, 1, 2, 3, 3, 3]*1e-3 %mm
[m, c, delta_c, delta_m] = function1(vekt, utslag)

figure(2)
errorbar(vekt, utslag, usikker, 'o')
hold on
grid on
set(gca,'fontsize',16)
title('Nedbooying av messingstav som funksjon av last','fontsize',16)
xlabel('vekt [kg]', 'fontsize',16)
ylabel('utslag [mm]', 'fontsize',16)
plot(vekt, c+m*vekt)
plot(vekt, c+(m+delta_m)*vekt)
plot(vekt, c+(m-delta_m)*vekt)

figure(1)
scatter(fut, energi/max(energi), 15, 'filled')
hold on
set(gca,'fontsize',16)
xlabel('Frekvens [hz]','fontsize',16)
ylabel('Relativ energi','fontsize',16)
title('Fouriertransformerte av signalet','fontsize',16)
box on
axis([0 1500 -0.05 1.05])
grid on
plot(fut, energi/max(energi))

[ah index] = min(abs(fut-1207.2))
%figure(3)
index = index -1 ;
intervall= 3;
x2 = fut(1, index-intervall:index+intervall);
y2 = energi(index-intervall:index+intervall, 1);

figure(1)
% create smaller axes in top right, and plot on it
axes('Position',[0.39 0.37 0.26 0.445])
box on
set(gca,'fontsize',15)
scatter(x2, y2/max(y2), 15, 'filled')
ax = gca;
axis([min(x2) max(x2) -0.05 1.05])
hold on
box on
plot(x2, y2/max(y2))

figure(3)
diff = abs(utslag - (c+m*vekt))
p1 = errorbar(vekt, diff, usikker, 'o');
M1 = 'Absolutt differanse';
hold on
grid on
set(gca,'fontsize',16)
title('Differanse mellom maalt utslag og lin.reg','fontsize',16)
xlabel('vekt [kg]', 'fontsize',16)
ylabel('utslag [mm]', 'fontsize',16)
axis([-0.05 3.55 -0.005, 1.05*max(abs(utslag - (c+m*vekt)))])
p2 = plot(vekt, delta_m*vekt+delta_c);
M2 = 'Usikkerhet lin.reg \Delta \beta + \Delta \alpha \cdot m';
legend([p1; p2], M1, M2, 'Location','northeast', 'Interpreter','latex');

%{
Y = transpose([8.18, 7.45, 6.71, 6.02, 5.23, 4.49, 3.75, 2.99])-8.18;%mm
VEKT = linspace(0, 3.5, 8)
usikker = (3-[0, 1, 1, 1, 2, 3, 3, 3])*1e-3 %mm

W = diag(usikker)
X = [1 VEKT(1); 1 VEKT(2); 1 VEKT(3); 1 VEKT(4); 1 VEKT(5); 1 VEKT(6); 1 VEKT(7); 1 VEKT(8)]
WX = W*X
size(W)
size(Y)
WY = W*Y
WXTWX = transpose(WX)*(WX)
size(WY)
size(transpose(WX))

WXTWY = transpose(WX)*WY
beta = inv(WXTWX)*WXTWY

plot(VEKT, Y, 'o')
hold on
plot(VEKT, beta(1)+VEKT*beta(2))
%}