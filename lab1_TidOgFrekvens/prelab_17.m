% variabels I will use
n = 10000;                   %number of measurments
A = 10;                      %Amplitude
mu = 0;                      %the average of the random noise is zero
sigma = 0.2*A;               %how large one sigma is
x = linspace(0, 4*pi, n) %since we have 1000 measurments a second we will divide total measurments with 1000
x2 = linspace(-7, 7, n)      %for plotting of the analytic gauss distribution later
analytic_gauss = (1/sqrt(2*pi*sigma^2))*exp(-(x2.^2)/(2*sigma^2)) %analytic gauss function I will use in the last plot

%1 - Getting the data%
accurate_data = A*sin(x);             %the data we would recive without noise and no systematics errors
noise = normrnd(mu,sigma,1, n);       %the randomly distributed gaussian noise 
drift = linspace(0, 0.5*A, n);        %the drift will go from zero to one fifth of the amplitude, this represents a systematic error which gets worse over time
real_data = accurate_data+noise+drift %this will be the measured data

%2 - Plotting the raw data%
figure
plot(x, real_data) %plotting the measured data
title('Measured value of voltage over time')
xlabel('Time [s]')      % x-axis label
ylabel('Voltage  [V]')  % y-axis label

%3 - Making histogram
figure
histogram(real_data, n/500)      %total bars are number of measurments, n, divided by 500, i thought this was an allright amount of bars, but i am unsure about what is common
title('Histogram of measured values of voltage')
xlabel('Voltage [V]')            % x-axis label
ylabel('Number of measurments')  % y-axis label

%{
    This plot tells us that there are more positive measurments of voltage, than negative measurments of voltage.
    Note that because of the x-values we chose, we have 4 local maximums, and only three local minimums. 
    Because of this we get that we have more measuremnts of voltages around +10 than around -10, this is not a lot, but it is a few.
    Another effect of this is the small drift, which means that we should have more measurments of larger values of voltage compared to values around zero, and negative values.
    We see this effect in the histogram
%}

%4 - Histogram of just the noise
figure
histogram(noise, n/500)
title('Histogram of noise on measurments')
xlabel('Noise value')            % x-axis label
ylabel('Number of measurments')  % y-axis label

%5- Histogram of just the noise, normalized with Gaussian ditribution
figure
title('Histogram of noise on measurments')
xlabel('Noise value')            % x-axis label
ylabel('Number of measurments')  % y-axis label
histogram(noise, 16, 'Normalization', 'probability')
hold on
plot(x2, analytic_gauss)
hold off

%6 - finding drift
%{
To find the value of the drift one can use the least squares method. 
To do this we can assume that we see the data and find that it starts at x=0, and is a sin function.
We can then loop over different values, for example: amplitude, frequency and drift.
The intervall we loop over is decided by looking at the graph of the raw
data and approximating by eye which intervall the different values are in.
By finding the indicies which resulted in the best approximation for the
drift we find a value of the drift. This can be done in the following
manner.

different_values = 8;
amplitudes = linspace(7, 13, different_values);
frequency = linspace(7, 13, different_values);
drift = linspace(0, 0.4*A, different_values);
difference = zeros(different_values^3);

for i=1:1:different_values
    for j=1:1:different_values
        for k=1:1:different_values
            difference(i*different_values^2+j*different_values+k) = sum((real_data))-i*j% - drift(k)*amplitudes(i)*sin(x)).^2);
        end  
    end
end

-- Another way could be to try and find the best approximation by using the
function polyval, and try to approximate the sine function with a
polynomial of first degree. By looking at the slope of this approximation we would
find the function of the drift, and can then subtract it from the data

The script would look like this:

[b, a] = polyfit(x, real_data, 1)
drift_approx = a+b*x
data_without_drift = real_data - drift_approx
%}