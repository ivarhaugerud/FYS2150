N=1000;
x=linspace(0, 10, N);
%y=linspace(5, 20, N)+0.5*randn(1, N);
%[m,c,delta_c,delta_m]=function1(x,y)

%figure
%plot(x, y, '.'); hold on
%plot(x, m*x+c, '-')
counter_c=0
counter_m=0
times=1000

for k = 1:times
    y=linspace(5, 25, N)+0.5*randn(1, N);
    [m,c,delta_c,delta_m]=function1(x,y);
    if c >5++delta_c
        counter_c = counter_c+1
    elseif c<5-delta_c
        counter_c = counter_c+1
    end
    if m > 2+delta_m
        counter_m = counter_m +1
    elseif m < 2-delta_m
        counter_m = counter_m +1
    end
end
100-68-(counter_c/times)*100
100-68-(counter_m/times)*100