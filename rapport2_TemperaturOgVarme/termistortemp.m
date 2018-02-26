function T=termistortemp(R) 
a = 8.420*10^(-4);
b = 2.068*10^(-4);
c = 8.591*10^(-8);
T = 1./(a+b*log(R)+c*(log(R)).^3);
end