rest = [1e6, 20*1e3]
rest = 130.4e3
%rest = 0.349e6
rest = 8.91e3
T = termistortemp(rest) - 273.15 
0.922-0.669
%{
test_R = linspace(exp(7), exp(17), 100);
test_T = termistortemp(test_R);
plot(log(test_R), 1./test_T);
%}