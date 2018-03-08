%mean(data)
%std(data)
%plot(data)

x = [0, 4, 8, 12, 16, 20, 24]
y = [13.7, 12.4, 11, 9.7, 8.9, 7.9, 7.1]*1e2
[m, c, delta_c, delta_m] = function1(x, y)
%{
plot(x, y)
hold on
plot(x, m*x + c)
%}

%plot(spektrum)
x1 = 718
x2 = 1000

figure(1)
plot(spektrum)
figure(2)
new_data = spektrum(x1:x2)
background = linspace(new_data(1), new_data(end), length(new_data));
no_background = new_data-transpose(background)
normalized = no_background/max(no_background)
I_first=find(normalized>0.5, 1, 'first') 
I_last=find(normalized>0.5, 1, 'last') 
FWHM  = (I_last-I_first)*2
plot(normalized)
