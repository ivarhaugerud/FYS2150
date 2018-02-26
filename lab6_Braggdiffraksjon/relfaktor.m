function [f]=relfaktor(U)
    e = 1.60217662e-19; %coloumb
    m = 9.10938356e-31; %kg
    c = 299792458;      %m/s
    f = 1./sqrt(1+e*U/(2*m*c^2));
end