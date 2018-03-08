% What we really want to do is 
% a) define the data (x,y,e)
% b) define the model f(p) where p is a vector of parameters to be fitted
% c) minimize the chi-squared to estimate the parameters and use the
%    hessian at the fitted values to estimate the uncertainties
%
% The code should be re-structured so that the user doesn't have to
% define the chi-squared theirself, only the model and the initial
% guess.
%
% By scanning x0 from xmin to xmax one can find a band for the set of
% compatible lines at a given confidence level - the band is given by the
% the error on the intercept at x0.


% Define the measurements x,y,error on y (call it e)
%x = [0 1 2 3 4 5]
%y = [0 1 2 3 4 5]
%e = [1 1 1 1 1 1]

x = [full_eta(length(etta1)+1:length(full_eta)-length(etta4)); transpose(etta4(second_index:end))];
y = [inv_foo(1:end, 2); inv_foo(1:end, 3); inv_foo(second_index:end, 4)];
e = [uncertenty_last(1:end, 2); uncertenty_last(1:end, 3); uncertenty_last(second_index:end, 4)];
x0 = mean(x);

% Define the model to perform a chi-squared fit of
pname = cellstr(['Intercept';
                 'Slope    ']);
model = eval('@(p,x)p(1)+x*p(2)''');

% Define the chi-squared function to minimize and a rough guess
% of the parameter values (theta)
chisq = @(theta)sum((y-model(theta,x-x0)).^2./e.^2);
guess = [1,1];

options = optimoptions('fminunc','Algorithm','quasi-newton');
options = optimoptions(options,'Display','off');
[theta,chisqmin,EXITFLAG,OUTPUT,GRAD,HESSIAN] = fminunc(chisq,guess,options);

% The inverse of 1/2 of the hessian is the error matrix. The
% square roots of the diagonal elements are the error estimates
% for the parameters. In general there is a non-zero correlation...
%
% For whatever reason, a warning is printed about using the line-search
% algorithm because the gradient is not supplied - this can be ignored in
% general.
invHESSIAN = inv(0.5*HESSIAN)
pe=sqrt(diag(invHESSIAN));

% Plot the the data
errorbar(x,y,e,'r*')

% Plot the fitted model
xfine = linspace(min(x),max(x),100);
yfit  = model(theta,xfine-x0);
hold on
plot(xfine,yfit,'b-')
legend('data','fit')

sigma = sqrt( sum( (y-model(theta,x)).^2 ) / (size(x,2)-size(HESSIAN,1)) );

% Print the values and errors of the fitted parameters
for i=1:length(theta)
    fprintf('%9s: %f +- %f\n',char(pname(i)),theta(i),pe(i))
end

fprintf('\nSigma from residuals = %.2d\n',sigma);