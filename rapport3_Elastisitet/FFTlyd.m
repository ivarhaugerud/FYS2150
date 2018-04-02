% Ta opp lyd-data for å finne egenfrekvensen til messinggstaven
% Alex Read 01.03.2018 (kopierte deler av FFThastighet.m)

duration = 10.0; % s (dette bestemmer 
                 % frekvensoppløsning = 1/duration)
samplerate = 8*1024; % Hz (best med antall samples = multipel av 2)
fmin = 500; % minimum signal-frekvens

% vis antall samples
samples = duration*samplerate;
fprintf('%d samples skal registreres\n',samples)

% Gjør klar mikrofonen og samle inn data
[DS,devicename] = initDaqSession(duration,samplerate,1);
addAudioInputChannel(DS,devicename, 1);
fprintf('Go!\n\n');
[data, t] = startForeground(DS);

% vis lyd-dataene
figure(1)
plot(t,data), xlabel('tid, s'),ylabel('amplitude')

%Fouriertransformen med FFT
L = length(data);
Y = fft(data);
energi = abs(Y).^2;
fut = samplerate*linspace(0,1,L)*(L-1)/L;
figure(2)
plot(fut,energi,'.') ,xlabel('frekvens, Hz'), ylabel('Energi')

% Finn maksimum energi med  f>fmin

ifirst = find(fut>fmin,1,'first');
[emaks,imaks] = max(energi(ifirst:end/2));
ipeak = ifirst+imaks-1;
fpeak = fut(ipeak);
fprintf('Energi-topp (%d) ved f =%10.2f Hz\n',emaks,fpeak)

fprintf('Delta f = %10.2f Hz\n',max(diff(fut)))

% Zoom plot

figure(3)
plot(fut(ipeak-5:ipeak+5),energi(ipeak-5:ipeak+5),'*-') ,xlabel('frekvens, Hz')
ylabel('Energi')

%for i=ipeak-5:ipeak+5
%    fprintf('%10.2f %10.1d\n',fut(i),energi(i))
%end

filename = input('\nHvilket filnavn vil du bruke for å lagre dataene? ','s');
save(filename,'t','data','fut','energi','L')

