load('RC_data.mat', 'frekvens')
load('RC_data.mat', 'Vu_over_Vi')

plot(log10(frekvens),log10(Vu_over_Vi),'o')
hold on
len = length(frekvens)-8
frekvens(len:end)

p = polyfit(log10(frekvens(len:end)),log10(Vu_over_Vi(len:end)), 1)
plot(log10(frekvens(len:end)), polyval(p, log10(frekvens(len:end))))

omega_null = 10^(p(2))
x = -0.5*log10(1+(frekvens/omega_null).^2)
plot(log10(frekvens), x)
hold off


