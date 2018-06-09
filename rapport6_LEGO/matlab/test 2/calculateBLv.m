time = data(:, 1);
coil = data(:, 2);


% startTime = 5;
t = time(1:100:end);
x = coil(1:100:end-1);
x2 = v(1:100:end);

% smooth dx
% windowSize = 3200; alpha = 4; w = gausswin(windowSize,alpha); w = w/sum(w);a = 1;
xfilt = filter1('bp',x,'fc',[0.2 0.8],'fs',500); 

dx = diff(xfilt); % filter(w,a,xfilt); %diff(x)
mcs = dx .* circshift(dx, -1);

zxix = find(mcs <= 0);
% zxix = zxix(1:2:end);
figure(6); xlabel('t [s]'); ylabel('Coil [V]'); grid;
% plot(t, x)
plot(t(zxix), zeros(size(zxix)), '+r', 'MarkerSize',10);
hold on

figure(7); xlabel('v [mm/s]'); ylabel('Coil [mV]'); grid;
hold on
delta_k = 1;
%BL = zeros(1,length(zxix)); dBL = zeros(1,length(zxix));
%t_BL = zeros(1,length(zxix));
BL = 0; dBL = 0; t_BL = 0; 
1
%clear BL dBL t_BL 
k0 = 28; deltak0 = 2; kN = 0;
i = 1;
for k = k0:deltak0:((length(zxix)-1)-kN)
    figure(6)
    plot(t(zxix(k):zxix(k+delta_k)), x(zxix(k):zxix(k+delta_k)))
    figure(7)
    plot(x2(zxix(k):zxix(k+delta_k)), 1000*x(zxix(k):zxix(k+delta_k)))
    [b, db] = linearError(1e-3*x2(zxix(k):zxix(k+1)),x(zxix(k):zxix(k+1))');
    BL(i) = b;
    dBL(i) = db;
    t_BL(i) = t(zxix(k));
    i = i + 1;
    %zx(k1) = interp1(x(zxix(k1):zxix(k1)+1), t(zxix(k1):zxix(k1)+1), 0);
end

figure(6); hold off
figure(7); hold off
figure(8); hold on
plot(t_BL(k0:end), BL(k0:end), 'or')
errorbar(t_BL(k0:end), BL(k0:end), dBL(k0:end), 'or')
%plot(zx, zeros(size(zx)), '+r', 'MarkerSize',10)
BL_v = mean(BL)
%%

Ts = mean(diff(t));                                         % Sampling Time
Fs = 1/Ts;                                                  % Sampling Frequency
Fn = Fs/2;                                                  % Nyquist Frequency
L  = length(x);

fts = fft(x)/L;                                             % Normalised Fourier Transform
Fv = linspace(0, 1, fix(L/2)+1)*Fn;                         % Frequency Vector
Iv = 1:length(Fv);                                          % Index Vector

amp_fts = abs(fts(Iv))*2;                                      % Spectrum Amplitude
phs_fts = angle(fts(Iv));                                   % Spectrum Phase

plot(amp_fts)
