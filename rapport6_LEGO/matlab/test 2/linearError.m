function [ A,dA ] = linearError( x,y )
    % returns slope A of 'least squares'-fitted straight line A x + b
    % with associated error dA.
    n = length(x);
    E = sum( (x - mean(x)).*y );
    F = sum( (y - mean(y)).^2 );
    D = sum( (x - mean(x)).^2 );
    dAsq = (D*F-E^2)/D^2/(n-2);
    %dBsq = (D/n+mean(x)^2)*dAsq
    dA = sqrt(dAsq);
    A = E/D;
    %return [E/D,sqrt(dAsq)]
    
end

