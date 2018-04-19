function [E]=prelab(x, R,a,N,A)
    lambda = 632.8; %nano meter - bolgelengde
    u = x/(lambda*R);
    E = a^2*(sin(N*pi*A*u)/(sin(pi*A*u))*sinc(a*u)).^2;
end