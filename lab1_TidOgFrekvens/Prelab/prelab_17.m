% variabels I will use
n = 10000;                   %number of measurments
A = 10;                      %Amplitude
mu = 0;                      %the average of the random noise is zero
sigma = 0.2*A;               %how large one sigma is
x = linspace(0, n/1000, n)   %since we have 1000 measurments a second we will divide total measurments with 1000
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
    And that the largest absolute value of voltage is on the positive side,
    due to the drift in data.
    Note that because of the x-values we chose, we have 2 full local maximums, and only one full local minimum. 
    Because of this we get that we have more measuremnts of voltages around +10 than around -10.
    Another effect of this is the small drift, which means that we should have more measurments of larger values of voltage compared to values around zero, and negative values.
    We see this effect in the histogram.
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


%6- remove the drift
new_x = linspace(0, 8*pi, n)
real_data = A*sin(new_x)+noise+2*drift                     %made the drift stronger, and the data to last for a periodic amount of measurments
drift_removed_data = detrend(real_data);                   %using function detrend which removes linear trends from data 
drift = real_data - drift_removed_data;                    %making array of the trend
mean(detrend_sdata)                                        %printing what the average of the detrended data is, to check if it removed the drift

figure
plot(new_x,real_data);                                      %plotting the real data
xlabel('Time [s]');                                         %x-label
ylabel('Voltage [V]');                                      %y-label
hold on
plot(new_x, drift,':r')                                     %plot the drift
plot(new_x, drift_removed_data,'m')                         %plot the data with removed drift
legend('Original Data','Drift','Drift removed Data')        %legend to understand which graph is which

polyfit(new_x, drift, 1)                                     %to get the value of the slope of the drift which was removed