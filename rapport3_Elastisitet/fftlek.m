%Dette er et lite skript for ? se hvor sm? frekvenser man kan skille med
%en diskret Fouriertransform og for ? f? en f?lelse av hvordan 
%energispekteret fra en diskret Fouriertransform ser ut.
%
%Skriptet lager et signal med to sinusb?lger med frekvenser f og fm der
%frekvensforskjellen er liten, dvs fm/f~1.
%
%Signalet Fouriertransformeres med fft() og energispekteret plottes.
%

%Parametre
T=1.5; %totaltid, s
fs=4000;% samplingsfrekvens, Hz
f=1000;% lydkildefrekvens, Hz
fm_f=0.999;% Relativt Doppler-skift fm/f=c/(c-v)
Ar=.7; % relativ amplitude
As=1; %st?yamplitude

%Sum av to b?lger
t=0:1/fs:T;
omega_t=2*pi*f*t;
y1=sin(omega_t);
y2=Ar*sin(fm_f*omega_t)+As*randn(length(t),1)';
y=y1+y2;
figure(1), plot(t,y),xlabel('tid, s'),ylabel('amplitude')

%Forbered Fouriertransformen med FFT
L=length(y);
NFFT = 2^nextpow2(L); % fft foretrekker vektorer med lengde 2^n
Y = fft(y',NFFT,1)/L;
fut = fs/2*linspace(0,1,NFFT/2);
figure(2),plot(fut,abs(Y(1:NFFT/2)).^2,'.-') ,xlabel('frekvens, Hz')
ylabel('Energi')
%Intensiteten er amplituden^2


