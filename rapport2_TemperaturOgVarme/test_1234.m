%load('varmeledning_600s.mat')
start_index = 70;
new_t = t(start_index:end)-t(start_index-1);
new_T = T(start_index:end, :);
new_R = R(start_index:end, :);
h = figure(1);
M=['os*+d']; %Plottesymboler
C=['rmgbk']; %Plottefarger
N = 4;
p1=plot(new_t, new_T(1:end, 1), 'ro');
hold on
grid on
p2=plot(new_t, new_T(1:end, 2), 'ms');
p3=plot(new_t, new_T(1:end, 3), 'g*');
p4=plot(new_t, new_T(1:end, 4), 'b+');

M1 = 'x_1';
M2 = 'x_2';
M3 = 'x_3';
M4 = 'x_4';
set(gca,'fontsize',15)
legend([p1; p2; p3; p4], M1, M2, M3, M4, 'Location','northeast', 'Interpreter','latex');
xlabel('tid [s]', 'Interpreter','latex')
ylabel('temperatur  [$^{\circ}$C]', 'Interpreter','latex')
hold off

new_start_index = 30;
new_new_T = new_T(new_start_index:end, :);
new_new_t = new_t(new_start_index:end);
new_new_R = new_R(new_start_index:end, :);
delta_R = (new_new_R*0.5/100 + 0.1e3);
uncertenty_T = sqrt(11)*delta_R./new_new_R%sqrt(11)*times(1./delta_R, log(new_new_R));
uncertenty_last = times(0.5*sqrt(pi)*exp((erfinv(2*uncertenty_T).^2)), uncertenty_T);
T1 = mean(new_new_T(:, 1))
T0 = T(1, 1)
Delta_T = T0-T1
x1 =  0.98e-3%73e-3;%14e-3;
x2 =  28.37e-3;%29e-3;
x3 =  88.70e-3;%89e-3;
x4 =  176.05e-3;%170e-3;
etta1 = x1./(sqrt(4*new_new_t));
etta2 = x2./(sqrt(4*new_new_t));
etta3 = x3./(sqrt(4*new_new_t));
etta4 = x4./(sqrt(4*new_new_t));

inv_foo = erfinv((new_new_T-T1)/Delta_T);
second_index = 52
%full_y = [inv_foo(1:end, 1);inv_foo(1:end, 2); inv_foo(1:end,3); inv_foo(second_index:end, 4)];
%full_x = transpose([etta1(1:end), etta2(1:end),etta3(1:end),etta4(second_index:end)]);
full_y = [inv_foo(1:end, 2); inv_foo(1:end,3); inv_foo(second_index:end, 4)];
full_x = transpose([etta2(1:end),etta3(1:end),etta4(second_index:end)]);
[m, c, delta_c, delta_m] = function1(full_x(1:end, 1), full_y(1:end, 1))
full_T = [new_new_T(1:end, 1); new_new_T(1:end, 2); new_new_T(1:end, 3); new_new_T(1:end, 4)];
full_eta = transpose([etta1(1:end), etta2(1:end),etta3(1:end),etta4(1:end)]);

%{
figure(4)
%hey_index = 120
%o_etta1 = x1./(sqrt(4*t(hey_index:end)));
%o_etta2 = x2./(sqrt(4*t(hey_index:end)));
%o_etta3 = x3./(sqrt(4*t(hey_index:end)));
%o_etta4 = x4./(sqrt(4*t(hey_index:end)));
p1 = plot(etta1, new_new_T(1:end, 1), 'ro')
%p1 = plot(o_etta1, T(hey_index:end, 1), 'ro')
set(gca,'fontsize',20)
xlabel('$\eta = \frac{x_i}{\sqrt{4t}}$ [ms$^{-1/2}$]', 'FontSize', 20, 'Interpreter','latex')
ylabel('temperatur  [$^{\circ}$C]', 'Interpreter','latex')
grid on
hold on
p2 = plot(etta2, new_new_T(1:end, 2), 'ms')
p3 = plot(etta3, new_new_T(1:end, 3), 'g*')
p4 = plot(etta4, new_new_T(1:end, 4), 'b+')
%p2 = plot(o_etta2, T(hey_index:end, 2), 'ms')
%p3 = plot(o_etta3, T(hey_index:end, 3), 'g*')
%p4 = plot(o_etta4, T(hey_index:end, 4), 'b+')
legend([p1; p2; p3; p4], M1, M2, M3, M4,'Location','southeast', 'Interpreter','latex');
hold off
%}

