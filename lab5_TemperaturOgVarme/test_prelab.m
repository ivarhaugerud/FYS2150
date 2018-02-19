
%{
e1 = 1
e2 = 1
e3 = 0.5
T1 = 20 %C
T2 = 60 %C
T3 = 20 %C
%}
%task 16
etta = datasett(1:end, 1);
f_inv = datasett(1:end, 2);
[m,c,delta_c,delta_m] = function1(etta, f_inv)

plot(etta, f_inv, '*')
hold on

plot(etta, c + m*etta)
plot(etta, f_inv)

%1/(m^2)