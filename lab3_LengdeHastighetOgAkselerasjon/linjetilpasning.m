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