figure(3)
%p1 = plot(etta1, inv_foo(1:end, 1), 'ro');
p1 = errorbar(etta1, inv_foo(1:end, 1), uncertenty_last(1:length(etta1)), 'r')
set(gca,'fontsize',20);
xlabel('$\eta = \frac{x_i}{\sqrt{4t}}$ [ms$^{-1/2}$]', 'FontSize', 20, 'Interpreter','latex');
ylabel('erfinv$\left(\left(T(x, t)-T_1\right)/\Delta T\right)$', 'Interpreter','latex');
M1 = 'x_1';
M2 = 'x_2';
M3 = 'x_3';
M4 = 'x_4';
hold on 
grid on
a = length(etta1)
p2 = errorbar(etta2, inv_foo(1:end, 2), uncertenty_last(a+1:2*a), 'm')
%p2 = plot(etta2, inv_foo(1:end, 2), 'ms');
%p3 = plot(etta3, inv_foo(1:end, 3), 'g*');
%p4 = plot(etta4(second_index:end), inv_foo(second_index:end, 4), 'b+');
p3 = errorbar(etta3, inv_foo(1:end, 3), uncertenty_last(2*a+1:3*a), 'g')
p4 = errorbar(etta4(second_index:end), inv_foo(second_index:end, 4), uncertenty_last(3*a+second_index:4*a), 'b')
%p5 = plot(full_x, c+m*full_x, 'k-');
p5 = plot(full_x, c + 128.419083*full_x, 'k-')
M5 = 'tilpasningslinje';
legend([p1; p2; p3; p4; p5], M1, M2, M3, M4, M5,'Location','southeast', 'Interpreter','latex');
set(p5(1),'linewidth',3);
D = 1/m^2
delta_D = 2*D*delta_m/m
%{
%{
%x1 = 3.079e-3;
%x2 = 28.37e-3;
%x3 = 88.70e-3;
%x4 = 168.95e-3;
etta1 = x1./(sqrt(4*new_t));
etta2 = x2./(sqrt(4*new_t));
etta3 = x3./(sqrt(4*new_t));
etta4 = x4./(sqrt(4*new_t));
%}
%{
full_y = [inv_foo(1:end, 2); inv_foo(1:end,3); inv_foo(1:end, 4)];
full_x = transpose([etta2(1:end),etta3(1:end),etta4(1:end)]);
[m, c, delta_c, delta_m] = function1(full_x(1:end, 1), full_y(1:end, 1))
%}
%{
figure(5)
plot(full_x, full_y, 'ro')
set(gca,'fontsize',20)
xlabel('$\eta = \frac{x_i}{\sqrt{4t}}$', 'FontSize', 25, 'Interpreter','latex')
ylabel('Temperatur [c]', 'FontSize', 20)
hold on
length(etta1)
plot(full_x, c+m*full_x, '--')
D = 1/m^2
delta_D = 2*D*delta_m/m
%}
%{
figure(1)
N = 4;
plot(etta1, inv_foo(1:end, 1), 'ro');
hold on
plot(etta2, inv_foo(1:end, 2), 'bo');
plot(etta3, inv_foo(1:end, 3), 'go');
plot(etta4, inv_foo(1:end, 4), 'co');
new_t(1)
%}
%}
%}