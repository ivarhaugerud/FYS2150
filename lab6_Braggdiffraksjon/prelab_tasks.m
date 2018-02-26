%a = [5e3, 4e4, 2e2]
%f=relfaktor(a)


data = [130, 124, 133, 131, 128, 132, 138, 192, 244, 301, 348, 403, 462, 508];
theta2 = linspace(12, 25, length(data))

plot(theta2, data)

e = 1.60217662e-19; %coloumb
m = 9.10938356e-31; %kg
c = 299792458;      %m/s
lambda_compton = 2.426e-12; %meter
another_factor = sqrt((m*c^2)./(2*e*e03));
size(another_factor)
size(lambda_compton*relfaktor(e03))
lambda = times(another_factor, lambda_compton*relfaktor(e03))
sigma_m = std(lambda./D)/(sqrt(length(e03)-1))
answer = mean((lambda./D))

a = lambda./D
a(11)
a(10)