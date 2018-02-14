R1 = 119.9; %ohm
R2 = R1; %ohm

delta_R1 = 0.3; %ohm
delta_R2 = delta_R1; %ohm

Fs = 1000;% sample rate [Hz]
V_E = 5; %V [amplituden til p?trykt spenning]
f_E = 10;%Hz [frekvensen til p?trykket spenning]
L = length(Vbro);

figure(1)
xlabel('tid [ms]')
ylabel('amplitude [V]')
plot(Vbro)

fourier_coeff_complex = (fft(Vbro));
fourier_coeff_real = abs(fourier_coeff_complex);
f = Fs*(0:(L/2+1))/L;
sigma_gauss = 0.05*f_E;
[min_index, max_index] = max(fourier_coeff_real);
ny = f(max_index);

figure(2)
plot(f, fourier_coeff_real(1:round(L/2+1)), 'o')
xlabel('frekvens [Hz]')
ylabel('fourier koeffisient')
hold on
gauss_func = exp(-(f - ny).^2/(2*sigma_gauss^2));
filterd_fourier = times(fourier_coeff_real(1:round(L/2+1)), gauss_func);
plot(f, filterd_fourier)

filterd_signal = real(ifft(filterd_fourier));
figure(3)
plot(f, filterd_signal)
xlabel('frekvens [Hz]')
ylabel('fiourier koeffisient')

rms_filterd = rms(filterd_signal);
rms_signal = V_E/sqrt(2); %rms value of cos or sin is 1/sqrt(2)
V_rel = rms_filterd/rms_signal
 
%Jeg syntes det er litt rart at jeg f?r s? mye lavere amplitude etter ? ha
%brukt fourier p? signalet som hadde amplitude p? rundt 2-3. Men det
%gir kanskje mening siden jeg fjerner veldig mange frekvenser ved ? bruke
%filtreringsfunksjonen, og selv om amplitudene deres var sm?, s? var det jo
%veldig mange, og det f?rer jo til at det har mye ? si for amplituden

