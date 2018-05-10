function [m,c,delta_c,delta_m]=function1(x,y)
    n=length(x);
    D=(sum(x.^2))-(1/n)*sum(x)^2;
    E=sum(times(x,y)) - (1/n)*sum(x)*sum(y);
    F=sum(y.^2)-(1/n)*sum(y)^2;
    m=E/D;
    c=mean(y)-m*mean(x);
    delta_m=sqrt((1/(n-2))*(D*F-E^2)/(D^2));
    delta_c=sqrt((1/(n-2))*((D/n)+mean(x)^2)*(D*F-E^2)/(D^2));
end