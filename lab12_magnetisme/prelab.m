function [D_para, D_tang]=prelab(f)
    epsilon = sqrt(1-1/f^2);
    D_para = abs((1-1/epsilon^2)*(1-1/(2*epsilon)*log((1+epsilon)/(1-epsilon))));
    D_tang = (1-D_para)/2;
    %programmet gir ut riktig verdier n?r f->0, men ikke n?r den er eksakt
    %lik null. Kunne legge inn en test, men f?ler dette er litt mot sin
    %hensikt siden dette tvinger fram riktig svar ved ? bruke fasit.
end