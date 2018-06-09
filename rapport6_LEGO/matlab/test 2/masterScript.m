
clear all
global DS
period = 300;
amplitude = 2;
coilFreq = 0.46;

background = false;
data = calibrate(period, amplitude, coilFreq, background);
%%
save('data1.mat', 'data');

%%
%data = data1;
figure(3);
title('Coil [V]')
plot(data(:,1),data(:,2))

figure(4);
title('Diode [V]')
plot(data(:,1),data(:,3))
% 
% chunkSize = 1000;
% diode = zeros(ceil(length(data(:,1))/chunkSize),1);
%%
windowSize = 8000; alpha = 4;
% w = (1/windowSize)*ones(1,windowSize);
w = gausswin(windowSize, alpha);
w = w/sum(w);

a = 1;

diode = data(:,3);
coil  = data(:,2);
time  = data(:,1);

N_iteration = 1; % filter N times

for i=(1:N_iteration)
    diode = filter(w,a,diode);
    coil  = filter(w,a,coil);
    %time = filter(w,a,time);
end
%%
armlengde = 175.; %mm 
dt = data(2,1)-data(1,1);
B = 0.0281  % - 0.0264;
A = 0.4407; %- 0.5296;
h = armlengde*( A*diode+B )'; %coilpos
v = diff(h)/dt; % mm/s

%%
figure(5);
p4=plot(v(1:100:end), coil(1:100:end-1),'.r');
title('Coil vs v');
xlabel('v [mm/s]');
ylabel('Coil [V]');
save('data_coil_v.mat', [v(1:100:end), coil(1:100:end-1)]);


%%
figure(10)
plot(time(1:100:end-1), v(1:100:end),'.r');
title('v vs tid');
ylabel('v [mm/s]');
xlabel('tid [s]');

%%
figure(11)
plot(time(1:100:end), coil(1:100:end),'.r');
title('coil vs tid');
ylabel('V [V]');
xlabel('tid [s]');
