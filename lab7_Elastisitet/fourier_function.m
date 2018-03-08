function [fourier_x, fourier_y]=fourier_function(t, y)
    L = length(y);
    Fs = 1/(t(2)-t(1));
    T = 1/Fs;
    p2 = abs(fft(y)/L);
    fourier_y = p2(1:L/2+1);
    fourier_y(2:end-1) = 2*fourier_y(2:end-1);
    fourier_x = Fs*(0:(L/2))/L;
    plot(fourier_x, fourier_y)
end
