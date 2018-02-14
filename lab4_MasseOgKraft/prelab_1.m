mass = e00;
h = e1;

[alpha, betta, delta_betta, delta_alpha] = function1(mass, h)
aprox_line = alpha*mass + betta

plot(mass, aprox_line)
hold on
plot(mass, h, '*')