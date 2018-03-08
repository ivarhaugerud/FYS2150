%m = e00
%{
%h = e1
%plot(m, h)
%[m, c, delta_c, delta_m] = function1(m, h)
[signal,sf]=audioread('messing_lyd.wav');
N = length(signal);
time = linspace(0, N/sf, N);
frek = 1.095e3
my_signal = transpose(max(signal)*sin(time*frek*2*pi));
signal_sum = signal+my_signal;
%plot(time, signal_sum)

%sound(signal_sum);
%soundview(signal_sum, frek)

fourier = abs(fft(signal, N, 1));
%dt = time(3)-time(2)
f = linspace(0, 1, N/2)*sf;
%L = N/sf
%plot(t, signal)
%t = sf*(0:(L/2))/L
plot(f, fourier(round(N/2)+1:end));
%}
%{
[signal,sf]=audioread('messing_lyd.wav');
%t = 0:1/50:10-1/50;
x = signal;%sin(2*pi*15*t) + sin(2*pi*20*t);
n = length(x)
size(x)
t = linspace(0, n/sf, n);

y = fft(x);     
f = (0:n-1)*sf/n;
size(f)
size(abs(y))

plot(f,abs(y))
title('Magnitude')
%}
N=1e4;
f1 = 1000;
f2 = 1400;
time=linspace(0, 1, N);
signal = sin(f1*2*pi*time)+sin(f2*2*pi*time);
[four_x, four_y] = fourier_function(time, signal)
