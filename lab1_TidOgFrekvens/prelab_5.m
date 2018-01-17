load('data1.mat', 'data1')

n = 100;
%TASK 5
average = mean(data1)
%TASK 6
standard_deviation = std(data1)
%TASK 7
standard_deviation_in_the_mean = standard_deviation/sqrt(n) %usikker p? denne
%TASK 9
inside_1_sigma = (n - (sum(data1>average+standard_deviation)+sum(data1<average-standard_deviation)))/n
%TASK 11
inside_2_sigma = (n - (sum(data1>average+2*standard_deviation)+sum(data1<average-2*standard_deviation)))/n
