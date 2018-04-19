R1 = 5e9; %nm avstand skjerm
a1 = 0.12e6; %nm spaltebredde
N1 = 1; %#spalter 
A1 = 100;  %nm avstand mellom spalter 
x1 = -5e7:10:5e7;
E = prelab(x1, R1, a1, N1, A1);
plot(x1, E);

