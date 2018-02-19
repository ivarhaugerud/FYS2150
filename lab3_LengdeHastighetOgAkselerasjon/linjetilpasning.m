
freq_A = [10, 500, 5000, 50000, 100, 1000, 10000, 100000, 10^6] %Hz
freq_B = [10, 500, 5000, 50000, 100, 1000, 10000, 100000, 6*10^6] %Hz
amplitude_A = ([706.5, 669.9, 665, 664.5, 695.5, 667.2, 664.9, 657.6, 603])*10^(-3) %volt
amplitude_B = ([698.4,  207.3, 21.79, 2.169, 585.7, 107.3, 10.93, 1.02, 630*10^(-3)])*10^(-3) %volt

log_y = log10(amplitude_B(2:8)./amplitude_A(2:8));
log_x = log10(freq_A(2:8));
[a, b, delta_b, delta_a] = function1(log_x, log_y)
y0 = -b/a
delta_y0 = ((delta_b/b)^2 + (delta_a/a)^2)*y0
delta_exp_y0 = 10^(y0)*delta_y0
R = 10^6
C = 100*10^(-9)
w0 = 1/(R*C)
poly_foo = 10^(b)*10.^(a*log_x);
analytic = (1+(freq_A*2*pi/w0).^(2)).^(-0.5)
%loglog(10.^log_x, poly_foo)
plot(log_x, log10(poly_foo))
grid on
ylabel('$\log_{10} \mid{V_{ut}/V_{inn}}\mid$','Interpreter','latex')
xlabel({'frekvens $\log_{10} (f)$ [Hz]'},'Interpreter','latex')
hold on
legend({'$y= 1.9367 -0.9363 f$'}, 'Interpreter','latex')
plot(log10(freq_A), log10(amplitude_B./amplitude_A), '*')
delta_z = ((delta_b/b)^2 + (delta_a/a)^2)*(10^(y0))
10^(y0)

%{
% Generer et datasett
a=3.5; %Parameter for konstantledd i generert datasett
b=5.0; %Parameter for helning i generert datasett
x=0:0.1:2;
y=a+b.*x+randn(1,length(x));
figure(1)
plot(x,y,'r*')
%Tilpass med line?r modell
p=polyfit(x,y,1);
%Tilpasningsparametre m og c i y=m*x+c:
m=p(1)
c=p(2)
yline = polyval(p,x);
hold on
plot(x,yline,'-')
xlabel('x')
ylabel('y')
legend('data',['linfit: ',num2str(c),'+',num2str(m),'x'],'Location','NorthWest')
hold off


%x=linspace(0, 10, N);
%y=linspace(5, 20, N)+0.5*randn(1, N)
[m,c,delta_c,delta_m]=function1(x,y)

figure
plot(x, y, '.'); hold on
plot(x, m*x+c, '-')
%}
%plot(dfreq, u1./u0, '*')
%{
start_nr = 4
[freq_sorted, freq_order] = sort(dfreq);
new_u1 = u1(freq_order);
new_u0 = u0(freq_order);

log_y = log10(new_u1(start_nr:end)./new_u0(start_nr:end));
log_x = log10(freq_sorted(start_nr:end));
[a, b, delta_b, delta_a] = function1(log_x, log_y)
y0 = -b/a
delta_y0 = ((delta_b/b)^2 + (delta_a/a)^2)*y0
delta_exp_y0 = 10^(y0)*delta_y0
%R = 10^6
%C = 100*10^(-9)
%w0 = 1/(R*C)
poly_foo = 10^(b)*10.^(a*log_x);
%analytic = (1+(freq_A*2*pi/w0).^(2)).^(-0.5)

plot(log_x, log10(poly_foo))
grid on
ylabel('$\log_{10} \mid{V_{ut}/V_{inn}}\mid$','Interpreter','latex')
xlabel({'frekvens $\log_{10} (f)$ [Hz]'},'Interpreter','latex')
hold on
legend({'$y=1.8907 -0.9093 f$'}, 'Interpreter','latex')
plot(log10(freq_sorted), log10(new_u1./new_u0), '*')

delta_z = ((delta_b/b)^2 + (delta_a/a)^2)*(10^(y0))
10^(y0)
%10^(b)
%10^(b)*delta_b
%}